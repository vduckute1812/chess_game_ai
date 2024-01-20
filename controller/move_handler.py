from controller.board_controller import BoardController
from controller.constant import MoveType
from controller.move_history import MoveHistory
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: MoveHistory):
        match move.move_type:
            case MoveType.ATTACK:
                pass
            case MoveType.NORMAL:
                BoardController().move_piece(move.target_index, move.moved_index)
                BoardController().set_piece(move.target_piece, move.target_index)

    @classmethod
    def redo(cls, move: MoveHistory):
        match move.move_type:
            case MoveType.ATTACK:
                pass
            case MoveType.NORMAL:
                BoardController().move_piece(move.moved_index, move.target_index)

    def handle_attack_move(self):
        pass