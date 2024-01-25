from typing import Optional, Tuple
from boards.constant import Alliance
from controller.constant import MoveType
from history.move import Move
from game.game_state import GameState
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton
from boards.pieces.piece import Piece
from boards.board import Board


class BoardController(Singleton):  # TODO: Bridge pattern
    _selected_piece: Optional[Piece] = None
    _board: Optional[Board] = None
    _game_state: Optional[GameState] = None

    def set_board(self, board: Board):
        self._board = board
        self._game_state = GameState(turn=Alliance.WHITE, running=True)
        self._game_state.set_player_config()
        Observer().send(msg=MessageType.INIT_BOARD)

    def handle_board_event(self, mx: int, my: int) -> Optional[Move]:
        if self._is_ai_turn():  # Block board event when play with AI
            return
        from utils import Utils
        row, col = Utils.coord_to_position(mx, my)
        target_index = row * 8 + col
        occupied_piece = self._board.get_piece(target_index)
        if self._is_same_alliance(occupied_piece):
            self._handle_select_piece(occupied_piece)
        elif self._has_selected_piece():
            return self._handle_move_selected_piece(target_index, occupied_piece)

    def is_running(self) -> bool:
        return self._game_state.running

    def force_quit(self):
        self._game_state.running = False

    def move_piece(self, moved_coord: int, target_coord: int, first_move=False, undo_piece: Optional["Piece"] = None):
        self._selected_piece = self._board.get_piece(moved_coord)
        self._selected_piece and self._move(target_coord, first_move=first_move)
        if undo_piece:
            self._set_piece(undo_piece, moved_coord)

    def _set_piece(self, piece: Optional["Piece"], index: int):
        self._board.set_piece(piece, index)

    def _change_turn(self):
        self._game_state.turn = Alliance.WHITE if Alliance.is_black(self._game_state.turn) else Alliance.BLACK

    def _is_ai_turn(self) -> bool:
        return self._game_state.ai_player[self._game_state.turn]

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional[Piece]):
        self._selected_piece = piece

    def _is_same_alliance(self, piece: Piece) -> bool:
        return bool(piece and self._game_state.turn == piece.alliance)

    def _move(self, target_index: int, first_move: bool = False) -> Tuple[int, bool]:
        moved_index = self._selected_piece.square_index
        check_first_move = self._selected_piece.first_move
        self._set_piece(None, moved_index)
        self._selected_piece.set_first_move(first_move=first_move)
        self._set_piece(self._selected_piece, target_index)
        self._set_selected_piece(None)
        self._change_turn()
        return moved_index, check_first_move

    def _handle_select_piece(self, piece: Piece):
        self.update_highlight_tiles(highlight=False)
        self._set_selected_piece(piece)
        self.update_highlight_tiles(highlight=True)

    def _handle_move_selected_piece(self, target_index: int, attacked_piece: Optional[Piece]) -> Optional[Move]:
        self.update_highlight_tiles()
        w_ids, b_ids = self._board.get_piece_indexes()
        valid_moves, _ = self._selected_piece.get_valid_moves(w_ids, b_ids)
        if target_index in valid_moves:
            moved_index, first_move = self._move(target_index=target_index)
            Observer().send(msg=MessageType.MOVE_MADE, moved_index=moved_index, target_index=target_index)
            return Move(
                moved_index=moved_index,
                target_index=target_index,
                target_piece=attacked_piece,
                move_type=MoveType.ATTACK if attacked_piece else MoveType.NORMAL,
                first_move=first_move
            )

    def update_highlight_tiles(self, highlight: bool = False):
        Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, piece=self._selected_piece, highlight=highlight)
