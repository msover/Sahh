from enum import Enum


class GameState(Enum):
    WHITE_TURN = 0
    BLACK_TURN = 1
    CHOOSE_PIECE = 2
    MOVE_PIECE = 3
    IDLE = 4
    CHECK = 5
    CHECKMATE = 6
