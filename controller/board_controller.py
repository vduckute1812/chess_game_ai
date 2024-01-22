from typing import Optional, List, Dict, TYPE_CHECKING, Tuple
from boards.constant import Alliance
from controller.constant import MoveType
from controller.move import Move
from game_state import GameState
from observer.constant import MessageType
from observer.observer import Observer
from pieces.contants import PieceType
from singleton import Singleton

if TYPE_CHECKING:
    from boards.board import Board
    from pieces.piece import Piece


class BoardController(Singleton):  # TODO: Bridge pattern
    _selected_piece: Optional["Piece"] = None
    _board: Optional["Board"] = None
    _game_state = GameState(turn=Alliance.WHITE, running=True)

    def set_board(self, board: "Board"):
        self._board = board
        w_piece_indexes, b_piece_indexes = self._set_init_board_indexes()
        self._game_state.w_piece_indexes = w_piece_indexes
        self._game_state.b_piece_indexes = b_piece_indexes
        self._game_state.board = board
        Observer().send(msg=MessageType.INIT_BOARD)

    def handle_move_event(self, mx: int, my: int):
        from utils import Utils
        row, col = Utils.coord_to_position(mx, my)
        target_index = row * 8 + col
        occupied_piece = self._board.get_piece(target_index)
        if self._is_same_alliance(occupied_piece):
            self._handle_select_piece(occupied_piece)
        elif self._has_selected_piece():
            self._handle_move_selected_piece(target_index, occupied_piece)

    def is_running(self) -> bool:
        return self._game_state.running

    def force_quit(self):
        self._game_state.running = False

    def move_piece(self, moved_coord: int, target_coord: int, move_type: int, first_move=False, is_undo=False):
        self._selected_piece = self._board.get_piece(moved_coord)
        self._selected_piece and self._selected_piece.set_first_move(first_move)
        self._selected_piece and self._move(target_coord, move_type, is_undo)

    def set_piece(self, piece: Optional["Piece"], index: int):
        self._board.set_piece(piece, index)

    def _get_board_config(self) -> Dict[int, List[int]]:
        return self._board.to_board_config()

    def _change_turn(self):
        self._game_state.turn = Alliance.WHITE if Alliance.is_black(self._game_state.turn) else Alliance.BLACK

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional["Piece"]):
        self._selected_piece = piece

    def _set_highlight(self, indexes: List[int], highlight: bool = False):
        self._board.set_highlight(indexes, highlight)

    def _is_same_alliance(self, piece: "Piece") -> bool:
        return bool(piece and self._game_state.turn == piece.alliance)

    def _move(self, target_index: int, move_type: int, is_undo: bool = False):
        selected_index = self._selected_piece.get_square_index()
        self.set_piece(None, selected_index)
        self.set_piece(self._selected_piece, target_index)
        self._update_indexes(selected_index, target_index, move_type, is_undo)
        self._set_selected_piece(None)
        self._change_turn()

    def _handle_select_piece(self, piece: "Piece"):
        self.reset_selected_highlight()
        self._set_selected_piece(piece)
        valid_moves, attack_moves = piece.get_valid_moves()
        square_index = piece.get_square_index()
        self._set_highlight([square_index] + valid_moves, highlight=True)
        Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, selected_indexes=[square_index] + valid_moves)

    def reset_selected_highlight(self):
        if self._selected_piece:
            square_index = self._selected_piece.get_square_index()
            valid_moves, attack_moves = self._selected_piece.get_valid_moves()
            valid_moves.append(square_index)
            self._set_highlight(valid_moves, highlight=False)
            Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, selected_indexes=[square_index] + valid_moves)

    def _handle_move_selected_piece(self, target_index: int, attacked_piece: Optional["Piece"]):
        from controller.move_mgr import MoveManager
        valid_moves, attack_moves = self._selected_piece.get_valid_moves()
        selected_index = self._selected_piece.get_square_index()
        self._set_highlight(valid_moves + [selected_index], highlight=False)
        move_type = MoveType.ATTACK if attacked_piece else MoveType.NORMAL
        if target_index in valid_moves:
            self._selected_piece.set_first_move(first_move=False)
            move = Move(move_type, selected_index, target_index, attacked_piece, self._selected_piece.first_move)
            self._move(target_index, move_type)
            MoveManager().add_move(move)
        Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[selected_index] + valid_moves)

    def _set_init_board_indexes(self) -> Tuple[List[int], List[int]]:
        w_piece_indexes, b_piece_indexes = [], []
        board_config = self._get_board_config()
        for piece_type, indexes in board_config.items():
            lts = b_piece_indexes if PieceType.is_black(piece_type) else w_piece_indexes
            lts.extend(indexes)
        return w_piece_indexes, b_piece_indexes

    def _update_indexes(self, selected_index: int, target_index: int, move_type: int, is_undo: bool = False):
        alliance_indexes, opponent_indexes = self.get_piece_indexes(self._selected_piece.alliance)
        alliance_indexes.remove(selected_index)
        alliance_indexes.append(target_index)
        if MoveType.is_attack(move_type):
            opponent_indexes.append(selected_index) if is_undo else opponent_indexes.remove(target_index)

    def get_piece_indexes(self, alliance: int) -> Tuple[List[int], List[int]]:
        return self._game_state.get_piece_indexes(alliance)
