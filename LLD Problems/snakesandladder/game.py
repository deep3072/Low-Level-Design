from board import Board
from dice import Dice
from player import Player
from collections import deque

class SnakesAndLadder:
    def __init__(self):
        self.players = deque()
        self.board = None
        self.dice = None
        self.winner = None

    def initialize_game(self):
        self.board = Board(board_size=10, snakes=5, ladders=5)
        self.dice = Dice(dice_count=1)

        player1 = Player("Jack", 1)
        player2 = Player("Jill", 2)

        self.players = deque([player1, player2])

        print("Game initialized!")

    def play(self):
        # until there is no winner keep playing
        # for every turn, roll the dice, move the player to the new position
        # check if it is a snake or ladder, move accordingly
        # check if the player has won
        # if yes, print the winner and break the loop
        while not self.winner:
            player_turn = self.get_player_turn()
            print(f"{player_turn.name}'s turn, current position: {player_turn.position}")
            
            dice_value = self.dice.roll()
            print(f"Dice value: {dice_value}")

            new_position = player_turn.position + dice_value
            new_position = self.check_snake_or_ladder(new_position)
            
            if new_position >= self.board.board_size * self.board.board_size-1:
                player_turn.position = self.board.board_size * self.board.board_size-1
                self.winner = player_turn
                break
            player_turn.position = new_position
            print(f"{player_turn.name} moved to position {player_turn.position}\n")

        print("Winner is: ", self.winner.name)

    def get_player_turn(self):
        player_turn = self.players.popleft()
        self.players.append(player_turn)
        return player_turn
    
    def check_snake_or_ladder(self, position):
        if position >= self.board.board_size * self.board.board_size:
            return position
        cell = self.board.getCell(position)
        if cell.snake:
            print(f"Snake found at position {position}")
            return cell.snake.tail
        elif cell.ladder:
            print(f"Ladder found at position {position}")
            return cell.ladder.end
        
        print("No snake or ladder found")
        return position
