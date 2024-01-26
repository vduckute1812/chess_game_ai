from multiprocessing import Queue, Process
from typing import Optional, Tuple, List, Dict
from boards.constant import Alliance
from controller.constant import MoveType
from history.move import Move
from game.game_state import GameState
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton
from boards.pieces.piece import Piece
from boards.board import Board
from utils import Utils


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
        row, col = Utils.coord_to_position(mx, my)
        target_index = row * 8 + col
        occupied_piece = self._board.get_piece(target_index)
        if self._is_same_alliance(occupied_piece):
            self._handle_select_piece(occupied_piece)
        elif self._has_selected_piece():
            self.update_highlight_tiles(highlight=False)
            return self._handle_move_selected_piece(target_index, occupied_piece)

    def is_running(self) -> bool:
        return self._game_state.running

    def force_quit(self):
        self._game_state.running = False

    def make_move(self, moved_coord: int, target_coord: int, first_move=False, attacked_piece: Optional[Piece] = None):
        self._selected_piece = self._board.get_piece(moved_coord)
        self._selected_piece and self._move(target_coord, first_move=first_move)
        attacked_piece and self._set_piece(attacked_piece, moved_coord)

    def _set_piece(self, piece: Optional[Piece], index: int):
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

    def _move(self, target_index: int, first_move: bool = False) -> Tuple[int, int, bool]:
        piece_type, square_index, _first_move = (
            self._selected_piece.piece_type, self._selected_piece.square_index, self._selected_piece.first_move
        )
        self._set_piece(None, self._selected_piece.square_index)
        self._selected_piece.set_first_move(first_move=first_move)
        self._set_piece(self._selected_piece, target_index)
        self._set_selected_piece(None)
        self._change_turn()
        return piece_type, square_index, _first_move

    def _handle_select_piece(self, piece: Piece):
        self.update_highlight_tiles(highlight=False)
        self._set_selected_piece(piece)
        self.update_highlight_tiles(highlight=True)

    def _handle_move_selected_piece(self, target_index: int, attacked_piece: Optional[Piece]) -> Optional[Move]:
        valid_moves, attacked_moves = self.get_valid_moves(self._selected_piece)
        updating_moves = valid_moves + attacked_moves
        if target_index in updating_moves:
            moved_piece_type, moved_index, first_move = self._move(target_index=target_index)
            move_data = dict(
                first_move=first_move,
                move_type=MoveType.ATTACK if attacked_piece else MoveType.NORMAL,
                moved_piece_type=moved_piece_type,
                moved_index=moved_index,
                target_index=target_index,
                attacked_piece=attacked_piece,
            )
            Observer().send(msg=MessageType.MOVE_MADE, **move_data)
            return Move(**move_data)

    def _handle_ai_turn(self):
        from history.move_handler import MoveHandler
        from history.move_mgr import MoveManager

        # return_queue = Queue()  # used to pass data between threads
        # move_finder_process = Process(target=Minimax.negamax_alpha_beta())
        # move_finder_process.start()
        moves = self.generate_valid_moves(self._game_state.turn)
        move = moves[0]
        MoveHandler().redo(moves[0])
        MoveManager().add_move(move)

    def update_highlight_tiles(self, highlight: bool = False):
        if not self._is_ai_turn():
            Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, piece=self._selected_piece, highlight=highlight)

    def get_valid_moves(self, piece: Piece) -> Tuple[List[int], List[int]]:
        w_ids, b_ids = self._board.get_piece_indexes(piece)
        return piece.get_valid_moves(w_ids, b_ids)

    def generate_valid_moves(self, alliance: int):
        return self._board.generate_valid_moves(alliance)
