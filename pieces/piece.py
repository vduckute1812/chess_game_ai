from typing import Tuple

from pieces.contants import PieceType


class Piece:
    def __init__(self, alliance: int, piece_type: int = PieceType.UNKNOWN, square_index: int = -1):
        from utils import Utils
        self._alliance = alliance
        self._piece_type = piece_type
        self._square_index = square_index
        self._img = Utils.generate_piece_img(self._piece_type, self._alliance)

    @property
    def alliance(self) -> int:
        return self._alliance

    def set_square_index(self, index: int):
        self._square_index = index

    def to_position(self) -> Tuple[int, int]:
        return self._square_index // 8, self._square_index % 8

    def draw(self, display, rect):
        centering_rect = self._img.get_rect()
        centering_rect.center = rect.center
        display.blit(self._img, centering_rect.topleft)
