from cmath import inf
from enum import Enum

from src.UI.Display.DisplayWindow import DisplayWindow


class Rank(Enum):
    NaN = 8 * DisplayWindow().getTileScalingFactor()
    ONE = 7 * DisplayWindow().getTileScalingFactor()
    TWO = 6 * DisplayWindow().getTileScalingFactor()
    THREE = 5 * DisplayWindow().getTileScalingFactor()
    FOUR = 4 * DisplayWindow().getTileScalingFactor()
    FIVE = 3 * DisplayWindow().getTileScalingFactor()
    SIX = 2 * DisplayWindow().getTileScalingFactor()
    SEVEN = 1 * DisplayWindow().getTileScalingFactor()
    EIGHT = 0 * DisplayWindow().getTileScalingFactor()


    @classmethod
    def all(cls):
        return [r for r in Rank if r != Rank.NaN]

    def getNormalized(self) -> float:
        return self.value // DisplayWindow().getTileScalingFactor()

    @classmethod
    def getFromNormalized(cls, index: int):
        match index:
            case 7:
                return Rank.EIGHT
            case 6:
                return Rank.SEVEN
            case 5:
                return Rank.SIX
            case 4:
                return Rank.FIVE
            case 3:
                return Rank.FOUR
            case 2:
                return Rank.THREE
            case 1:
                return Rank.TWO
            case 0:
                return Rank.ONE
            case _:
                return None

    @classmethod
    def matchSetup(cls, index: int):
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

    @classmethod
    def matchMouseclick(cls, pixel: int):
        if pixel >= Rank.EIGHT.value and pixel < Rank.SEVEN.value:
            return Rank.EIGHT
        elif pixel >= Rank.SEVEN.value and pixel < Rank.SIX.value:
            return Rank.SEVEN
        elif pixel >= Rank.SIX.value and pixel < Rank.FIVE.value:
            return Rank.SIX
        elif pixel >= Rank.FIVE.value and pixel < Rank.FOUR.value:
            return Rank.FIVE
        elif pixel >= Rank.FOUR.value and pixel < Rank.THREE.value:
            return Rank.FOUR
        elif pixel >= Rank.THREE.value and pixel < Rank.TWO.value:
            return Rank.THREE
        elif pixel >= Rank.TWO.value and pixel < Rank.ONE.value:
            return Rank.TWO
        elif pixel >= Rank.ONE.value and pixel < Rank.NaN.value:
            return Rank.ONE
        return Rank.NaN