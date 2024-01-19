from controller.board_controller import BoardController
from controller.move import Move
from singleton import Singleton


class MoveHandler(Singleton):

    def undo(self, move: Move):
        BoardController().move_piece(move.target_index, move.moved_index)
        BoardController().set_piece(move.target_piece, move.target_index)

    def redo(self, move: Move):
        BoardController().move_piece(move.moved_index, move.target_index)
