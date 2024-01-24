from typing import Tuple, List

import pygame

from boards.pieces.contants import PieceType
from boards.pieces.piece import Piece


class Pawn(Piece):
    SECOND_STEP_MOVE = 16

    # Handle valid moves

    def __init__(self, square_index: int, piece_type: int, img: pygame.Surface):
        super().__init__(square_index, piece_type, img)
        self._attack_directions = [7, 9]
        self._legal_directions = [8]
        self._one_step = True

    def get_valid_moves(self) -> Tuple[List[int], List[int]]:
        pawn_direction = 1 if PieceType.is_black(self._piece_type) else -1
        alliance_indexes, opponent_indexes = self._get_piece_indexes()
        all_indexes = alliance_indexes + opponent_indexes
        self.update_legal_directions()
        normal_moves = self.get_legal_moves(pawn_direction, all_indexes)
        attack_moves = self.get_attack_moves(pawn_direction, opponent_indexes)
        return normal_moves + attack_moves, attack_moves

    def update_legal_directions(self):
        if self._first_move and self.SECOND_STEP_MOVE not in self._legal_directions:
            self._legal_directions.append(self.SECOND_STEP_MOVE)
        elif not self._first_move and self.SECOND_STEP_MOVE in self._legal_directions:
            self._legal_directions.remove(self.SECOND_STEP_MOVE)

    def get_legal_moves(self, pawn_direction: int, all_indexes: List[int]) -> List[int]:
        normal_moves = []
        for direction in self._legal_directions:
            direction *= pawn_direction
            cur_pos = self._square_index
            if self._is_valid_index(cur_pos, cur_pos + direction):
                cur_pos += direction
                if cur_pos in all_indexes:
                    break
                else:
                    normal_moves.append(cur_pos)
        return normal_moves

    def get_attack_moves(self, pawn_direction: int, opponent_indexes: List[int]) -> List[int]:
        attack_moves = []
        for direction in self._attack_directions:
            direction *= pawn_direction
            cur_pos = self._square_index
            if self._is_valid_index(cur_pos, cur_pos + direction):
                cur_pos += direction
                cur_pos in opponent_indexes and attack_moves.append(cur_pos)
        return attack_moves
