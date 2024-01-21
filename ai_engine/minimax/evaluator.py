from typing import Dict, List

from singleton import Singleton


class StandardBoardEvaluator:
    @classmethod
    def evaluate(cls, board_config: Dict[int, List[int]],  depth: int = 0) -> float:
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