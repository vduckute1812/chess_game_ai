from typing import List, Dict, Optional

from ai_engine.constant import PIECE_POSITION_SCORES, PIECE_VALUE_MAP, DEPTH, CHECKMATE
from boards.constant import Alliance
from boards.pieces.contants import PieceType
from history.move import Move
from singleton import Singleton


class Minimax(Singleton):
    _next_move = None

    @classmethod
    def find_best_move(cls, board_config: Dict[int, List[int]], moves: List[Move], turn: int) -> Optional[Move]:
        cls._next_move = None   # reset
        turn_multiplier = 1 if Alliance.is_white(turn) else -1
        cls.negamax_alpha_beta(board_config, moves, DEPTH,  -CHECKMATE, CHECKMATE, turn_multiplier)
        return cls._next_move

    @classmethod
    def negamax_alpha_beta(
        cls,
        board_config: Dict[int, List[int]],
        valid_moves: List[Move],
        depth: int,
        alpha: int,
        beta: int,
        turn_multiplier: int,
    ):
        """
        Negamax algorithm with alpha-beta pruning
        :param board_config:
        :param valid_moves:
        :param depth:
        :param alpha:
        :param beta:
        :param turn_multiplier:
        :return:
        """
        from controller.board_controller import BoardController
        from history.move_handler import MoveHandler
        max_score = -CHECKMATE
        if depth == 0:
            return turn_multiplier * cls.score_board(board_config)
        for move in valid_moves:
            MoveHandler().redo(move, is_ai=True)
            next_moves = BoardController().generate_valid_moves()
            board_config = BoardController().get_board_config()
            score = -cls.negamax_alpha_beta(board_config, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
            print(score)
            if score > max_score:
                max_score = score
                if depth == DEPTH:
                    cls._next_move = move
            MoveHandler().undo(move, is_ai=True)
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score

    @classmethod
    def score_board(cls, board_config: Dict[int, List[int]]):
        """
        Score the board. A positive score is good for white, a negative score is good for black.
        """
        score = 0
        for piece_type, index_ids in board_config.items():
            for index in index_ids:
                if not PieceType.is_king(piece_type):
                    score += PIECE_POSITION_SCORES[piece_type][index]
                if PieceType.is_white(piece_type):
                    score += PIECE_VALUE_MAP[piece_type]
        return score
