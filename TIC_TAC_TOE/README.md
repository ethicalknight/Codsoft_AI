Tic-Tac-Toe Game
Overview
This is a simple command-line implementation of the classic Tic-Tac-Toe game, where a human player competes against an AI opponent. The AI uses the Minimax algorithm to make optimal moves, ensuring a challenging gameplay experience.

Features
Play against an AI opponent.
Simple command-line interface.
The AI uses the Minimax algorithm for decision-making.
Detects win conditions and ties.
Requirements
Python 3.x
No additional libraries are required, as the game uses built-in Python functionalities.
Installation
Clone the Repository:

bash

Run
Copy code
git clone https://github.com/ethicalknight/Codsoft_AI.git
cd Codsoft_AI
cd TIC_TAC_TOE
Run the Game:

Open your terminal and navigate to the directory where the tic_tac_toe.py file is located.
Run the following command:
bash

Run
Copy code
python tic_tac_toe.py
How to Play
The game board is a 3x3 grid, indexed as follows:


Run
Copy code
Row 0: [0, 0] [0, 1] [0, 2]
Row 1: [1, 0] [1, 1] [1, 2]
Row 2: [2, 0] [2, 1] [2, 2]
When prompted, enter your move in the format row column (e.g., 0 0 for the top-left corner).

The AI will make its move automatically after your turn.

The game will announce the winner or if the game ends in a tie.

Example Gameplay

Run
Copy code
Welcome to Tic-Tac-Toe!
| | | 
-----
| | | 
-----
| | | 
Enter your move (row and column): 1 1
AI is making a move...
| | | 
-----
|X| | 
-----
| |O| 
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Inspired by the classic Tic-Tac-Toe game.
AI logic implemented using the Minimax algorithm.