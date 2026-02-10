from enum import Enum


class Color(Enum):
    BLACK = "b"
    WHITE = "w"
    NaN = "w"

    @classmethod
    def match(cls, index: int):
        match index:
            case 0:
                return Color.WHITE
            case 1:
                return Color.BLACK
            case _:
                return None