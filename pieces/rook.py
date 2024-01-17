from pieces.contants import PieceType
from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, alliance: int):
        super().__init__(alliance, PieceType.ROOK)

