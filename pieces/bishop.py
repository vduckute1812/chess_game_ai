from typing import List, Tuple
import pygame
from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [9, 7, -7, -9]
