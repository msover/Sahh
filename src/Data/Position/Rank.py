from enum import Enum

from src.UI.Display.DisplayWindow import DisplayWindow


class Rank(Enum):
    ONE = 7 * DisplayWindow().getScalingFactor()
    TWO = 6 * DisplayWindow().getScalingFactor()
    THREE = 5 * DisplayWindow().getScalingFactor()
    FOUR = 4 * DisplayWindow().getScalingFactor()
    FIVE = 3 * DisplayWindow().getScalingFactor()
    SIX = 2 * DisplayWindow().getScalingFactor()
    SEVEN = 1 * DisplayWindow().getScalingFactor()
    EIGHT = 0 * DisplayWindow().getScalingFactor()

    @classmethod
    def match(cls, index: int):
        match index:
            case 0:
                return Rank.EIGHT
            case 1:
                return Rank.SEVEN
            case 2:
                return Rank.SIX
            case 3:
                return Rank.FIVE
            case 4:
                return Rank.FOUR
            case 5:
                return Rank.THREE
            case 6:
                return Rank.TWO
            case 7:
                return Rank.ONE
            case _:
                return None