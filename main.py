import matplotlib.pyplot as plt
import numpy as np
import time
import random

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

def monte_carlo_simulation(runs, n):
    times = []
    nodes_counts = []
    for _ in range(runs):
        start_time = time.time()
        solution, nodes = solve_n_queens_monte_carlo(n)
        end_time = time.time()
        times.append(end_time - start_time)
        nodes_counts.append(nodes)
    return times, nodes_counts

def plot_queens(board):
    """Plot the positions of queens on the chess board."""
    n = len(board)
    grid = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                grid[i, j] = 1

    plt.imshow(grid, cmap='gray', interpolation='none')
    plt.grid(which='major', axis='both', linestyle='--', color='yellow', linewidth=2)
    plt.xticks(np.arange(0, n, 1))
    plt.yticks(np.arange(0, n, 1))
    plt.title('12-Queens Solution')
    plt.show()
