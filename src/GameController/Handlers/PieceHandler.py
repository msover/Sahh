from src.Data.Enums.Color import Color
from src.Data.Enums.ObjectType import ObjectType
from src.Data.Exceptions.PieceHandlerException import PieceHandlerException
from src.Data.GameObjects.Board.PossibleMove import PossibleMove
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Enums.File import File
from src.Data.GameObjects.Pieces.Set.Rook import Rook
from src.Data.Position.Position import Position
from src.Data.Enums.Rank import Rank
from src.GameController.Animation.Animation import Animation
from src.Repo.GameObjects import GameObjects
from src.Repo.MatchRepo import MatchRepo


class PieceHandler:
    def __init__(self, match: MatchRepo, gameObjects: GameObjects):
        self._gameObjects = gameObjects
        self._match = match
        self._selectedPiece = Piece(Color.NaN, ObjectType.EMPTY, Position(File.NaN, Rank.NaN))
        self._targetPosition = Position(File.NaN, Rank.NaN)
        self._moveset: list[Position] = []

    def reset(self):
        self._gameObjects.wipePossibleMoves()
        self._selectedPiece = Piece(Color.NaN, ObjectType.EMPTY, Position(File.NaN, Rank.NaN))
        self._targetPosition = Position(File.NaN, Rank.NaN)
        self._moveset = []

    def makeAnimation(self):
        return Animation(self._selectedPiece, self._targetPosition)

    @property
    def selectedPiece(self):
        return self._selectedPiece

    @property
    def targetPosition(self):
        return self._targetPosition

    @selectedPiece.setter
    def selectedPiece(self, selectedPiece: Piece):
        if selectedPiece.color != self._match.turn:
            raise PieceHandlerException("Chosen piece does not belong to the player")
        if selectedPiece.objectType == ObjectType.EMPTY:
            raise PieceHandlerException("Chosen piece does not exist")
        self._selectedPiece = selectedPiece
        self.pruneMoveset()

    @targetPosition.setter
    def targetPosition(self, targetPosition: Position):
        if targetPosition not in self._moveset:
            raise PieceHandlerException("Can't move there")
        pieceAtPosition = self._gameObjects.getPieceAtPosition(targetPosition)
        if pieceAtPosition.color == self._match.turn and pieceAtPosition.objectType != ObjectType.EMPTY:
            raise PieceHandlerException("Can't overlap your own piece")
        self._targetPosition = targetPosition

    def pruneMoveset(self):

        moveset = self._selectedPiece.moveset()
        for branch in moveset:
            for move in branch:
                piece = self._gameObjects.getPieceAtPosition(move)
                if piece.color == self._match.turn and piece.objectType != ObjectType.EMPTY:
                    break
                self._gameObjects.add(PossibleMove(move))
                self._moveset.append(move)
                if piece.objectType != ObjectType.EMPTY:
                    break