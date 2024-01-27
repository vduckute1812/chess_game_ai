from dataclasses import dataclass, field
from typing import Optional, Dict
from boards.constant import Alliance


@dataclass
class GameState:
    turn: int = Alliance.UNKNOWN
    ai_thinking: bool = False
    running: bool = False
    check_mate: bool = False
    ai_player: Dict = None

    def set_player_config(self):
        self.ai_player = {
            Alliance.WHITE: True,
            Alliance.BLACK: True
        }
