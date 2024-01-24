import pygame

from boards.pieces.piece import Piece


class Queen(Piece):
    # Handle valid moves
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [-1, -8, 9, 7, -7, -9, 8, 1]
