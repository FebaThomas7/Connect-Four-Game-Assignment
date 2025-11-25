import random
import tkinter as tk

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

# dropping a piece 
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
            return row  
    return -1 

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

# AI move
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
    
# GUI
class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.player = "X"
        self.game_moves = []
        self.buttons = []
        self.labels = [[None]*7 for _ in range(6)]
        self.choice_frame()

    # Choice screen
    def choice_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        tk.Label(self.frame, text="Choose an option:", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Button(self.frame, text="Play with a friend", font=("Arial",12), width=20, bg="lightblue", command=lambda: self.start_game(1)).pack(pady=5)
        tk.Button(self.frame, text="Play with plAIer", font=("Arial",12), width=20, bg="lightgreen", command=lambda: self.start_game(2)).pack(pady=5)

    def start_game(self, mode):
        self.mode = mode
        self.frame.destroy()
        self.name_frame()

    # Name entry screen
    def name_frame(self):
        self.name_f = tk.Frame(self.root)
        self.name_f.pack(pady=20)
        tk.Label(self.name_f, text="Enter Player 1 name:", font=("Arial",12)).grid(row=0, column=0)
        self.p1_entry = tk.Entry(self.name_f, font=("Arial",12))
        self.p1_entry.grid(row=0, column=1)
        if self.mode == 1:
            tk.Label(self.name_f, text="Enter Player 2 name:", font=("Arial",12)).grid(row=1, column=0)
            self.p2_entry = tk.Entry(self.name_f, font=("Arial",12))
            self.p2_entry.grid(row=1, column=1)
        tk.Button(self.name_f, text="Start Game", font=("Arial",12), bg="orange", command=self.setup_game).grid(row=2, columnspan=2, pady=10)

    # Setup board
    def setup_game(self):
        player1_name = self.p1_entry.get()
        player2_name = self.p2_entry.get() if self.mode == 1 else "plAIer"
        self.players = {"X": player1_name, "O": player2_name}
        self.name_f.destroy()
        self.build_board()
        self.update_status(f"{self.players[self.player]}'s turn ({self.player})")

    # Build GUI board
    def build_board(self):
        self.board_frame = tk.Frame(self.root, bg="lightpink")
        self.board_frame.pack(pady=10)
        self.status_label = tk.Label(self.root, text="", font=("Arial",14,"bold"))
        self.status_label.pack(pady=5)

        for c in range(7):
            btn = tk.Button(self.board_frame, text=str(c+1), width=4, height=1, font=("Arial",12,"bold"), bg="white", command=lambda col=c: self.make_move(col))
            btn.grid(row=0, column=c, padx=2, pady=2)
            self.buttons.append(btn)

        for r in range(6):
            for c in range(7):
                lbl = tk.Label(self.board_frame, text=" ", width=4, height=2, borderwidth=2, relief="ridge", font=("Arial",16,"bold"), bg="skyblue")
                lbl.grid(row=r+1, column=c, padx=2, pady=2)
                self.labels[r][c] = lbl

    def update_status(self, msg):
        self.status_label.config(text=msg)

    # Make move
    def make_move(self, col):
        if self.players[self.player] == "plAIer":
            human_piece = "X" if self.player == "O" else "O"
            col = ai_move_medium(self.player, human_piece)
            self.update_status(f"plAIer chooses column {col+1}")

        if not drop_piece(col, self.player):
            self.update_status("Column is full. Try another one.")
            return

        self.game_moves.append((self.players[self.player], self.player, col+1))
        self.update_labels()
        print_board()

        if check_win(self.player):
            self.update_status(f"{self.players[self.player]} ({self.player}) wins")
            self.save_game()
            for btn in self.buttons:
                btn.config(state="disabled")
            return

        self.player = "O" if self.player == "X" else "X"
        self.update_status(f"{self.players[self.player]}'s turn ({self.player})")

        # AI move if needed
        if self.players[self.player] == "plAIer":
            self.root.after(500, lambda: self.make_move(None))

    # Update board labels with colors
    def update_labels(self):
        for r in range(6):
            for c in range(7):
                piece = board[r][c]
                if piece == "X":
                    self.labels[r][c].config(text="X", bg="green", fg="white")
                elif piece == "O":
                    self.labels[r][c].config(text="O", bg="orange", fg="black")
                else:
                    self.labels[r][c].config(text=" ", bg="skyblue")

    # Save moves to file
    def save_game(self):
        with open("game_log.txt", "w") as f:
            f.write("Game Moves Log\n")
            f.write("---------------------------\n")
            for i, move in enumerate(self.game_moves, start=1):
                f.write(f"Move {i}: {move[0]} ({move[1]}) -> Column {move[2]}\n")
            f.write(f"\nWinner: {self.players[self.player]} ({self.player})\n")
        print("Game data saved to game_log.txt")


root = tk.Tk()
game = ConnectFourGUI(root)
root.mainloop()
