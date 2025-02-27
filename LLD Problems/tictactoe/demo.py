from playing_piece import PlayingPieceX, PlayingPieceO
from tictactoegame import TicTacToeGame
from collections import deque
from player import Player

class Demo:
    def initialize_game():
        crossPiece = PlayingPieceX()
        circlePiece = PlayingPieceO()

        player1 = Player("Player 1", crossPiece)
        player2 = Player("Player 2", circlePiece)

        players = deque([player1, player2])

        tictactoe = TicTacToeGame(players)
        tictactoe.start_game()




if __name__ == "__main__":
    Demo.initialize_game()