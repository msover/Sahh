from cmath import inf
from enum import Enum


class Layer(Enum):
    DEFAULT = 0
    TILE = 1
    COORDINATE = 2
    STATIC_PIECE = 3