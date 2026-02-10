from enum import Enum


class ObjectType(Enum):
    PAWN = "p"
    ROOK = "r"
    HORSE = "n"
    BISHOP = "b"
    QUEEN = "q"
    KING = "k"
    TILE = "t"
    TILE_HIGHLIGHT = "th"
    POSSIBLE_MOVE = "p"
    EMPTY = "empty"
    COORDINATE = "coordinate"

    @classmethod
    def match(cls, index: int):
        match index:
            case 1:
                return ObjectType.PAWN
            case 2:
                return ObjectType.ROOK
            case 3:
                return ObjectType.HORSE
            case 4:
                return ObjectType.BISHOP
            case 5:
                return ObjectType.QUEEN
            case 6:
                return ObjectType.KING
            case 7:
                return ObjectType.TILE
            case _:
                return ObjectType.EMPTY
