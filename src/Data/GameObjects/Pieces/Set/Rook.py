from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Enums.Movement.Direction import Direction


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.ROOK, position)
    def moveset(self) -> list[MovesetOption]:
        movesetOptions: list[MovesetOption] = []
        movesetOptions.append(MovesetOption(UniversalMoveset.FILE, Direction.UP))
        movesetOptions.append(MovesetOption(UniversalMoveset.FILE, Direction.DOWN))
        movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.LEFT))
        movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.RIGHT))
        return movesetOptions