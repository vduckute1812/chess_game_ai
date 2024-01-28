from controller.board_controller import BoardController
from history.move import Move
from observer.constant import MessageType
from observer.observer import Observer
from singleton import Singleton


class MoveHandler(Singleton):

    @classmethod
    def undo(cls, move: Move, is_ai: bool = False):
        if not BoardController().is_ai_thinking():
            return
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().make_move(move, is_undo=True, is_ai=is_ai)

    @classmethod
    def redo(cls, move: Move, is_ai: bool = False):
        if not BoardController().is_ai_thinking():
            return
        BoardController().update_highlight_tiles(highlight=False)
        BoardController().make_move(move, is_ai=is_ai)
