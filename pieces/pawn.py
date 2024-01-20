import pygame
from pieces.piece import Piece


class Pawn(Piece):
    # Handle valid moves
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [8, 7, 9]

    def get_valid_moves(self):
        return [], []
