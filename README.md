# <center>Quantum TSP<center/>

### Introduction

---

- TSP(Travelling Salesman Problem):
  - Given a list of cities and the distances between each pair of cities, what is the shortest

    possible route that visits each city exactly once and returns to the origin city?”(wiki)

  - It is an NP-hard problem in combinatorial optimization.

  - In our project, the distance between cities are symmetric.

  - In our project, the first and last cities are not defined.

- Classical VS Quantum:

- - Classical brute force: number of possible solutions is growing exponentially

    with each additional city.

  - Quantum TSP: polynomial speed up.

### Prerequisites

---

- Forest SKD:
  - In order to connect to Quantum Virtual Machine.
- Pyquil:
  -  Use pyquil.api, pyquil.paulis, pyquil.gates.
- Grove:
  -  QAOA: Quantum approximate optimization algorithm.
  - QAOA is an algorithm for solving a broad range of optimization problems using NISQ (Noisy Intermediate-Scale Quantum) devices.

### QAOA

---

- QAOA:
  - An algorithm that combine quantum part and classical part.
  - The quantum part prepare the quantum state and measure it , repeat the process.
  - The classical part use Nelder-Mead algorithm find the most improved angles iteratively.
- betas, gammas = QAOA_inst.get_angles()
  - Beta and gammas are the angles that we got.
- most_common_result, _ = QAOA_inst.get_string(betas, gammas, samples=50000)
  - By knowing the angles, we can get the most common results. Since the result is probabilistic, we should find the most common result.

### Problem representation

---

- Graph:

  - For example, we want to present 3 cities: [(1,2), (3,4), (5,7)]

  - The distance matrix is:

    [[0, 2.82842712, 6.40312424] 

    [2.82842712 0. 3.60555128] 

    [6.40312424 3.60555128 0. ]]

  - Cost function is the sum of the cost we want to minimize.

### Encode Problem

---

- Points representation:
  - [0,1,2,3 ] means city 0 to 1 to ... 3
- Time-city matrix:
  - row represents time slots,
  - columns represent cities
  - Point representation and time-city matrix are interchangeable.

### Solving TSP

---

- Naïve Approach

  - Start with 3 cities, calculate the best distance(fig 1.1)

  - Then go for more cities...

  - Use *ForestTSPSolverNaive()* to solve the whole problem.

  - Naive solution: [0,1,2,2]

    <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt409/cmpt409_final_project/Picture1.png" alt="Picture1" style="zoom:48%;" />

- Naïve Approach Contd.

  -  The output doesn’t make sense(fig 2.1)

  -  One big reason is that *ForestTSPSolverNaive()* doesn’t have enough constraints. – Adding penalties to the solver

    <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt409/cmpt409_final_project/Picture2.png" alt="Picture2" style="zoom:48%;" />

- Improved naïve approach:

  - Create penalty matrices - add huge penalty for the states we don't want.
  - Example of 3 cities
    - At t = 0, only possible states are 100,010,001. So we penalize other states by creating an operator matrix(fig 3.1), such operator ignores 100,010,001 and 111 and penalizes the rest states.
    - To penalize state 111, it requires a little bit of linear algebra.
    - After we combine those operators to the final operator, we can implement it in QAOA.

- Summary:

  - Naïve approach summary:
    - QAOA - An algorithm that combine quantum part and classical part.
    - Initially not good enough to solve TSP due to the missing of constraints.
    - Encoding constraints and costs in QAOA to solve TSP.
  - Possible improvements:
    - Tuned parameters
    - More compact encoding
    - Check for changes dynamically

