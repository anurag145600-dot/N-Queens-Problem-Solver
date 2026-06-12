# N-Queens Problem Solver

## Overview

This project is a Python implementation of the classic N-Queens Problem using the Backtracking Algorithm.

The objective is to place N queens on an N × N chessboard such that no two queens threaten each other. The program uses a 2D array representation of the chessboard and recursively searches for valid queen placements.

## Features

* 2D Chessboard Representation
* Backtracking Algorithm
* Recursive Solution Search
* Safe Position Validation
* Solution Export to File
* Input Validation
* Error Handling

## Technologies Used

* Python
* Recursion
* Backtracking
* File Handling

## How It Works

The algorithm places queens column by column.

For every position:

1. Check if the queen can be safely placed.
2. If safe, place the queen.
3. Move to the next column.
4. If no valid position exists, backtrack and try another placement.

This process continues until a valid solution is found.

## Project Structure

N_Queens_Problem/

├── screenshots/

├── n_queens.py

├── solutions.txt

├── README.md

└── requirements.txt

## Sample Output

For N = 4:

. . Q .

Q . . .

. . . Q

. Q . .

## Screenshots

* Program Start
* N = 4 Solution
* N = 8 Solution
* Solutions File
* Invalid Input Handling
* Small Number Error Handling

## Learning Outcomes

* Recursion
* Backtracking
* Constraint Satisfaction Problems
* Algorithm Design
* File Handling
* Problem Solving

## Author

Anurag

B.Tech CSE (AI & ML)