import random

# Create an empty board (6 rows, 7 columns)
board = [[" " for _ in range(7)] for _ in range(6)]

# simple check for board size
assert len(board) == 6, "Board must have 6 rows"
assert len(board[0]) == 7, "Board must have 7 columns"

# printing the board
def print_board():
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("  1   2   3   4   5   6   7") 

# decorator to log moves
def log_move(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            print(f"Move made: {args}")
        return result
    return wrapper

# dropping a piece (actual move)
@log_move
def drop_piece(col, piece):
    for row in range(5, -1, -1): 
        if board[row][col] == " ":
            board[row][col] = piece
            return True
    return False 

# simulate dropping a piece
def simulate_drop_piece(col, piece):
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return row  # return row index
    return -1  # column full

# Checking for a win
def check_win(piece):
    # horizontal
    for r in range(6):
        for c in range(4):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # vertical
    for c in range(7):
        for r in range(3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # diagonal
    for r in range(3):
        for c in range(4):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for r in range(3, 6):
        for c in range(4):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False


def ai_move_medium(ai_piece, human_piece):
    # Check for winning move
    for c in range(7):
        if board[0][c] == " ":
            row = simulate_drop_piece(c, ai_piece)
            if check_win(ai_piece):
                board[row][c] = " " 
                return c
            board[row][c] = " " 

    # Check for blocking human's winning move
    for c in range(7):
        if board[0][c] == " ":
            row = simulate_drop_piece(c, human_piece)
            if check_win(human_piece):
                board[row][c] = " " 
                return c
            board[row][c] = " "  

    # Otherwise, pick random available column
    available_cols = [c for c in range(7) if board[0][c] == " "]
    return random.choice(available_cols)


print("Welcome to Connect Four")
print("Choose an option:")
print("1. Play with a friend")
print("2. Play with plAIer")

while True:
    try:
        choice = int(input("Enter 1 or 2: "))
        assert choice in [1, 2], "Please enter 1 or 2."
        break
    except ValueError:
        print("Invalid input. Enter a number 1 or 2.")
    except AssertionError as e:
        print(e)

# Get player names 
if choice == 1:
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
else:
    player1_name = input("Enter your name: ")
    player2_name = "plAIer"

players = { "X": player1_name, "O": player2_name }

# Initialize list to store game moves
game_moves = []  

# main game loop
player = "X"
print("Connect Four Game")
print_board()

while True:
    try:
        if players[player] == "plAIer":
            human_piece = "X" if player == "O" else "O"
            col = ai_move_medium(player, human_piece)
            print(f"plAIer chooses column {col+1}")
        else:
            col = int(input(f"{players[player]} ({player}), choose a column (1-7): ")) - 1
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
        # store move
    game_moves.append((players[player], player, col+1))  
    print_board()
    # win checking
    if check_win(player):
        print(f"{players[player]} ({player}) wins")

        # export game moves to a file
        with open("game_log.txt", "w") as f:
            f.write("Game Moves Log\n")
            f.write("---------------------------\n")
            for i, move in enumerate(game_moves, start=1):
                f.write(f"Move {i}: {move[0]} ({move[1]}) -> Column {move[2]}\n")
            f.write(f"\nWinner: {players[player]} ({player})\n")
        print("Game data saved to game_log.txt")
        break

    # switch player
    player = "O" if player == "X" else "X"
