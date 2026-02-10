from math import inf

from src.Data.Enums.Movement.Direction import Direction
from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset


class MovesetOption:
    def __init__(self, moveset: UniversalMoveset, direction: Direction = Direction.UP, restriction: int = 7):
        self.moveset = moveset
        self.direction = direction
        self.restriction = restriction

    def __repr__(self):
        return f"{self.moveset.name}:{self.direction.name}:{self.restriction}"