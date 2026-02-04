from src.Data.Enums.ObjectType import ObjectType
from src.Data.GameObjects.Pieces.Piece import Piece

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.KING, position)