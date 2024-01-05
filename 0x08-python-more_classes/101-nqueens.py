#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if placing a queen in a specific position is safe."""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    """Print the chessboard with queens placed."""
    n = len(board)
    for row in range(n):
        line = ["Q" if i == board[row] else "." for i in range(n)]
        print("".join(line))
    print()

def solve_nqueens(board, row, n):
    """Recursively solve the N-Queens problem."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def nqueens(N):
    """Main function to solve the N-Queens problem."""
    try:
        n = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
