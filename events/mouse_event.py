from controller.board_controller import BoardController
from events.base import BaseEvent
from events.constant import EventHandlerType


class MouseEvent(BaseEvent):
    def __init__(self, _type: int, _pos: tuple):
        super().__init__(_type)
        self._pos = _pos

    def process(self, controller: BoardController):
        match self._type:
            case EventHandlerType.MOUSE_CLICK:
                controller.handle_click(self._pos[0], self._pos[1])

