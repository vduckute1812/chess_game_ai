from typing import Dict, List

from game_state import GameState
from singleton import Singleton


class StandardBoardEvaluator:
    @classmethod
    def evaluate(cls, board: GameState, alliance: int,  depth: int = 0) -> float:
        """
        Provides a number representing the value of the board at a given state
        :param board: the current board being used for the game (Board)
        :param alliance: color associated with maximizing player (tuple)
        :param depth: the depth of the current board state (int)
        :return: integer representing boards value
        """
        return 0.0

    def _score_player(self, board_config: Dict[int, List[int]]):
        pass

    def _mobility(self, board_config: Dict[int, List[int]]):
        pass

    def _mobility_ratio(self, board_config: Dict[int, List[int]]):
        pass

    def _check(self, board_config: Dict[int, List[int]]):
        pass

    def _king_threats(self, board_config: Dict[int, List[int]]):
        pass

    def _depth_bonus(self, board_config: Dict[int, List[int]]):
        pass

    def _piece_value(self, board_config: Dict[int, List[int]]):
        pass

    def _attacks(self, board_config: Dict[int, List[int]]):
        pass

    def _king_safety(self, board_config: Dict[int, List[int]]):
        pass

    def _piece_evaluations(self, board_config: Dict[int, List[int]]):
        pass