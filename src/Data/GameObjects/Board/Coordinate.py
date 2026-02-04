from src.Data.Position.Position import Position


class Coordinate:
    def __init__(self, position: Position):
        self._position = position

class One(Coordinate):
    def __init__(self, position: Position):
        super().__init__(position)
