from controller.board_controller import BoardController
from controller.constant import MoveType
from controller.move_history import MoveHistory
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: MoveHistory):
        BoardController().move_piece(move.target_index, move.moved_index)
        BoardController().set_piece(move.target_piece, move.target_index)
        Observer().send(msg=MessageType.BOARD_CHANGED)

    @classmethod
    def redo(cls, move: MoveHistory):
        BoardController().move_piece(move.moved_index, move.target_index)
        Observer().send(msg=MessageType.BOARD_CHANGED)

    def handle_attack_move(self):
        pass