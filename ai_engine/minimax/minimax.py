from ai_engine.constant import PIECE_POSITION_SCORES, PIECE_VALUE_MAP
from controller.board_controller import BoardController
from game.game_state import GameState
from boards.pieces.contants import PieceType
from observer.constant import MessageType
from observer.observer import Listener, Observer
from singleton import Singleton


class Minimax(Singleton, Listener):
    def __init__(self):
        super().__init__()
        Observer().listen_to(self)

    @classmethod
    def find_best_move(cls, moves):
        pass

    def on_message_received(
            self, msg: int, **kwargs
    ):
        match msg:
            case MessageType.AI_MOVE:
                BoardController().handle_ai_turn()
                BoardController().change_turn()

    @classmethod
    def negamax_alpha_beta(cls, valid_moves, depth, alpha, beta, turn_multiplier):
        """
        Negamax algorithm with alpha-beta pruning
        :param valid_moves:
        :param depth:
        :param alpha:
        :param beta:
        :param turn_multiplier:
        :return:
        """
        return 0
        # board_config = game_state.board.to_square_piece_index_map()
        # if depth == 0:
        #     return turn_multiplier * cls.score_board(game_state)
        # # move ordering - implement later //TODO
        # max_score = -CHECKMATE
        # for move in valid_moves:
        #     # game_state.make_move(move)  Handle make move // TODO
        #     # next_moves = game_state.getValidMoves()  Handle get valid moves // TODO
        #     next_moves = []
        #     score = -cls.negamax_alpha_beta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        #     if score > max_score:
        #         max_score = score
        #         if depth == DEPTH:
        #             next_move = move
        #     # game_state.undoMove()  Handle undo move //TODO
        #     if max_score > alpha:
        #         alpha = max_score
        #     if alpha >= beta:
        #         break
        # return max_score

    @classmethod
    def score_board(cls, game_state: GameState):
        """
        Score the board. A positive score is good for white, a negative score is good for black.
        """
        # if game_state.checkmate:
        #     if Alliance.is_white(game_state.turn):
        #         return -CHECKMATE  # black wins
        #     else:
        #         return CHECKMATE  # white wins
        # elif game_state.stalemate:
        #     return STALEMATE
        score = 0
        for square_index in game_state.board:
            piece_type = game_state.board[square_index]
            if not PieceType.is_king(piece_type):
                score += PIECE_POSITION_SCORES[piece_type][square_index]
            if PieceType.is_white(piece_type):
                score += PIECE_VALUE_MAP[piece_type]
        return score
