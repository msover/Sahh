from src.Data.Position.File import File
from src.Data.Position.Rank import Rank


class Position:
    def __init__(self, file: File, rank: Rank):
        self.rank = rank
        self.file = file