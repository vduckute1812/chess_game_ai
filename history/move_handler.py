from controller.board_controller import BoardController
from history.move import Move
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: Move, is_ai: bool = False):
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().make_move(move.target_index, move.moved_index, move.first_move, move.attacked_piece)
        Observer().send(
            msg=MessageType.MOVE_MADE,
            moved_index=move.target_index,
            target_index=move.moved_index,
            moved_piece_type=move.moved_piece_type,
            attacked_piece=move.attacked_piece,
            is_undo=True,
            is_ai=is_ai,
        )

    @classmethod
    def redo(cls, move: Move, is_ai: bool = False):
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().make_move(move.moved_index, move.target_index, first_move=False)
        Observer().send(
            msg=MessageType.MOVE_MADE,
            moved_index=move.moved_index,
            target_index=move.target_index,
            moved_piece_type=move.moved_piece_type,
            attacked_piece=move.attacked_piece,
            is_ai=is_ai,
        )
