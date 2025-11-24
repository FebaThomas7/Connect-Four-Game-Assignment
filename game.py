# making an empty board (6 rows, 7 columns)
board = [[" " for _ in range(7)] for _ in range(6)]

# simple check for board size
assert len(board) == 6, "Board must have 6 rows"
assert len(board[0]) == 7, "Board must have 7 columns"

# printing the board
def print_board():
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("  1   2   3   4   5   6   7") 

# dropping a piece
def drop_piece(col, piece):
    for row in range(5, -1, -1): 
        if board[row][col] == " ":
            board[row][col] = piece
            return True
    return False 

# Checking for a win 
def check_win(piece):
    # horizontal
    for r in range(6):
        for c in range(4):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # vertical
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # diagonal
    for r in range(3):
        for c in range(4):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for r in range(3, 6):
        for c in range(4):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# main game loop
player = "X"
print("Connect Four Game")
print_board()

while True:
    try:

        col = int(input(f"Player {player}, choose a column (1-7): ")) - 1

        # Correctness check using assert
        assert 0 <= col <= 6, "Column number must be between 1 and 7"

    except ValueError:
        print("Please enter a valid number.")
        continue
    except AssertionError as e:
        print(e)
        continue
        
    # trying to drop piece
    if not drop_piece(col, player):
        print("Column is full. Try another one.")
        continue

    print_board()
    
    # win checking
    if check_win(player):
        print(f"Player {player} wins")
        break

    # switch player
    player = "O" if player == "X" else "X"

