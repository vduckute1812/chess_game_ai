from typing import List

from controller.board_controller import BoardController
from controller.move_history import Move
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton
from controller.move_handler import MoveHandler


class MoveManager(Singleton):  # TODO: Command pattern
    __m_index: int = 0
    __moves: List[Move] = []

    def add_move(self, move: Move):
        # Delete all moves from current index to the end
        self.__moves = self.__moves[:self.__m_index]
        self.__moves.append(move)
        self.__m_index += 1

    def undo(self):
        if self.has_undo():
            self.__m_index -= 1
            move = self.__moves[self.__m_index]
            BoardController().reset_selected_highlight()
            MoveHandler.undo(move)
            Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[move.moved_index, move.target_index])

    def redo(self):
        if self.has_redo():
            move = self.__moves[self.__m_index]
            MoveHandler.redo(move)
            self.__m_index += 1
            Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[move.moved_index, move.target_index])

    def has_undo(self) -> bool:
        return self.__m_index > 0

    def has_redo(self) -> bool:
        return self.__m_index < len(self.__moves)
