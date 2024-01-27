from typing import Optional

from controller.board_controller import BoardController
from history.move_mgr import MoveManager
from events.base import BaseEvent
from events.constant import EventHandlerType


class EventHandler(BaseEvent):
    def __init__(self, _type: int, _pos: Optional[tuple] = None):
        super().__init__(_type)
        self._pos = _pos

    def process(self):
        match self._type:
            case EventHandlerType.MOUSE_CLICK:
                move = BoardController().handle_board_event(self._pos[0], self._pos[1])
                move and MoveManager().add_move(move=move)
            case EventHandlerType.QUIT:
                BoardController().force_quit()
            case EventHandlerType.UNDO:
                MoveManager().undo()
                BoardController().is_ai_turn() and MoveManager().undo()
            case EventHandlerType.REDO:
                MoveManager().redo()
                BoardController().is_ai_turn() and MoveManager().redo()
