from src.Data.Enums.ObjectType import ObjectType
from src.Data.Enums.Rank import Rank
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Position.Position import Position


class Horse(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.HORSE, position)

    def moveset(self) -> list[list[Position]]:
        rank1 = Rank.getFromNormalized(min(max(self.position.rank.getNormalized() - 2, 0), 8))
        branch1: list[Position] = [Position(self.position.file, self.position.rank)]
        branch2: list[Position] = [Position(self.position.file, self.position.rank)]
        branch3: list[Position] = [Position(self.position.file, self.position.rank)]
        branch4: list[Position] = [Position(self.position.file, self.position.rank)]
        branch5: list[Position] = [Position(self.position.file, self.position.rank)]
        branch6: list[Position] = [Position(self.position.file, self.position.rank)]
        branch7: list[Position] = [Position(self.position.file, self.position.rank)]
        branch8: list[Position] = [Position(self.position.file, self.position.rank)]

        return [branch1, branch2, branch3, branch4, branch5, branch6, branch7, branch8]
