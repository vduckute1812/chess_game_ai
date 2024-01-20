from typing import Tuple

import pygame

from pieces.contants import PieceType


class Piece:
    def __init__(self, square_index: int = -1, piece_type: int = PieceType.UNKNOWN, img: pygame.Surface = None):
        self._piece_type = piece_type
        self._square_index = square_index
        self._img = img
        self._first_move = True

    def set_square_index(self, index: int):
        self._square_index = index

    def get_square_index(self) -> int:
        return self._square_index

    def draw(self, display, rect):
        centering_rect = self._img.get_rect()
        centering_rect.center = rect.center
        display.blit(self._img, centering_rect.topleft)

    @property
    def alliance(self) -> int:
        return PieceType.get_alliance(self._piece_type)
