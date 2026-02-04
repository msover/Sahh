import pygame

from src.Data.Enums.Color import Color
from src.Data.Enums.GameState import GameState
from src.Data.Exceptions.PieceHandlerException import PieceHandlerException
from src.Data.GameObjects.Pieces.Set.Rook import Rook
from src.Data.Enums.File import File
from src.Data.Position.Position import Position
from src.Data.Enums.Rank import Rank
from src.GameController.Handlers.PieceHandler import PieceHandler
from src.GameController.Handlers.TileHandler import TileHandler
from src.Repo.Animations import Animations
from src.Repo.GameObjects import GameObjects
from src.Repo.MatchRepo import MatchRepo


class GameController:
    def __init__(self):
        self.gameObjects = GameObjects()
        self.animations = Animations()
        self.testRook = Rook(Color.BLACK, Position(File.C, Rank.THREE))
        self.match = MatchRepo()
        self.pieceHandler = PieceHandler(self.match, self.gameObjects)
        self.tileHandler = TileHandler(self.match, self.gameObjects)

    def clickEvent(self, event):
        x, y = event.pos
        clickPosition = Position(File.matchMouseclick(x), Rank.matchMouseclick(y))
        match self.match.gameState:
            case GameState.CHOOSE_PIECE:
                try:
                    self.pieceHandler.selectedPiece = self.gameObjects.getPieceAtPosition(clickPosition)
                    self.tileHandler.selectedTile = self.gameObjects.getTileAtPosition(clickPosition)
                    self.tileHandler.selectedTile.switchHighlight()
                    self.match.gameState = GameState.MOVE_PIECE
                    return
                except PieceHandlerException as e:
                    print(e)
                    self.pieceHandler.reset()
                    self.tileHandler.reset()
                    self.match.gameState = GameState.CHOOSE_PIECE
                    return
            case GameState.MOVE_PIECE:
                try:
                    self.pieceHandler.targetPosition = clickPosition
                    self.tileHandler.selectedTile.switchHighlight()
                    self.animations.queue(self.pieceHandler.makeAnimation())
                    self.pieceHandler.reset()
                    self.tileHandler.reset()
                    self.match.gameState = GameState.CHOOSE_PIECE
                    self.match.switchTurn()
                    return
                except PieceHandlerException as e:
                    self.pieceHandler.reset()
                    self.tileHandler.reset()
                    self.match.gameState = GameState.CHOOSE_PIECE
                    return

    def quitEvent(self):
        pygame.quit()
        quit()

    def update(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quitEvent()
                case pygame.MOUSEBUTTONDOWN:
                    self.clickEvent(event)

        self.animations.execute()
        self.gameObjects.draw()