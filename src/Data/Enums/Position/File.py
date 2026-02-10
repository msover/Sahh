from cmath import inf
from enum import Enum

from src.UI.Display.DisplayConstants import DisplayConstants


class File(Enum):
    A = 0 * DisplayConstants.TILE_SCALING_FACTOR
    B = 1 * DisplayConstants.TILE_SCALING_FACTOR
    C = 2 * DisplayConstants.TILE_SCALING_FACTOR
    D = 3 * DisplayConstants.TILE_SCALING_FACTOR
    E = 4 * DisplayConstants.TILE_SCALING_FACTOR
    F = 5 * DisplayConstants.TILE_SCALING_FACTOR
    G = 6 * DisplayConstants.TILE_SCALING_FACTOR
    H = 7 * DisplayConstants.TILE_SCALING_FACTOR
    NaN = 8 * DisplayConstants.TILE_SCALING_FACTOR

    @classmethod
    def all(cls):
        return [f for f in File if f != File.NaN]

    @classmethod
    def getIndex(cls, file):
        if file.name == File.A:
            return 0
        return file.value // DisplayConstants.TILE_SCALING_FACTOR

    @classmethod
    def matchIndex(cls, index: int):
        match index:
            case 0:
                return File.A
            case 1:
                return File.B
            case 2:
                return File.C
            case 3:
                return File.D
            case 4:
                return File.E
            case 5:
                return File.F
            case 6:
                return File.G
            case 7:
                return File.H
            case _:
                return None

    @classmethod
    def matchMouseclick(cls, pixel: int):
        if pixel >= File.A.value and pixel < File.B.value:
            return File.A
        elif pixel >= File.B.value and pixel < File.C.value:
            return File.B
        elif pixel >= File.C.value and pixel < File.D.value:
            return File.C
        elif pixel >= File.D.value and pixel < File.E.value:
            return File.D
        elif pixel >= File.E.value and pixel < File.F.value:
            return File.E
        elif pixel >= File.F.value and pixel < File.G.value:
            return File.F
        elif pixel >= File.G.value and pixel < File.H.value:
            return File.G
        elif pixel >= File.H.value and pixel < File.NaN.value:
            return File.H
        return File.NaN