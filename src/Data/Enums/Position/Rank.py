from cmath import inf
from enum import Enum

from src.UI.Display.DisplayConstants import DisplayConstants


class Rank(Enum):
    NaN = 8 * DisplayConstants.TILE_SCALING_FACTOR
    ONE = 7 * DisplayConstants.TILE_SCALING_FACTOR
    TWO = 6 * DisplayConstants.TILE_SCALING_FACTOR
    THREE = 5 * DisplayConstants.TILE_SCALING_FACTOR
    FOUR = 4 * DisplayConstants.TILE_SCALING_FACTOR
    FIVE = 3 * DisplayConstants.TILE_SCALING_FACTOR
    SIX = 2 * DisplayConstants.TILE_SCALING_FACTOR
    SEVEN = 1 * DisplayConstants.TILE_SCALING_FACTOR
    EIGHT = 0 * DisplayConstants.TILE_SCALING_FACTOR


    @classmethod
    def all(cls):
        return [r for r in Rank if r != Rank.NaN]

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
    def getIndex(cls, rank):
        if rank == Rank.EIGHT:
            return 0
        return rank.value // DisplayConstants.TILE_SCALING_FACTOR

    @classmethod
    def matchIndex(cls, index: int):
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