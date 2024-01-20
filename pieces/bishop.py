from typing import List

import pygame

from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [9, 7, -7, -9]

    # Handle valid moves
    def get_valid_moves(self) -> list:
        valid_moves = []
        for direction in self._directions:
            pass
            # valid_moves += self._get_valid_moves_in_direction(board, direction)
        return valid_moves

    def _get_valid_moves_in_direction(self, direction: int) -> List[int]:
        pass
