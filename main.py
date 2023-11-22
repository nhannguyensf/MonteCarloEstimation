import random
import time
import matplotlib.pyplot as plt
import numpy as np

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_monte_carlo(board, col, node_count):
    if col >= len(board):
        return True

    children = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            children.append(i)

    random.shuffle(children)  # Shuffle to ensure random selection

    for i in children:
        board[i][col] = 1
        node_count[0] += 1  # Increment node count
        if solve_nq_monte_carlo(board, col + 1, node_count):
            return True
        board[i][col] = 0

    return False

def solve_n_queens_monte_carlo(n):
    board = [[0] * n for _ in range(n)]
    node_count = [0]  # Initialize node count
    if not solve_nq_monte_carlo(board, 0, node_count):
        return False, node_count[0]
    return board, node_count[0]

def solve_n_queens_monte_carlo_with_timing(n):
    start_time = time.time()
    board, node_count = solve_n_queens_monte_carlo(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return board, node_count, execution_time

def plot_queens(board, run_no):
    """Plot the positions of queens on a chess board with a checkerboard pattern."""
    n = len(board)
    grid = np.zeros((n, n))

    # Create a checkerboard pattern
    grid[1::2, ::2] = 1
    grid[::2, 1::2] = 1

    plt.imshow(grid, cmap='gray', interpolation='none')
    plt.grid(which='major', axis='both', linestyle='-', color='black', linewidth=2)

    # Place queens on the board
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                plt.text(j, i, '♛', fontsize=20, ha='center', va='center', color='red')

    plt.xticks(np.arange(0, n, 1))
    plt.yticks(np.arange(0, n, 1))
    plt.title(f'12-Queens Solution ({run_no})')
    plt.show()

# Now we will run the program to solve the 12-Queens problem using Monte Carlo approach and plot the solution
total_time = 0
total_counts = 0
for i in range(10):
    n_queens = 12
    solution_board_mc, node_count_mc, execution_time_mc = solve_n_queens_monte_carlo_with_timing(n_queens)
    if solution_board_mc:
        print(f'Execution Time: {execution_time_mc:.9f} seconds')
        print(f'Node Counted: ', node_count_mc)
        total_time += execution_time_mc
        total_counts += node_count_mc
        plot_queens(solution_board_mc, i)
    else:
        print('No solution found.')
print('Total time: ', total_time)
print('Total nodes counted: ', total_counts)
