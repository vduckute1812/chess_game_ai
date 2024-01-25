from typing import Optional, List, Dict, Tuple

import pygame

from boards.constant import WINDOW_SIZE, Alliance
from boards.square import Square
from observer.constant import MessageType
from observer.observer import Listener, Observer
from boards.pieces.contants import PieceType
from boards.pieces.piece import Piece
from utils import Utils


class Board(Listener):
    def __init__(self):
        super().__init__()
        self._squares = Utils.set_init_board()
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        Observer().listen_to(self)

    def _get_square(self, index: int) -> Square:
        return self._squares[index]

    def get_piece(self, index: int) -> Optional[Piece]:
        square = self._get_square(index)
        return square.get_piece() if square else None

    def set_piece(self, piece: Piece, index: int):
        piece and piece.set_square_index(index)
        self._get_square(index).set_piece(piece)

    def to_board_config(self) -> Dict[int, List[int]]:
        config = {}
        for square in self._squares:
            piece = square.get_piece()
            piece and config.setdefault(piece.piece_type, []).append(square.index)
        return config

    def get_piece_indexes(self) -> Tuple[List[int], List[int]]:
        w_piece_indexes, b_piece_indexes = [], []
        for piece_type, indexes in self.to_board_config().items():
            lts = b_piece_indexes if PieceType.is_black(piece_type) else w_piece_indexes
            lts.extend(indexes)

        return w_piece_indexes, b_piece_indexes

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
        if piece := kwargs.get("piece"):
            indexes = self.get_piece_indexes()
            alliance_ids, opponent_ids = indexes if Alliance.is_white(alliance=piece.alliance) else indexes[::-1]
            update_moves, _ = piece.get_valid_moves(alliance_ids, opponent_ids)
            update_moves.append(piece.square_index)
            self.set_highlight(update_moves, highlight=kwargs.get("highlight", False))
            self.update_squares(selected_squares=update_moves)

    def update_moved_piece_tiles(self, **kwargs):
        moved_index = kwargs.get("moved_index")
        target_index = kwargs.get("target_index") or 0
        self.update_squares(selected_squares=[moved_index, target_index])
