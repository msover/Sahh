from src.Data.Enums.Movement.Direction import Direction
from src.Data.Enums.Movement.UniversalMoveset import UniversalMoveset
from src.Data.Enums.Visual.Color import Color
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.Exceptions.PieceHandlerException import PieceHandlerException
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Enums.Position.File import File
from src.Data.Position.Position import Position
from src.Data.Enums.Position.Rank import Rank
from src.GameController.Animation.Animation import Animation
from src.Repo.GameObjects import GameObjects
from src.Repo.MatchRepo import MatchRepo


class PieceHandler:
    def __init__(self, match: MatchRepo, gameObjects: GameObjects):
        self._moveset = None
        self._gameObjects = gameObjects
        self._match = match
        self._selectedPiece = Piece(Color.NaN, ObjectType.EMPTY, Position(File.NaN, Rank.NaN))
        self._targetPosition = Position(File.NaN, Rank.NaN)

    def pruneMoveset(self) -> list[Position]:
        movesetOptions = self._selectedPiece.moveset()
        moveset: list[Position] = []
        if self._selectedPiece.objectType == ObjectType.HORSE:
            moveset.extend(self.pruneHorse(movesetOptions))
        else:
            moveset.extend(self.pruneNormal(movesetOptions))

        print(moveset)
        return moveset

    def pruneNormal(self, movesetOptions: list[MovesetOption]) -> list[Position]:
        startPos = self._selectedPiece.position
        moves: list[Position] = []
        for option in movesetOptions:
            if option.moveset == UniversalMoveset.RANK:
                moves.extend(self.processRank(startPos, option))
            if option.moveset == UniversalMoveset.FILE:
                moves.extend(self.processFile(startPos, option))
        return moves

    def processRank(self, startPos: Position, option: MovesetOption) -> list[Position]:
        moves: list[Position]=  []
        stepsTaken = 0
        iterator = Rank
        if option.direction == Direction.DOWN:
            iterator = reversed(Rank)
        for rank in iterator:
            if stepsTaken >= option.restriction:
                return moves
            stepsTaken += 1
            currentPosition = Position(startPos.file, rank)
            pieceAtPosition = self._gameObjects.getPieceAtPosition(currentPosition)
            if pieceAtPosition.color != Color.NaN:
                if pieceAtPosition.objectType.color == self._match.turnColor:
                    print(f"enemy piece {pieceAtPosition}")
                    return moves
                elif pieceAtPosition.objectType.color != self._match.turnColor:
                    print(f"self piece {pieceAtPosition}")
                    moves.append(currentPosition)
                    return moves
            moves.append(currentPosition)
        return moves


    def processFile(self, startPos: Position, option: MovesetOption) -> list[Position]:
        pass

    def pruneHorse(self, movesetOptions: list[MovesetOption]) -> list[Position]:
        pass

    def reset(self):
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
        if selectedPiece.color != self._match.turnColor:
            raise PieceHandlerException("Chosen piece does not belong to the player")
        if selectedPiece.objectType == ObjectType.EMPTY:
            raise PieceHandlerException("Chosen piece does not exist")
        self._selectedPiece = selectedPiece
        self._moveset = self.pruneMoveset()


    @targetPosition.setter
    def targetPosition(self, targetPosition: Position):
        if targetPosition not in self._moveset:
            raise PieceHandlerException("Can't move there")
        pieceAtPosition = self._gameObjects.getPieceAtPosition(targetPosition)
        if pieceAtPosition.color == self._match.turnColor and pieceAtPosition.objectType != ObjectType.EMPTY:
            raise PieceHandlerException("Can't overlap your own piece")
        self._targetPosition = targetPosition