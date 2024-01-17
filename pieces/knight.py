from pieces.contants import Alliance, PieceType
from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, alliance: int):
        super().__init__(alliance, PieceType.KNIGHT)
