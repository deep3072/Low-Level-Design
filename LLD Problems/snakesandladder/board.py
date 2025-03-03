from cell import Cell
from snake import Snake
from ladder import Ladder
import random

class Board:
    def __init__(self, board_size, snakes, ladders):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders
        self.cells = self.initialize_cells(board_size)
        self.add_snakes_and_ladders(snakes, ladders)

    def initialize_cells(self, board_size):
        cells = [[Cell() for _ in range(board_size)] for _ in range(board_size)]
        return cells
    
    def add_snakes_and_ladders(self, snakes, ladders):
        for _ in range(snakes):
            snake_tail = random.randint(1, self.board_size * self.board_size - 1)
            snake_head = random.randint(snake_tail+1, self.board_size * self.board_size - 1)
            
            print("Snake head: ", snake_head)
            print("Snake tail: ", snake_tail)
            print("\n")
            
            snake_obj = Snake(snake_head, snake_tail)

            cell = self.getCell(snake_head)
            cell.snake = snake_obj

        for _ in range(ladders):
            ladder_start = random.randint(1, self.board_size * self.board_size - 1)
            ladder_end = random.randint(ladder_start+1, self.board_size * self.board_size - 1)
            
            print("Ladder start: ", ladder_start)
            print("Ladder end: ", ladder_end)
            print("\n")

            ladder_obj = Ladder(ladder_start, ladder_end)

            cell = self.getCell(ladder_start)
            cell.ladder = ladder_obj
    
    def getCell(self, position: int) -> Cell:
        row = position // self.board_size
        col = position % self.board_size
        return self.cells[row][col]