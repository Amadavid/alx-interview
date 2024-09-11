#!/usr/bin/python3
"""
    Module implementing solution to the N Queens problem

"""
import sys


def is_possible(board, row, col):
    """Check if its possible to place a queen at given position"""
    for i in range(row):
        if board[i] == col or board[i] - i == \
                col - row or board[i] + i == col + row:
            return False
    return True


def backtrack(n, board, row):
    """Recursively solve the N Queens problem"""
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if is_possible(board, row, col):
            board[row] = col
            backtrack(n, board, row + 1)


def print_board(board):
    """Prints the solved N Queens board"""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def main():
    """Program entry point -  reads cmdline inputs"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    backtrack(n, board, 0)


if __name__ == "__main__":
    main()
