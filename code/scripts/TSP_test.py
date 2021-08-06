from forest_tsp_solver_naive import ForestTSPSolverNaive
from scripts import utilities
from scripts import plots
import matplotlib.pyplot as plt


# cities = utilities.create_cities(3)
cities = np.array([[0, 4],[0, 0],[3, 0]])
distance_matrix = utilities.get_distance_matrix(cities)
plots.plot_cities(cities)
plt.show()

tsp_solver = ForestTSPSolverNaive(distance_matrix, use_constraints=True)
solution, naive_distribution = tsp_solver.solve_tsp()
print("The solution is:", solution)