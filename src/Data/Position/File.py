from enum import Enum

from src.UI.Display.DisplayWindow import DisplayWindow

class File(Enum):
    A = 0 * DisplayWindow().getScalingFactor()
    B = 1 * DisplayWindow().getScalingFactor()
    C = 2 * DisplayWindow().getScalingFactor()
    D = 3 * DisplayWindow().getScalingFactor()
    E = 4 * DisplayWindow().getScalingFactor()
    F = 5 * DisplayWindow().getScalingFactor()
    G = 6 * DisplayWindow().getScalingFactor()
    H = 7 * DisplayWindow().getScalingFactor()

    @classmethod
    def match(cls, index: int):
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