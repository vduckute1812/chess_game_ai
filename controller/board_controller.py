from typing import Optional
from boards.board import Board
from boards.constant import Alliance
from controller.constant import MoveType
from controller.move_history import MoveHistory
from observer.constant import MessageType
from observer.observer import Observer
from pieces.piece import Piece
from singleton import Singleton
from utils import Utils


class BoardController(Singleton):  # TODO: Bridge pattern
    _turn: int = Alliance.WHITE
    _running = True
    _selected_piece: Optional[Piece] = None
    _board: Optional[Board] = None

    def set_board(self, board):
        self._board = board
        Observer().send(msg=MessageType.INIT_BOARD)

    def set_piece(self, piece: Optional[Piece], index: int):
        self._board.set_piece(piece, index)

    def handle_move_event(self, mx: int, my: int) -> Optional[MoveHistory]:
        move = None
        row, col = Utils.coord_to_position(mx, my)
        target_index = row * 8 + col
        occupied_piece = self._board.get_piece(target_index)
        if self._is_same_alliance(occupied_piece):
            self._set_selected_piece(occupied_piece)
        elif self._has_selected_piece() and occupied_piece:
            move = self._handle_attack(target_index, occupied_piece)
        elif self._has_selected_piece():
            move = self._handle_move(target_index)
        return move

    def is_running(self) -> bool:
        return self._running

    def force_quit(self):
        self._running = False

    def move_piece(self, moved_coord: int, target_coord: int):
        self._selected_piece = self._board.get_piece(moved_coord)
        self._selected_piece and self._move(target_coord)

    def _change_turn(self):
        self._turn = Alliance.WHITE if Alliance.is_black(self._turn) else Alliance.BLACK

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional[Piece]):
        self._selected_piece = piece

    def _is_same_alliance(self, piece: Piece) -> bool:
        return bool(piece and self._turn == piece.alliance)

    def _move(self, target_index: int):
        selected_index = self._selected_piece.get_square_index()
        self.set_piece(None, selected_index)
        self.set_piece(self._selected_piece, target_index)
        self._set_selected_piece(None)
        self._change_turn()
        Observer().send(msg=MessageType.BOARD_CHANGED)

    def _handle_move(self, target_index: int):
        selected_index = self._selected_piece.get_square_index()
        self._move(target_index)
        return MoveHistory(MoveType.NORMAL, selected_index, target_index)

    def _handle_attack(self, target_index: int, attacked_piece: Piece):
        selected_index = self._selected_piece.get_square_index()
        self._move(target_index)
        return MoveHistory(MoveType.ATTACK, selected_index, target_index, attacked_piece)
