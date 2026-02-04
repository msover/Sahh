from src.Data.Enums.File import File
from src.Data.Enums.Rank import Rank

class Position:
    def __init__(self, rank: Rank, file: File):
        self.rank = rank
        self.file = file