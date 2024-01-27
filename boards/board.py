from typing import Optional, List, Dict, Tuple

import pygame

from boards.constant import WINDOW_SIZE, Alliance
from boards.square import Square
from controller.constant import MoveType
from history.move import Move
from observer.constant import MessageType
from observer.observer import Listener, Observer
from boards.pieces.contants import PieceType, BOARD_CONFIG
from boards.pieces.piece import Piece
from utils import Utils


class Board(Listener):
    def __init__(self):
        super().__init__()
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        self._board_config = BOARD_CONFIG
        self._squares = Utils.set_init_board(BOARD_CONFIG)
        Observer().listen_to(self)

    def _get_square(self, index: int) -> Square:
        return self._squares[index]

    def get_piece(self, index: int) -> Optional[Piece]:
        square = self._get_square(index)
        return square.get_piece() if square else None

    def get_board_config(self) -> Dict:
        return self._board_config

    def set_piece(self, piece: Piece, index: int):
        piece and piece.set_square_index(index)
        self._get_square(index).set_piece(piece)

    def get_piece_indexes(self, piece: Piece) -> Tuple[List[int], List[int]]:
        piece_indexes = [], []
        for piece_type, indexes in self._board_config.items():
            lts = piece_indexes[0] if PieceType.is_white(piece_type) else piece_indexes[1]
            lts.extend(indexes)
        alliance_ids, opponent_ids = piece_indexes if PieceType.is_white(piece.piece_type) else piece_indexes[::-1]
        return alliance_ids, opponent_ids

    def set_highlight(self, selected_indexes: List[int], highlight: bool = True):
        for index in selected_indexes:
            self._get_square(index).set_highlight(highlight)

    def on_message_received(
            self, msg: int, selected_squares: Optional[List[int]] = None, **kwargs
    ):
        match msg:
            case MessageType.INIT_BOARD | MessageType.BOARD_CHANGED:
                self.draw()
            case MessageType.SQUARE_HIGHLIGHT:
                self.update_highlight_tiles(**kwargs)
            case MessageType.MOVE_MADE:
                self.update_moved_piece_tiles(**kwargs)
                self.update_board_config(**kwargs)

    def draw(self):
        self._screen.fill('white')
        for square in self._squares:
            square.draw(self._screen)
        pygame.display.update()

    def update_squares(self, **kwargs):
        selected_squares = kwargs.get("selected_squares", [])
        for index in selected_squares:
            self._get_square(index).draw(self._screen)
        pygame.display.update()

    def update_highlight_tiles(self, **kwargs):
        piece = kwargs.get("piece")
        if piece and not kwargs.get("is_ai"):
            alliance_ids, opponent_ids = self.get_piece_indexes(piece=piece)
            normal_moves, attack_moves = piece.get_valid_moves(alliance_ids, opponent_ids)
            update_moves = normal_moves + attack_moves + [piece.square_index]
            self.set_highlight(update_moves, highlight=kwargs.get("highlight", False))
            self.update_squares(selected_squares=update_moves)

    def update_moved_piece_tiles(self, **kwargs):
        allow_render = not kwargs.get("is_ai", False)
        moved_index = kwargs.get("moved_index")
        target_index = kwargs.get("target_index")
        allow_render and self.update_squares(selected_squares=[moved_index, target_index])

    def update_board_config(self, **kwargs):
        moved_index = kwargs.get("moved_index")
        target_index = kwargs.get("target_index")
        is_undo = kwargs.get("is_undo", False)
        if piece_type := kwargs.get("moved_piece_type"):
            indexes = self._board_config.get(piece_type, [])
            indexes.remove(moved_index)
            isinstance(target_index, int) and indexes.append(target_index)
        if attacked_piece := kwargs.get("attacked_piece"):
            indexes = self._board_config.get(attacked_piece.piece_type, [])
            indexes.append(moved_index) if is_undo else indexes.remove(target_index)

    def generate_valid_moves(self, alliance: int) -> List[Move]:
        valid_moves = []
        for piece_type, indexes in self._board_config.items():
            if Alliance.is_opposite(alliance, PieceType.get_alliance(piece_type)):
                continue
            for index in indexes:
                if piece := self.get_piece(index):
                    normal_moves, attack_moves = piece.get_valid_moves(*self.get_piece_indexes(piece=piece))
                    valid_moves.extend(self._generate_moves(piece, normal_moves, attack_moves))
        return valid_moves

    def _generate_moves(self, piece: Piece, normal_moves: List[int], attack_moves: List[int]) -> List[Move]:
        valid_moves = []
        for move_idx in normal_moves + attack_moves:
            attacked_piece = move_idx in attack_moves and self.get_piece(move_idx) or None
            valid_moves.append(
                Move(
                    move_type=MoveType.ATTACK if move_idx in attack_moves else MoveType.NORMAL,
                    moved_index=piece.square_index,
                    target_index=move_idx,
                    moved_piece_type=piece.piece_type,
                    attacked_piece=attacked_piece
                )
            )
        return valid_moves
