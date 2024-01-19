from typing import Optional
from boards.board import Board
from boards.constant import Alliance
from controller.constant import MoveType
from controller.move import Move
from pieces.piece import Piece
from singleton import Singleton
from utils import Utils


class BoardController(Singleton):  # TODO: Bridge pattern
    _turn: int = Alliance.WHITE
    _running = True
    _selected_piece: Optional[Piece] = None
    _board: Board = Board()

    def get_board(self) -> Board:
        return self._board

    def set_piece(self, piece: Optional[Piece], index: int):
        self._board.set_piece(piece, index)

    def handle_move_event(self, mx: int, my: int) -> Optional[Move]:
        move = None
        row, col = Utils.coord_to_position(mx, my)
        index = row * 8 + col
        occupied_piece = self._board.get_piece(index)
        if occupied_piece and self._is_same_alliance(occupied_piece):
            self._set_selected_piece(occupied_piece)
        elif self._has_selected_piece() and not occupied_piece:
            move = self._move(index)
        return move

    def is_running(self) -> bool:
        return self._running

    def force_quit(self):
        self._running = False

    def move_piece(self, moved_coord: int, target_coord: int):
        self._selected_piece = self._board.get_piece(moved_coord)
        if self._selected_piece:
            self._move(target_coord)

    def _change_turn(self):
        self._turn = Alliance.WHITE if Alliance.is_black(self._turn) else Alliance.BLACK

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional[Piece]):
        self._selected_piece = piece

    def _is_same_alliance(self, piece: Piece) -> bool:
        return bool(piece and self._turn == piece.alliance)

    def _move(self, moved_index: int) -> Move:
        selected_index = self._selected_piece.get_square_index()
        self.set_piece(None, selected_index)
        self.set_piece(self._selected_piece, moved_index)
        self._set_selected_piece(None)
        self._change_turn()
        return Move(MoveType.NORMAL, selected_index, moved_index)
