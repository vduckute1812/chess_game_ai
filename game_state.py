from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING, Tuple, List
from boards.constant import Alliance

if TYPE_CHECKING:
    from pieces.piece import Board


@dataclass
class GameState:
    turn: int = Alliance.UNKNOWN
    running: bool = False
    w_piece_indexes = []
    b_piece_indexes = []
    board: Optional["Board"] = None

    def get_piece_indexes(self, alliance: int) -> Tuple[List[int], List[int]]:
        indexes = self.w_piece_indexes, self.b_piece_indexes
        return indexes if Alliance.is_white(alliance) else indexes[::-1]