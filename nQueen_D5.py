# Taking number of queens as input from user
print("Enter the number of queens")
N = int(input())

# Taking the position of the first queen as input from the user
print("Enter the row and column index (0-indexed) for the first queen (separated by space):")
first_queen_row, first_queen_col = map(int, input().split())

# Create a chessboard NxN matrix with all elements set to 0
board = [[0] * N for _ in range(N)]

# Place the first queen on the board
board[first_queen_row][first_queen_col] = 1

def attack(i, j):
    # checking vertically and horizontally
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonally
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queens(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queens(n - 1) == True:
                    return True
                board[i][j] = 0
    return False

# Use backtracking to place the remaining queens
if not N_queens(N - 1):
    print("Solution does not exist")
else:
    # Print the final N-queens matrix
    for i in board:
        print(i)
