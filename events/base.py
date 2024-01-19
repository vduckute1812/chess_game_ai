from events.constant import EventHandlerType


class BaseEvent:
    def __init__(self, _type: int = EventHandlerType.UNKNOWN):
        self._type = _type

    def process(self):
        pass
