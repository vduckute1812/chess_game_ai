
from abc import ABCMeta, abstractmethod
from Piece.constant.constant import Alliance, PieceType
from DataObject.data import Position

class Piece(metaclass=ABCMeta):
    "The Builder Interface"

    def __init__(self):
        self._aliance: Alliance
        self._type: PieceType
        self._position: Position

    @staticmethod
    @abstractmethod
    def get_generating_moves():
        pass


    @staticmethod
    def move(self, x: int, y: int):
        _position.x = x
        _position.y = y


class King(Piece):
    def get_generating_moves(self):
        print("moves")
