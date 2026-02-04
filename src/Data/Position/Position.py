from src.Data.Enums.File import File
from src.Data.Enums.Rank import Rank


class Position:
    def __init__(self, file: File, rank: Rank):
        self.rank = rank
        self.file = file

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.rank == other.rank and self.file == other.file

    def __str__(self):
        return f"{self.rank.name}:{self.file.name}"

    def __repr__(self):
        return self.__str__()