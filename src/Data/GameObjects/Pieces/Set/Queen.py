from src.Data.Enums.Movement.Direction import Direction
from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.GameObjects.Pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.QUEEN, position)

    def moveset(self) -> list[MovesetOption]:
        movesetOptions: list[MovesetOption] = []
        movesetOptions.append(MovesetOption(UniversalMoveset.FILE, Direction.UP))
        movesetOptions.append(MovesetOption(UniversalMoveset.FILE, Direction.DOWN))
        movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.LEFT))
        movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.RIGHT))
        movesetOptions.append(MovesetOption(UniversalMoveset.MAIN_DIAGONAL, Direction.DOWN))
        movesetOptions.append(MovesetOption(UniversalMoveset.MAIN_DIAGONAL, Direction.UP))
        movesetOptions.append(MovesetOption(UniversalMoveset.SECOND_DIAGONAL, Direction.UP))
        movesetOptions.append(MovesetOption(UniversalMoveset.SECOND_DIAGONAL, Direction.DOWN))
        return movesetOptions