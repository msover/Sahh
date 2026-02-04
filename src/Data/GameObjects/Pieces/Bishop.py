from src.Data.Enums.Layer import Layer
from src.Data.Enums.SpriteType import SpriteType
from src.Data.GameObjects.GameObject import GameObject


class Bishop(GameObject):
    def __init__(self, color, position):
        super().__init__(color, SpriteType.BISHOP, position)
        self._layer = Layer.STATIC_PIECE