from dataclasses import dataclass
from typing import Optional
from boards.pieces.piece import Piece


@dataclass
class Move:
    move_type: int
    moved_index: int
    target_index: int
    moved_piece_type: int
    attacked_piece: Optional[Piece] = None
    first_move: bool = False

    def to_dict(self):
        return dict(
            first_move=self.first_move,
            move_type=self.move_type,
            moved_piece_type=self.moved_piece_type,
            moved_index=self.moved_index,
            target_index=self.target_index,
            attacked_piece=self.attacked_piece,
        )
