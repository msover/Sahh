from src.Data.Enums.Layer import Layer
from src.Data.Enums.SpriteType import SpriteType
from src.Data.GameObjects.GameObject import GameObject


class Tile(GameObject):
    def __init__(self, color, position):
        super().__init__(color, SpriteType.TILE, position)
        self._layer = Layer.TILE.value