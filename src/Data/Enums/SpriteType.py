from enum import Enum


class SpriteType(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    HORSE = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"
    TILE = "square"
    COORDINATE = "coordinate"

    @classmethod
    def match(cls, index: int):
        match index:
            case 0:
                return SpriteType.PAWN
            case 1:
                return SpriteType.ROOK
            case 2:
                return SpriteType.HORSE
            case 3:
                return SpriteType.BISHOP
            case 4:
                return SpriteType.QUEEN
            case 5:
                return SpriteType.KING
            case 6:
                return SpriteType.TILE
            case _:
                return None
