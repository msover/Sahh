from src.Data.Enums.ObjectType import ObjectType
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Position.Position import Position


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.BISHOP, position)