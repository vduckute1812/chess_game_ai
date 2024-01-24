from functools import wraps
from typing import TYPE_CHECKING, Callable, List

from observer.constant import MessageType
from observer.observer import Observer

if TYPE_CHECKING:
    from boards.board import Board
    from boards.pieces.piece import Piece


def input_validate(func: Callable):
    def wrapper(cls, piece, board):
        if piece and board:
            return func(cls, piece, board)

    return wrapper


class BoardTileRender:
    @classmethod
    @input_validate
    def render_selected_piece_tiles(cls, piece: "Piece", board: "Board"):
        valid_moves, _ = piece.get_valid_moves()
        square_index = piece.get_square_index()
        board.set_highlight([square_index] + valid_moves, highlight=True)
        Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, selected_indexes=[square_index] + valid_moves)

    @classmethod
    @input_validate
    def reset_selected_piece_tiles(cls, piece: "Piece", board: "Board") -> List[int]:
        square_index = piece.get_square_index()
        valid_moves, attack_moves = piece.get_valid_moves()
        valid_moves.append(square_index)
        board.set_highlight(valid_moves, highlight=False)
        Observer().send(msg=MessageType.SQUARE_HIGHLIGHT, selected_indexes=[square_index] + valid_moves)
        return valid_moves

    @classmethod
    def update_piece_tiles(cls, selected_index: int, target_index: int):
        Observer().send(msg=MessageType.MOVE_MADE, selected_indexes=[target_index, selected_index])
