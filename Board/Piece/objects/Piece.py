
from abc import ABCMeta, abstractmethod
from Board.Piece.constant.constant import Alliance, PieceType
from DataObject.data import Position

class Piece(metaclass=ABCMeta):
    "The Builder Interface"

    def __init__(self):
        self._aliance: Alliance
        self._type: PieceType
        self._position: Position = Position()

    @staticmethod
    @abstractmethod
    def generate_legal_moves():
        pass


    def set_position(self, x: int, y: int):
        self._position.x = x
        self._position.y = y

    def get_position(self) -> tuple:
        return (self._position.x, self._position.y)


class King(Piece):
    def __init__(self):
        super().__init__()

    def generate_legal_moves(self):
        print("moves")

class King(Piece):
    def __init__(self):
        super().__init__()

    def generate_legal_moves(self):
        print("moves")

class King(Piece):
    def __init__(self):
        super().__init__()

    def generate_legal_moves(self):
        print("moves")

class King(Piece):
    def __init__(self):
        super().__init__()

    def generate_legal_moves(self):
        print("moves")
