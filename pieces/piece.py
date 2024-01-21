from typing import Tuple, List
import pygame
from controller.board_controller import BoardController
from pieces.contants import PieceType


class Piece:
    def __init__(self, square_index: int = -1, piece_type: int = PieceType.UNKNOWN, img: pygame.Surface = None):
        self._piece_type = piece_type
        self._square_index = square_index
        self._img = img
        self._directions = []
        self._one_step = False
        self._first_move = True

    def set_square_index(self, index: int):
        self._square_index = index

    def set_first_move(self, first_move: bool):
        self._first_move = first_move

    def get_square_index(self) -> int:
        return self._square_index

    def draw(self, display, rect):
        centering_rect = self._img.get_rect()
        centering_rect.center = rect.center
        display.blit(self._img, centering_rect.topleft)

    @property
    def alliance(self) -> int:
        return PieceType.get_alliance(self._piece_type)

    @property
    def piece_type(self) -> int:
        return self._piece_type

    def _get_piece_indexes(self) -> Tuple[List[int], List[int]]:
        return BoardController().get_piece_indexes(self._piece_type)

    @staticmethod
    def _is_valid_index(current_index, target_index) -> bool:
        step_row = abs(target_index // 8 - current_index // 8)
        step_col = abs(target_index % 8 - current_index % 8)
        return 0 < target_index < 64 and step_row <= 2 and step_col <= 2

    def get_valid_moves(self) -> Tuple[List[int], List[int]]:
        normal_moves, attack_moves = [], []
        alliance_indexes, opponent_indexes = self._get_piece_indexes()

        all_indexes = alliance_indexes + opponent_indexes
        for direction in self._directions:
            cur_pos = self._square_index
            while self._is_valid_index(cur_pos, cur_pos + direction):
                cur_pos += direction
                if cur_pos in all_indexes:
                    cur_pos in opponent_indexes and attack_moves.append(cur_pos)
                    break
                normal_moves.append(cur_pos)
                if self._one_step:
                    break
        return normal_moves + attack_moves, attack_moves
