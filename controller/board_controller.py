from typing import Optional, List, Tuple

from boards.board import Board
from boards.square import Square
from pieces.contants import Alliance
from pieces.piece import Piece


class BoardController:  # TODO: Bridge pattern
    def __init__(self, board: Board):
        self._board_tiles: List[List[Square]] = board.get_board_tiles()
        self._width, self._height = board.get_board_size()
        self._turn: int = Alliance.WHITE
        self._selected_piece: Optional[Piece] = None

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        square = self._board_tiles[row][col]
        return square.get_piece() if square else None

    def change_turn(self):
        if Alliance.is_black(self._turn):
            self._turn = Alliance.WHITE
        else:
            self._turn = Alliance.BLACK

    def set_piece(self, piece: Piece, row: int, col: int):
        self._board_tiles[row][col].set_piece(piece)

    def has_selected_piece(self):
        return bool(self._selected_piece)

    def set_selected_piece(self, piece: Piece):
        self._selected_piece = piece

    def is_same_alliance(self, piece: Piece) -> bool:
        return bool(piece and self._turn == piece.alliance)

    def handle_click(self, mx, my):
        tile_width = self._width // 8
        tile_height = self._height // 8
        col = mx // tile_width
        row = my // tile_height
        occupied_piece = self.get_piece(row, col)
        if self.is_same_alliance(occupied_piece):
            self.set_selected_piece(occupied_piece)
