from pieces.contants import PieceType
from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, alliance: int):
        super().__init__(alliance, PieceType.PAWN)
        self.has_moved = False
