from typing import Tuple
import pygame
from boards.constant import WINDOW_SIZE


class Piece:
    def __init__(self, alliance: int):
        self._tile_width, self._tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        self._alliance = alliance
        self._img = None

    @property
    def alliance(self) -> int:
        return self._alliance

    def draw(self, display, rect):
        centering_rect = self._img.get_rect()
        centering_rect.center = rect.center
        display.blit(self._img, centering_rect.topleft)
