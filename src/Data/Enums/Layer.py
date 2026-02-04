from cmath import inf
from enum import Enum


class Layer(Enum):
    DEFAULT = 0
    TILE = 1
    POSSIBLE_MOVE = 2
    COORDINATE = 3
    STATIC_PIECE = 4
    MOVING_PIECE = 5