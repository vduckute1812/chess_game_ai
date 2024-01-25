from controller.board_controller import BoardController
from history.move import Move
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: Move):
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().move_piece(move.target_index, move.moved_index, move.first_move, move.target_piece)
        Observer().send(msg=MessageType.MOVE_MADE, moved_index=move.moved_index, target_index=move.target_index)

    @classmethod
    def redo(cls, move: Move):
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().move_piece(move.moved_index, move.target_index, first_move=False)
        Observer().send(msg=MessageType.MOVE_MADE, moved_index=move.moved_index, target_index=move.target_index)
