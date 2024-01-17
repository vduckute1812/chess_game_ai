from controller.board_controller import BoardController
from events.base import BaseEvent
from events.constant import EventHandlerType


class GameEvent(BaseEvent):
    def __init__(self, _type: int):
        super().__init__(_type)

    def process(self, controller: BoardController):
        match self._type:
            case EventHandlerType.QUIT:
                controller.force_quit()
