class Singleton: # TODO: Singleton pattern
    _instance = None

    def __new__(self, *args, **kwargs):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self)
            print(id(self._instance))
        return self._instance
