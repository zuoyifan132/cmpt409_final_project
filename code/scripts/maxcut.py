import numpy as np
import pyquil.api as api
from grove.pyqaoa.maxcut_qaoa import maxcut_qaoa
from collections import Counter
import matplotlib.pyplot as plt

# on terminal one run qvm -S
# on another terminal run quilc -S

qvm_connection = api.QVMConnection()

first_graph = [(0, 1), (0, 2), (0, 3)]

#%%capture supresses printing. 
#get_angles() prints out a lot of stuff that we don't care about right now.
maxcut_solver = maxcut_qaoa(graph=first_graph)
betas, gammas = maxcut_solver.get_angles()

angles = np.hstack((betas, gammas))

# We take a template for quil program from the maxcut_solver.
param_prog = maxcut_solver.get_parameterized_program()
# We initialize this program with the angles we have found
prog = param_prog(angles)
# Now we can print the program. 
# Some of the values you see here are the angles we calculated earlier.
print(prog)
print("Number of gates:", len(prog))

qubits = [0, 1, 2, 3]
measurements = qvm_connection.run_and_measure(prog, qubits, trials=1000)

# This is just a hack - we can't use Counter on a list of lists but we can on a list of tuples.
measurements = [tuple(measurement) for measurement in measurements]
measurements_counter = Counter(measurements)
# This line gives us the results in the diminishing order
measurements_counter.most_common()

# We create an array of angles with correct format
angles = np.hstack((betas, gammas))
print(angles)

wf = qvm_connection.wavefunction(prog)
print("Probability amplitudes for all the possible states:")
for state_index in range(maxcut_solver.nstates):
    print(maxcut_solver.states[state_index], wf[state_index])

print("Probabilities of measuring given states:")
states_with_probs = []
for state_index in range(maxcut_solver.nstates):
    states_with_probs.append([maxcut_solver.states[state_index], np.real(np.conj(wf[state_index])*wf[state_index])])
    print(states_with_probs[-1][0], states_with_probs[-1][1])

def plot_state_histogram(states_with_probs):
    states = np.array(states_with_probs)[:,0]
    probs = np.array(states_with_probs)[:,1].astype(float)
    n = len(states_with_probs)
    plt.barh(range(n), probs, tick_label=states)
    plt.show()

plot_state_histogram(states_with_probs)





