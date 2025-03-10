# Design Snakes and Ladders Game

## Requirements

1. The game should have a board with a specified size.
2. The board should contain a number of snakes and ladders, each with a head and tail (for snakes) or start and end (for ladders) position.
3. Players should be able to roll `n` number of dices to determine their movement on the board.
4. The game should handle the movement of players, including interactions with snakes and ladders.
5. The game should determine the winner when a player reaches the last cell of the board.

## Classes, Interfaces, and Enums

1. The `Snake` class represents a snake on the board, with properties such as head and tail positions.
2. The `Ladder` class represents a ladder on the board, with properties such as start and end positions.
3. The `Cell` class represents a cell on the board, which may contain a snake or a ladder.
4. The `Dice` class simulates the rolling of dice, with a specified number of dice.
5. The `Player` class represents a player in the game, with properties such as name, id, and current position.
6. The `Board` class represents the game board, with methods to initialize cells, add snakes and ladders, and get a cell by position.
7. The `SnakesAndLadder` class is the main class that manages the game, including initializing the game, handling player turns, and determining the winner.
8. The `Demo` class demonstrates the usage of the Snakes and Ladders game by initializing the game and starting the play.
