import pygame

from boards.pieces.piece import Piece


class King(Piece):
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [8, 1, -8, -1, 7, 9, -7, -9]
        self._one_step = True
