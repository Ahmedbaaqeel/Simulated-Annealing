
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def objective_function(state):
    count = 0  # Number of times the queens can attack each other
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:  # Attacking queens on the same row
                count += 1
            if abs(state[i] - state[j]) == abs(i - j):  # Attacking queens on the diagonal
                count += 1

    return count


def is_goal(state):
    # Check if no queens are attacking then return True
    if objective_function(state) == 0:
        return True
    else:
        return False


def simulated_annealing(initial_state, initial_T=1000):
    T = initial_T
    current_stat = initial_state
    iters = 0
    N = len(initial_state)
    e = 2.718281828

    while True:
        T = T * 0.95
        if T < 1e-14:
            return current_stat, iters  # returning the goal state and iterations
        rnd_queen = np.random.choice(range(N))
        # getting a random value to put in a random queen place
        rnd_val = np.random.choice(
            [i for i in range(N) if i != current_stat[rnd_queen]])
        next = list(current_stat)
        # changing the random queen value in the current state
        next[rnd_queen] = rnd_val
        next = tuple(next)

        # Measure of how good the next step is
        deltaE = objective_function(current_stat) - objective_function(next)
        if deltaE > 0:
            current_stat = next
        else:
            u = np.random.uniform()

            if u <= e ** (deltaE / T):  # accept the next state with probability e^(deltaE/T)
                current_stat = next
        iters += 1  # Number of iterations

def visualize_nqueens_solution(n_queens, file_name):
#n_queens = (0,1,1,3)
    N = len(n_queens)
    rows = N
    colms = N
    array_2d = [[0 for i in range(colms)] for j in range(rows)] # initilize 
    
    for j in range(N):
        for i in range(N):
            if n_queens[j] == i: # if the colm has a value at a level equal to rows then = 1
                array_2d[i][j] = 1

    plt.figure(figsize=(N, N))
    ax = sns.heatmap(array_2d, cmap='Purples', linewidths= 1.5, linecolor='k',cbar=False)
    ax.invert_yaxis()
    plt.savefig(file_name)
    plt.close()
    
            

                
                
