from dataclasses import dataclass
from typing import Optional
from pieces.piece import Piece


@dataclass
class MoveHistory:
    move_type: int
    moved_index: int
    target_index: int
    target_piece: Optional[Piece] = None
