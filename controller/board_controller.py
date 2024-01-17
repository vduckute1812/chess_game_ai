from typing import Optional, List, Tuple

from boards.board import Board
from boards.square import Square
from pieces.contants import Alliance
from pieces.piece import Piece
from singleton import Singleton
from utils import Utils


class BoardController(Singleton):  # TODO: Bridge pattern
    def __init__(self):
        self._turn: int = Alliance.WHITE
        self._running = True
        self._selected_piece: Optional[Piece] = None

    def set_board(self, board):
        self._board_tiles: List[List[Square]] = board.get_board_tiles()

    def get_square(self, piece: Piece) -> Square:
        row, col = piece.to_position()
        return self._board_tiles[row][col]

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        square = self._board_tiles[row][col]
        return square.get_piece() if square else None

    def change_turn(self):
        if Alliance.is_black(self._turn):
            self._turn = Alliance.WHITE
        else:
            self._turn = Alliance.BLACK

    def set_piece(self, piece: Piece, row: int, col: int):
        piece.set_square_index(row * 8 + col)
        self._board_tiles[row][col].set_piece(piece)

    def has_selected_piece(self):
        return bool(self._selected_piece)

    def set_selected_piece(self, piece: Optional[Piece]):
        self._selected_piece = piece

    def is_same_alliance(self, piece: Piece) -> bool:
        return bool(piece and self._turn == piece.alliance)

    def move(self, row: int, col: int):
        if self.has_selected_piece():
            self.get_square(self._selected_piece).set_piece(None)
            self.set_piece(self._selected_piece, row, col)
            self.change_turn()
            self.set_selected_piece(None)

    def handle_click(self, mx: int, my: int):
        row, col = Utils.coord_to_position(mx, my)
        occupied_piece = self.get_piece(row, col)
        if occupied_piece and self.is_same_alliance(occupied_piece):
            self.set_selected_piece(occupied_piece)
        elif self.has_selected_piece() and not occupied_piece:
            self.move(row, col)

    def is_running(self) -> bool:
        return self._running

    def force_quit(self):
        self._running = False

    def move_piece(self, moved_coord: int, target_coord: int):
        pass
