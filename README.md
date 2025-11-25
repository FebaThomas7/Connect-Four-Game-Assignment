# Connect Four Game – Python

# Student Details

Student Number: 3521404

Student Name: Feba Rachel Thomas

# Introduction

This repository contains a fully functional text-based Connect Four game written in Python. The game allows two players to take turns dropping pieces into a 6×7 grid. The project demonstrates Python fundamentals, game logic, input validation, and file handling.

# Current Goal

The aim of this project is to build an intermediate-level version of Connect Four that:

* Runs entirely in the terminal

* Uses clean and readable Python code

* Includes strong input validation

* Correctly checks for horizontal, vertical, and diagonal wins

* Saves all moves and the winner to a game_log.txt file

# Stages of the Project

1. Understanding the Game Rules

* The game is played on a 6×7 grid.

* Two players take turns dropping pieces into a column.

* A player wins by connecting four pieces horizontally, vertically, or diagonally.

* If a column is full, the player must choose a different column.

2. Setting Up the Project

* Created a project folder.

* Added the main Python file: game.py.

3. Features Implemented
   
* Board Setup

* A 6×7 grid created using Python lists.

* Function to print the board neatly in the terminal.

 User Input & Validation

* Players enter their names.

* Symbols assigned: Player 1 → X, Player 2 → O.

 Input validation using:

* try/except for handling non-numeric input

* assert to check valid column range

* Full-column detection

Gameplay Mechanics

* Function to drop a piece into a valid column.

* Automatic turn switching between players.

* Every move stored in a list for logging.

Win Detection

Implemented for all directions:

* Horizontal

* Vertical

* Diagonal

Game Log Export

At the end of the game, all moves are written to game_log.txt, including:

* Move number

* Player name and symbol

* Column chosen

* Winner

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

This project demonstrates the full implementation of a classic Connect Four game using Python. It includes clean game logic, player input handling, win checking, and log file generation. It serves as a strong example of structured programming and Python fundamentals.
