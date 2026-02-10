from src.Data.Enums.Movement.Direction import Direction
from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.GameObjects.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.PAWN, position)
        self.isFirstMove = True
        self.isSecondMove = False

    def moveset(self) -> list[MovesetOption]:
        movesetOptions: list[MovesetOption] = []
        movesetOptions.append(MovesetOption(UniversalMoveset.MAIN_DIAGONAL, Direction.UP, 1))
        movesetOptions.append(MovesetOption(UniversalMoveset.SECOND_DIAGONAL, Direction.UP, 1))

        if self.isFirstMove:
            movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.UP))
            return movesetOptions
        movesetOptions.append(MovesetOption(UniversalMoveset.RANK, Direction.UP, 1))
        return movesetOptions