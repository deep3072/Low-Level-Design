from piece_type import PieceType

class PlayingPiece:
    def __init__(self, piece_type: PieceType):
        self.piece_type = piece_type


class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)