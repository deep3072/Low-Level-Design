from board import Board
from collections import deque

class TicTacToeGame:
    def __init__(self, players: deque):
        self.board = Board(3)
        self.players = players

    def start_game(self):
        winner = None
        while winner is None:
            # check if board is occupied if it is draw
            if all(cell is not None for row in self.board.board for cell in row):
                print("It's a draw!")
                break

            print(f"{self.players[0].name}'s turn. Enter row, column format to place your piece. (0-based index)")
            row, col = map(int, input().split())

            if not self.board.is_valid_move(row, col):
                print("Invalid move or position already occupied. Try again.")
                continue

            self.board.place_piece(row, col, self.players[0].piece)

            self.board.display()

            if self.board.check_winner() is True:
                winner = self.players[0]
                print(f"{winner.name} wins!")
                break
            self.players.rotate()