from typing import Optional, List, Dict, TYPE_CHECKING, Tuple
from boards.constant import Alliance
from controller.constant import MoveType
from controller.move_history import MoveHistory
from observer.constant import MessageType
from observer.observer import Observer
from pieces.contants import PieceType
from singleton import Singleton

if TYPE_CHECKING:
    from boards.board import Board
    from pieces.piece import Piece


class BoardController(Singleton):  # TODO: Bridge pattern
    _turn: int = Alliance.WHITE
    _running = True
    _selected_piece: Optional["Piece"] = None
    _board: Optional["Board"] = None
    _w_piece_indexes = []
    _b_piece_indexes = []

    def set_board(self, board: "Board"):
        self._board = board
        self._w_piece_indexes, self._b_piece_indexes = self._set_init_board_indexes()
        Observer().send(msg=MessageType.INIT_BOARD)

    def handle_move_event(self, mx: int, my: int) -> Optional[MoveHistory]:
        from utils import Utils
        row, col = Utils.coord_to_position(mx, my)
        target_index = row * 8 + col
        occupied_piece = self._board.get_piece(target_index)
        if self._is_same_alliance(occupied_piece):
            self._handle_select_piece(occupied_piece)
        elif self._has_selected_piece():
            return self._handle_move_piece(target_index, occupied_piece)

    def get_piece_indexes(self, piece_type: int) -> Tuple[List[int], List[int]]:
        if PieceType.is_white(piece_type):
            return self._w_piece_indexes, self._b_piece_indexes
        else:
            return self._b_piece_indexes, self._w_piece_indexes

    def is_running(self) -> bool:
        return self._running

    def force_quit(self):
        self._running = False

    def move_piece(self, moved_coord: int, target_coord: int):
        self._selected_piece = self._board.get_piece(moved_coord)
        self._selected_piece and self._move(target_coord)

    def set_piece(self, piece: Optional["Piece"], index: int):
        self._board.set_piece(piece, index)

    def _get_board_config(self) -> Dict[int, List[int]]:
        return self._board.to_board_config()

    def _change_turn(self):
        self._turn = Alliance.WHITE if Alliance.is_black(self._turn) else Alliance.BLACK

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional["Piece"]):
        self._selected_piece = piece

    def _set_highlight(self, indexes: List[int], highlight: bool = False):
        self._board.set_highlight(indexes, highlight)

    def _is_same_alliance(self, piece: "Piece") -> bool:
        return bool(piece and self._turn == piece.alliance)

    def _move(self, target_index: int):
        selected_index = self._selected_piece.get_square_index()
        self.set_piece(None, selected_index)
        self.set_piece(self._selected_piece, target_index)
        self._set_selected_piece(None)
        self._change_turn()

    def _handle_select_piece(self, piece: "Piece"):
        valid_moves, attack_moves = piece.get_valid_moves()
        self._set_selected_piece(piece)
        square_index = piece.get_square_index()
        self._set_highlight([square_index] + valid_moves, highlight=True)
        Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, selected_indexes=[square_index] + valid_moves)

    def _handle_move_piece(self, target_index: int, occupied_piece: Optional["Piece"]) -> MoveHistory:
        valid_moves, attack_moves = self._selected_piece.get_valid_moves()
        selected_index = self._selected_piece.get_square_index()
        move_type = MoveType.ATTACK if occupied_piece else MoveType.NORMAL
        self._update_indexes(selected_index, target_index, move_type)
        self._move(target_index)
        self._set_highlight([selected_index] + valid_moves, highlight=False)
        Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[selected_index, target_index] + valid_moves)
        return MoveHistory(move_type, selected_index, target_index, occupied_piece)

    def _set_init_board_indexes(self) -> Tuple[List[int], List[int]]:
        w_piece_indexes, b_piece_indexes = [], []
        board_config = self._get_board_config()
        for piece_type, indexes in board_config.items():
            lts = b_piece_indexes if PieceType.is_black(piece_type) else w_piece_indexes
            lts.extend(indexes)
        return w_piece_indexes, b_piece_indexes

    def _update_indexes(self, selected_index, target_index, move_type: int):
        alliance, opponent_indexes = self.get_piece_indexes(self._selected_piece.piece_type)
        alliance.remove(selected_index)
        alliance.append(target_index)
        MoveType.is_attack(move_type) and opponent_indexes.remove(target_index)
