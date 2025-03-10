# Design a Tic Tac Toe Game

## Requirements

1. The game should have a nxn board.
2. Two players should be able to play the game, taking turns to place their pieces (X or O) on the board.
3. The game should check for a winner after each move.
4. The game should detect a draw if all cells are occupied and there is no winner.

## Classes, Interfaces, and Enums

1. The `PieceType` enum represents the types of pieces (X and O) that players can use.
2. The `PlayingPiece` class represents a playing piece on the board, with a specific type (X or O).
3. The `PlayingPieceX` and `PlayingPieceO` classes are specific implementations of the `PlayingPiece` class for X and O pieces, respectively.
4. The `Player` class represents a player in the game, with properties such as name and the piece they use.
5. The `Board` class represents the game board, with methods to place pieces, check for valid moves, check for a winner, and display the board.
6. The `TicTacToeGame` class is the main class that manages the game, including initializing the game, handling player turns, and determining the winner.
7. The `Demo` class demonstrates the usage of the Tic Tac Toe game by initializing the game and starting the play.
