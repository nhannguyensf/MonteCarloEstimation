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

def solve_nq_util(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nq_util(board, col + 1) == True:
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if solve_nq_util(board, 0) == False:
        return False

    return board

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

def monte_carlo_simulation(runs, n):
    times = []
    for _ in range(runs):
        start_time = time.time()
        solve_n_queens(n)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


print('Monte Carlo simulation for solving 12-Queens problem')

# Calling the main function to solve the 12-Queens problem and print the solution board
n_queens = 12
solution_board = solve_n_queens(n_queens)

# Printing the solution board if a solution exists
if solution_board:
    for row in solution_board:
        print(" ".join(str(x) for x in row))
else:
    print("No solution found for the 12-Queens problem.")
