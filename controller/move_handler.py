from controller.board_controller import BoardController
from controller.constant import MoveType
from controller.move_history import MoveHistory
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: MoveHistory):
        BoardController().reset_selected_highlight()
        BoardController().move_piece(move.target_index, move.moved_index, move.move_type, move.first_move, is_undo=True)
        BoardController().set_piece(move.target_piece, move.target_index)
        Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[move.moved_index, move.target_index])

    @classmethod
    def redo(cls, move: MoveHistory):
        BoardController().move_piece(move.moved_index, move.target_index, move.move_type, False)
        Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[move.moved_index, move.target_index])

    def handle_attack_move(self):
        pass
