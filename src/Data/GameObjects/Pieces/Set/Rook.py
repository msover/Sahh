from src.Data.Enums.File import File
from src.Data.Enums.ObjectType import ObjectType
from src.Data.Enums.Rank import Rank
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Position.Position import Position


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.ROOK, position)

    def moveset(self) -> list[list[Position]]:
        down: list[Position] = []
        up: list[Position] = []
        right: list[Position] = []
        left: list[Position] = []

        ranks = Rank.all()
        files = File.all()

        for index in range(len(ranks) - 1, -1, -1):
            rank = ranks[index]
            if rank.value <= self.position.rank.value:
                continue
            down.append(Position(self.position.file, rank))

        for index in range(len(ranks)):
            rank = ranks[index]
            if rank.value >= self.position.rank.value:
                continue
            up.append(Position(self.position.file, rank))

        for index in range(len(files)):
            file = files[index]
            if file.value <= self.position.file.value:
                continue
            right.append(Position(file, self.position.rank))

        for index in range(len(files) - 1, -1, -1):
            file = files[index]
            if file.value >= self.position.file.value:
                continue
            left.append(Position(file, self.position.rank))

        return [up, down, left, right]
