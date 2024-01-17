from typing import List

from controller.move import Move
from singleton import Singleton


class MoveManager(Singleton):   # TODO: Command pattern
    __m_index: int = 0
    __moves: List[Move] = []

    def add_move(self, move: Move):
        self.__moves.append(move)
        self.__m_index += 1
        print(f"Add move {move._moved_coordinate} {move._dest_coordinate}")

    def undo(self):
        self.__m_index -= 1
        self.__moves[self.__m_index].undo()

    def redo(self):
        self.__m_index += 1
        self.__moves[self.__m_index].redo()

    def has_undo(self) -> bool:
        return self.__m_index > 0

    @classmethod
    def has_redo(self) -> bool:
        return self.__m_index < len(self.__moves)
