from typing import List, Tuple
import pygame
from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._directions = [9, 7, -7, -9]

    # Handle valid moves
    def get_valid_moves(self) -> Tuple[List[int], List[int]]:
        valid_moves, attack_moves = [], []
        alliance_indexes, opponent_indexes = self._get_piece_indexes()

        all_indexes = alliance_indexes + opponent_indexes
        for direction in self._directions:
            # in_border = self._in_border(self._square_index)
            cur_pos = self._square_index + direction
            while self._is_valid_index(cur_pos):
                if cur_pos in all_indexes:
                    cur_pos in opponent_indexes and attack_moves.append(cur_pos)
                    break
                else:
                    valid_moves.append(cur_pos)
                cur_pos += direction
                in_border = self._in_border(cur_pos)
        return valid_moves + attack_moves, attack_moves

    def _get_valid_moves_in_direction(self, direction: int) -> List[int]:
        pass
