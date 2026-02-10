from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset


class Horse(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.HORSE, position)

    def moveset(self) -> list[MovesetOption]:
        return [MovesetOption(UniversalMoveset.HORSE)]