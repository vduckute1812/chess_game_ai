from typing import Optional, List

import pygame

from boards.square import Square
from pieces.piece import Piece
from utils import Utils


class Board:
    def __init__(self):
        self._squares = Utils.set_init_board()

    def _get_square(self, index: int) -> Square:
        return self._squares[index]

    def get_piece(self, index: int) -> Optional[Piece]:
        square = self._get_square(index)
        return square.get_piece() if square else None

    def set_piece(self, piece: Piece, index: int):
        if piece:
            piece.set_square_index(index)
        self._get_square(index).set_piece(piece)

    def draw(self, display: pygame.Surface):
        display.fill('white')
        for square in self._squares:
            square.draw(display)
        pygame.display.update()
