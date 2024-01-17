class BaseEvent:
    def __init__(self, _type: int):
        self._type = _type

    def process(self, controller):
        pass
