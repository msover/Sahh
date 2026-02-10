from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.Board.Board import Board


class Tile(Board):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.TILE, position)
    def setHighlight(self):
        self.objectType = ObjectType.TILE_HIGHLIGHT
        self.makeSprite()
    def resetHighlight(self):
        self.objectType = ObjectType.TILE
        self.makeSprite()