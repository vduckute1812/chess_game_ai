from typing import List, Tuple

from boards.constant import WINDOW_SIZE, BOARD_COLUMNS
from boards.square import Square
from utils import Utils


class Board:
    def __init__(self):
        self._width, self._height = WINDOW_SIZE
        self._board: List[List[Square]] = self.generate_squares()
        Utils.set_init_board(self)

    def generate_squares(self) -> List[List[Square]]:
        board = []
        tile_width = self._width // 8
        tile_height = self._height // 8
        for y in range(8):
            squares = []
            for x in range(8):
                squares.append(
                    Square(x,  y, tile_width, tile_height)
                )
            board.append(squares)
        return board

    def get_board_tiles(self) -> List[List[Square]]:
        return self._board

    def get_square(self, row: int, col: int):
        return self._board[row][col]

    def draw(self, display):
        for squares in self._board:
            for square in squares:
                square.draw(display)