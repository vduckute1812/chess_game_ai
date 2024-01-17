from typing import Tuple, Optional, TYPE_CHECKING

import pygame

from boards.constant import BOARD_COLUMNS, SQUARE_COLOR_MAP, HIGH_LIGHT_SQUARE_COLOR_MAP, Color
if TYPE_CHECKING:
    from pieces.piece import Piece


class Square:
    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
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

    def is_occupied(self) -> bool:
        return bool(self._occupying_piece)

    @property
    def color(self) -> int:
        return Color.BLACK if self._is_dark() else Color.WHITE

    @property
    def coordinate_str(self) -> str:
        return f"{BOARD_COLUMNS[self._x]}{self._y + 1}"

    @property
    def position(self) -> Tuple[int, int]:
        return self._x, self._y

    def get_size(self) -> Tuple[int, int]:
        return self._width, self._height

    def _rendered_color(self) -> Tuple[int, int, int]:
        return self._highlight_color() if self._highlight else self._draw_color()

    def _is_dark(self) -> bool:
        return bool((self._x + self._y) % 2)

    def _draw_color(self) -> Tuple[int, int, int]:
        return SQUARE_COLOR_MAP[self.color]

    def _highlight_color(self) -> Tuple[int, int, int]:
        return HIGH_LIGHT_SQUARE_COLOR_MAP[self.color]

    def draw(self, display):
        abs_x = self._x * self._width
        abs_y = self._y * self._height
        rect = pygame.Rect(abs_x, abs_y, self._width, self._height)
        # Render tile
        pygame.draw.rect(display, self._rendered_color(), rect)
        # Render piece
        self._occupying_piece and self._occupying_piece.draw(display, rect)
