from typing import List, Tuple, Optional

from boards.square import Square
from pieces.contants import Alliance
from pieces.piece import Piece
from utils import Utils


class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._board: List[List[Square]] = []
        self.generate_squares()
        self._turn: int = Alliance.WHITE
        self._selected_piece: Optional[Piece] = None

    def generate_squares(self):
        tile_width = self._width // 8
        tile_height = self._height // 8
        for y in range(8):
            squares = []
            for x in range(8):
                squares.append(
                    Square(x,  y, tile_width, tile_height)
                )
            self._board.append(squares)

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        square = self._board[row][col]
        return square.get_piece() if square else None

    def change_turn(self):
        self._turn = Alliance.WHITE if self._turn == Alliance.WHITE else Alliance.BLACK

    def handle_click(self, mx, my):
        tile_width = self._width // 8
        tile_height = self._height // 8
        column = mx // tile_width
        row = my // tile_height
        occupied_piece = self._board[row][column].get_piece()
        if self._selected_piece is None:
            self._selected_piece = occupied_piece
        elif self._selected_piece.move():
            self.change_turn()
        if occupied_piece and occupied_piece.color == self._turn:
            self._selected_piece = occupied_piece

    def draw(self, display):
        if self._selected_piece is not None:
            row, col = self._selected_piece.get_pos()
            square = self._board[row][col]
            square.set_highlight(True)
            for square in []:
                square.set_highlight(True)
        for squares in self._board:
            for square in squares:
                square.draw(display)