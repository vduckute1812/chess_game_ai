from dataclasses import dataclass
from typing import Optional, Dict
from boards.constant import Alliance


@dataclass
class GameState:
    turn: int = Alliance.UNKNOWN
    running: bool = False
    ai_player: Dict = None


    def set_player_config(self):
        self.ai_player = {
            Alliance.WHITE: False,
            Alliance.BLACK: False
        }
