from ai_engine.minimax.evaluator import StandardBoardEvaluator
from controller.board_controller import BoardController
from singleton import Singleton


class Minimax(Singleton):

    def execute(self):
        pass

    # Refer: https://www.chessprogramming.org/Alpha-Beta
    def min(self, board_config, depth: int, highest: float, lowest: float) -> float:
        if depth == 0:
            return StandardBoardEvaluator.evaluate(board_config, depth)
        alliance_indexes, opponent_indexes = BoardController().collect_all_valid_moves()

    def max(self, board, depth: int, highest: float, lowest: float) -> float:
        return 0.0
