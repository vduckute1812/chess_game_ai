from pieces.contants import Alliance, PieceType
from pieces.piece import Piece


class Queen(Piece):
    def __init__(self, alliance: int):
        super().__init__(alliance, PieceType.QUEEN)

