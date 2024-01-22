from typing import Optional, List, Dict

import pygame

from boards.constant import WINDOW_SIZE
from boards.square import Square
from observer.constant import MessageType
from observer.observer import Listener
from observer.observer import Observer
from pieces.piece import Piece
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

    def set_highlight(self, selected_indexes: List[int], highlight: bool = True):
        for index in selected_indexes:
            self._get_square(index).set_highlight(highlight)

    def on_message_received(
        self, msg: int, selected_squares: Optional[List[int]] = None, **kwargs
    ):
        selected_squares = selected_squares or []
        match msg:
            case MessageType.INIT_BOARD | MessageType.BOARD_CHANGED:
                self.draw()
            case MessageType.SQUARE_HIGHLIGHT | MessageType.MOVE_MADE:
                self.update_squares(selected_squares)

    def draw(self):
        self._screen.fill('white')
        for square in self._squares:
            square.draw(self._screen)
        pygame.display.update()

    def update_squares(self, square_indexes: List[int]):
        for index in square_indexes:
            self._get_square(index).draw(self._screen)
        pygame.display.update()

    def to_square_piece_index_map(self) -> Dict[int, int]:
        config = {}
        for square in self._squares:
            piece = square.get_piece()
            if piece:
                config[square.index] = piece.piece_type
        return config
