from src.Data.Enums.ObjectType import ObjectType
from src.Data.GameObjects.Board.Board import Board


class Tile(Board):
    def __init__(self, color, position):
        super().__init__(color, ObjectType.TILE, position)
    def switchHighlight(self):
        match self.objectType:
            case ObjectType.TILE:
                self.objectType = ObjectType.TILE_HIGHLIGHT
                self.makeSprite()
                return
            case ObjectType.TILE_HIGHLIGHT:
                self.objectType = ObjectType.TILE
                self.makeSprite()
                return
    def resetHighlight(self):
        self.objectType = ObjectType.TILE
        self.makeSprite()