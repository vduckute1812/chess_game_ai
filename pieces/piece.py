from typing import Tuple


class Piece:
    def __init__(self, x: int, y: int, alliance: int):
        self._x = x
        self._y = y
        self._alliance = alliance

    def get_pos(self) -> Tuple[int, int]:
        return self._x, self._y

    @property
    def color(self) -> int:
        return self._alliance

    def move(self) -> bool:
        return True

    def draw(self, display):
        pass