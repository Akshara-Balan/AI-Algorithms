def print_board(board):
    """Function to print the chessboard"""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, N):
    """Check if placing a queen at (row, col) is safe"""
    # Check the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    """Recursive function to place queens using backtracking"""
    if col >= N:
        print_board(board)  # Print solution
        return True

    res = False
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen

            res = solve_n_queens_util(board, col + 1, N) or res

            board[row][col] = 0  # Backtrack

    return res

def solve_n_queens(N):
    """Main function to solve the N-Queens problem"""
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("No solution exists")

# Input: Size of the chessboard
N = int(input("Enter the number of queens: "))
solve_n_queens(N)
