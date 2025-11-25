# Connect Four Game – Python

# Student Details

Student Number: 3521404

Student Name: Feba Rachel Thomas

# Project Description

A text based Connect Four game in Python, featuring both Human vs Human and Human vs AI (plAIer) modes. The game demonstrates Python fundamentals, structured programming, input validation, logging, and simple AI integration.

# Features

1) Runs entirely in the terminal

2) Full input validation:

* Handles non-numeric input.

* Validates column selection (1–7).

* Detects full columns.

3) Win detection in all directions: horizontal, vertical, and diagonal.

4) Moves are logged using a decorator and saved to game_log.txt.

# Advance Features

1) Human vs Human and Human vs AI modes.

## Medium-level heuristic AI:

* Checks for winning moves.

* Blocks the player’s potential wins.

* Chooses random columns otherwise.


# Implementation

1) Board Setup

* 6×7 grid using Python lists.

* Neatly printed in the terminal.

2) User Input & Validation

* Players enter their names.

* Player symbols: X → Player 1, O → Player 2 / plAIer.

* Input validated using try/except and assert.

3) Gameplay Mechanics

* Drop pieces into chosen columns.

* Automatic turn switching between players.

* Store every move for logging.

4) Win Detection

* Checks horizontal, vertical, and diagonal connections.

5) Game Log Export

* Moves logged with move number, player name, symbol, and column chosen.

* Winner recorded at the end in game_log.txt.

# Project Structure
Connect-Four-Game-Assignment

* game.py        - Main game file
* game_log.txt   - Auto generated after each completed game
* README.md      - Project documentation

# How to Run the Game

* Use Python

* Open the terminal inside the project folder

* Run the game using: game.py
  
* Enter player names when prompted.

* Play the game

# Conclusion

This project demonstrates the full implementation of a classic Connect Four game using Python with both Human vs Human and Human vs AI modes. It includes clean game logic, Input validation and error handling, Medium level AI heuristic, Logging moves and game result.
