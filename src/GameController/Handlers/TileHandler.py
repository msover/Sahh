from src.Data.Enums.Visual.Color import Color
from src.Data.GameObjects.Board.Tile import Tile
from src.Data.Enums.Position.File import File
from src.Data.Position.Position import Position
from src.Data.Enums.Position.Rank import Rank
from src.Repo.GameObjects import GameObjects
from src.Repo.MatchRepo import MatchRepo


class TileHandler:
    def __init__(self, match: MatchRepo, gameObjects: GameObjects):
        self._gameObjects = gameObjects
        self._match = match
        self._selectedTile = Tile(Color.NaN, Position(File.NaN, Rank.NaN))

    @property
    def selectedTile(self):
        return self._selectedTile

    @selectedTile.setter
    def selectedTile(self, selectedTile: Tile):
        self._selectedTile = selectedTile

    def reset(self):
        self._selectedTile.resetHighlight()
        self._selectedTile = Tile(Color.NaN, Position(File.NaN, Rank.NaN))