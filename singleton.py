from controller.move import Move


class Singleton(object):  # TODO: Singleton pattern
    _instance = None
    _move_history = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
