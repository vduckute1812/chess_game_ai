from typing import Tuple, Optional, TYPE_CHECKING

import pygame

from boards.constant import SQUARE_COLOR_MAP, HIGH_LIGHT_SQUARE_COLOR_MAP, Color, ATTACK_SQUARE_COLOR_MAP

if TYPE_CHECKING:
    from pieces.piece import Piece


class Square:
    def __init__(self, index: int, width: int, height: int):
        self._index = index
        self._width = width
        self._height = height
        self._highlight = False
        self._occupying_piece = None

    def set_highlight(self, highlight: bool):
        self._highlight = highlight

    def set_piece(self, piece: Optional["Piece"]):
        self._occupying_piece = piece

    def get_piece(self) -> Optional["Piece"]:
        return self._occupying_piece

    @property
    def color(self) -> int:
        return Color.BLACK if self._is_dark() else Color.WHITE

    @property
    def index(self) -> int:
        return self._index

    def _rendered_color(self) -> Tuple[int, int, int]:
        if self._highlight and self._occupying_piece:
            return self._attack_color()
        elif self._highlight:
            return self._highlight_color()
        else:
            return self._draw_color()

    def _is_dark(self) -> bool:
        return bool((self._index // 8 + self._index % 8) % 2)

    def _draw_color(self) -> Tuple[int, int, int]:
        return SQUARE_COLOR_MAP[self.color]

    def _highlight_color(self) -> Tuple[int, int, int]:
        return HIGH_LIGHT_SQUARE_COLOR_MAP[self.color]

    def _attack_color(self) -> Tuple[int, int, int]:
        return ATTACK_SQUARE_COLOR_MAP[self.color]

    def draw(self, display):
        row, col = self._index // 8, self._index % 8
        abs_x = col * self._width
        abs_y = row * self._height
        rect = pygame.Rect(abs_x, abs_y, self._width, self._height)
        pygame.draw.rect(display, self._rendered_color(), rect)
        self._occupying_piece and self._occupying_piece.draw(display, rect)
