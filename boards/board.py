from typing import Optional

import pygame

from boards.constant import WINDOW_SIZE
from boards.square import Square
from observer.constant import MessageType
from observer.listener import Listener
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

    def on_message_received(self, msg: int):
        if MessageType.is_init_board(msg) or MessageType.is_board_change(msg):
            self.draw()

    def draw(self):
        self._screen.fill('white')
        for square in self._squares:
            square.draw(self._screen)
        pygame.display.update()
