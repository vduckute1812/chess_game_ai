from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from boards.pieces.piece import Piece


@dataclass
class Move:
    move_type: int
    moved_index: int
    target_index: int
    target_piece: Optional["Piece"] = None
    first_move: bool = False
