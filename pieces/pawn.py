from pieces.contants import PieceType
from pieces.piece import Piece


class Pawn(Piece):
    # Handle valid moves
    def get_valid_moves(self):
        if PieceType.is_black(self._piece_type):
            pass
