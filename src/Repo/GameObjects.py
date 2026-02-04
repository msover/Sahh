import pygame

from src.Data.Enums.Color import Color
from src.Data.GameObjects.GameObject import GameObject
from src.Data.GameObjects.Board.Tile import Tile
from src.Data.Position.File import File
from src.Data.Position.Position import Position
from src.Data.Position.Rank import Rank
from src.Repo.TextRepo import TextRepo
from src.UI.Display.DisplayWindow import DisplayWindow


class GameObjects:
    def __init__(self):
        self._sprites = pygame.sprite.LayeredUpdates()
        self._tiles = TextRepo("src\\Assets\\TileLayout.txt").getData()
        self._pieces = TextRepo("src\\Assets\\PieceLayout.txt").getData()

    def add(self, gameObject: GameObject):
        self._sprites.add(gameObject)
    def remove(self, gameObject: GameObject):
        self._sprites.remove(gameObject)

    def setTiles(self):
        for row in range(8):
            for col in range(8):
                color = Color.match(self._tiles[row][col])
                pos = Position(File.match(row), Rank.match(col))
                self.add(Tile(color, pos))

    def draw(self):
        self._sprites.draw(DisplayWindow().getSurface())
        DisplayWindow().update()
