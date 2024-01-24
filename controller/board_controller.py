from typing import Optional, List, TYPE_CHECKING, Tuple
from boards.constant import Alliance
from controller.board_tile_render import BoardTileRender
from controller.constant import MoveType
from controller.move import Move
from game.game_state import GameState
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton

if TYPE_CHECKING:
    from boards.board import Board
    from boards.pieces.piece import Piece


class BoardController(Singleton):  # TODO: Bridge pattern
    _selected_piece: Optional["Piece"] = None
    _board: Optional["Board"] = None
    _game_state: Optional[GameState] = None

    def set_board(self, board: "Board"):
        self._board = board
        self._game_state = GameState(turn=Alliance.WHITE, running=True)
        self._game_state.set_player_config()
        Observer().listen_to(board)
        Observer().send(msg=MessageType.INIT_BOARD)

    def handle_board_event(self, mx: int, my: int):
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

    def _change_turn(self):
        self._game_state.turn = Alliance.WHITE if Alliance.is_black(self._game_state.turn) else Alliance.BLACK

    def _is_ai_turn(self) -> bool:
        return self._game_state.ai_player[self._game_state.turn]

    def _has_selected_piece(self):
        return bool(self._selected_piece)

    def _set_selected_piece(self, piece: Optional["Piece"]):
        self._selected_piece = piece

    def _is_same_alliance(self, piece: "Piece") -> bool:
        return bool(piece and self._game_state.turn == piece.alliance)

    def _move(self, target_index: int, move_type: int, is_undo: bool = False):
        selected_index = self._selected_piece.get_square_index()
        self.set_piece(None, selected_index)
        self.set_piece(self._selected_piece, target_index)
        self._set_selected_piece(None)
        self._change_turn()

    def _handle_select_piece(self, piece: "Piece"):
        self.reset_selected_piece_tiles()
        self._set_selected_piece(piece)
        self.render_selected_piece_tiles()

    def _handle_move_selected_piece(self, target_index: int, attacked_piece: Optional["Piece"]):
        from controller.move_mgr import MoveManager
        valid_moves = self.reset_selected_piece_tiles()
        selected_index = self._selected_piece.get_square_index()
        if target_index in valid_moves:
            move_type = MoveType.ATTACK if attacked_piece else MoveType.NORMAL
            self._selected_piece.set_first_move(first_move=False)
            move = Move(move_type, selected_index, target_index, attacked_piece, self._selected_piece.first_move)
            self._move(target_index, move_type)
            MoveManager().add_move(move)
        BoardTileRender.update_piece_tiles(selected_index, target_index)

    def get_piece_indexes(self, alliance: int) -> Tuple[List[int], List[int]]:
        indexes = self._board.get_piece_indexes()
        return indexes if Alliance.is_white(alliance) else indexes[::-1]

    def reset_selected_piece_tiles(self) -> List[int]:
        return BoardTileRender.reset_selected_piece_tiles(self._selected_piece, self._board)

    def render_selected_piece_tiles(self):
        BoardTileRender.render_selected_piece_tiles(self._selected_piece, self._board)
