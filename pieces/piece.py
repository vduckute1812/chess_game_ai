from typing import Tuple, List

import pygame

from controller.board_controller import BoardController
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

    def get_valid_moves(self) -> Tuple[List[int], List[int]]:
        return [], []   # Normal moves, Attack moves

    @property
    def alliance(self) -> int:
        return PieceType.get_alliance(self._piece_type)

    @property
    def piece_type(self) -> int:
        return self._piece_type

    def _get_piece_indexes(self) -> Tuple[List[int], List[int]]:
        return BoardController().get_piece_indexes(self._piece_type)

    @staticmethod
    def _in_border(square_index):
        return square_index // 8 in [0, 7] or square_index % 8 in [0, 7]

    @staticmethod
    def _is_valid_index(square_index) -> bool:
        return 0 < square_index < 64


