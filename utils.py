from typing import Tuple

class Utils:
    def is_same_position(pos_1: Tuple[int, int], pos_2: Tuple[int, int]) -> bool:
        return pos_1[0] == pos_2[0] and pos_1[1] == pos_2[1]