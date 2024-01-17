class Move:
    def __init__(self, moved_coord: int, dest_coord: int):
        self._moved_coordinate = moved_coord
        self._dest_coordinate = dest_coord

    def redo(self):
        pass

    def undo(self):
        pass
