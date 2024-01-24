from typing import Optional

from controller.board_controller import BoardController
from controller.move_mgr import MoveManager
from events.base import BaseEvent
from events.constant import EventHandlerType


class EventHandler(BaseEvent):
    def __init__(self, _type: int, _pos: Optional[tuple] = None):
        super().__init__(_type)
        self._pos = _pos

    def process(self):
        match self._type:
            case EventHandlerType.MOUSE_CLICK:
                BoardController().handle_board_event(self._pos[0], self._pos[1])
            case EventHandlerType.QUIT:
                BoardController().force_quit()
            case EventHandlerType.UNDO:
                MoveManager().undo()
            case EventHandlerType.REDO:
                MoveManager().redo()
