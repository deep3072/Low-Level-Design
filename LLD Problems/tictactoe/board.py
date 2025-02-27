from playing_piece import PlayingPiece

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def place_piece(self, row: int, col: int, piece: PlayingPiece):
        if self.board[row][col] is None:
            self.board[row][col] = piece
            return True
        return False
    
    def is_valid_move(self, row: int, col: int):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] is None
    
    def check_winner(self):
        
        # Check row
        for i in range(self.size):
            if self.board[i][0] is not None:
                winner = True
                for j in range(1, self.size):
                    if self.board[i][j] != self.board[i][0]:
                        winner = False
                        break
                if winner:
                    return True

        # Check column
        for i in range(self.size):
            if self.board[0][i] is not None:
                winner = True
                for j in range(1, self.size):
                    if self.board[j][i] != self.board[0][i]:
                        winner = False
                        break
                if winner:
                    return True

        # main diagonal
        if self.board[0][0] is not None:
            winner = True
            for i in range(1, self.size):
                if self.board[i][i] != self.board[0][0]:
                    winner = False
                    break
            if winner:
                return True

        # anti-diagonal
        if self.board[0][self.size - 1] is not None:
            winner = True
            for i in range(1, self.size):
                if self.board[i][self.size - 1 - i] != self.board[0][self.size - 1]:
                    winner = False
                    break
            if winner:
                return True
        return False

    
    def display(self):
        for row in self.board:
            for col in row:
                if col is None:
                    print(" ", end=" | ")
                else:
                    print(col.piece_type.name, end=" | ")
                
            print()
            print("-" * (self.size * 4))