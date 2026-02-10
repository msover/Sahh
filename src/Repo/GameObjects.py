import os

import pygame
from pygame import Surface

from src.Data.Enums.Visual.Color import Color
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.Board.Tile import Tile
from src.Data.GameObjects.GameObject import GameObject
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.GameObjects.Pieces.Set.Horse import Horse
from src.Data.GameObjects.Pieces.Set.King import King
from src.Data.GameObjects.Pieces.Set.Pawn import Pawn
from src.Data.GameObjects.Pieces.Set.Queen import Queen
from src.Data.GameObjects.Pieces.Set.Rook import Rook
from src.Data.GameObjects.Pieces.Set.Bishop import Bishop
from src.Data.Enums.Position.File import File
from src.Data.Position.Position import Position
from src.Data.Enums.Position.Rank import Rank
from src.Repo.TextRepo import TextRepo


class GameObjects:
    def __init__(self):
        self._sprites = pygame.sprite.LayeredUpdates()
        self._pieces: list[Piece] = []
        self._tiles: list[Tile] = []
        self.initPieces(TextRepo(os.path.join("src", "Assets", "PieceLayout.txt")).getData())
        self.initTiles(TextRepo(os.path.join("src", "Assets", "TileLayout.txt")).getData())

    def add(self, gameObject: GameObject):
        if isinstance(gameObject, Tile):
            self._tiles.append(gameObject)
        if isinstance(gameObject, Piece):
            self._pieces.append(gameObject)
        self._sprites.add(gameObject)

    def remove(self, gameObject: GameObject):
        if isinstance(gameObject, Tile):
            self._tiles.remove(gameObject)
        if isinstance(gameObject, Piece):
            self._pieces.remove(gameObject)
        self._sprites.remove(gameObject)


    def movePiece(self, newPosition: Position):
        self._pieces[0].position = newPosition

    def createPiece(self, gameObject: GameObject):
        match gameObject.objectType:
            case ObjectType.ROOK:
                return Rook(gameObject.color, gameObject.position)
            case ObjectType.HORSE:
                return Horse(gameObject.color, gameObject.position)
            case ObjectType.BISHOP:
                return Bishop(gameObject.color, gameObject.position)
            case ObjectType.QUEEN:
                return Queen(gameObject.color, gameObject.position)
            case ObjectType.KING:
                return King(gameObject.color, gameObject.position)
            case ObjectType.PAWN:
                return Pawn(gameObject.color, gameObject.position)
            case _:
                return gameObject

    def getPieceAtPosition(self, position: Position) -> Piece:
        for piece in self._pieces:
            if piece.position == position:
                return piece
        return Piece(Color.NaN, ObjectType.EMPTY, Position(File.NaN, Rank.NaN))

    def getTileAtPosition(self, position: Position) -> Tile:
        for tile in self._tiles:
            if tile.position == position:
                return tile
        return Tile(Color.NaN, Position(File.NaN, Rank.NaN))

    def initPieces(self, layout):
        for row in range(8):
            for col in range(8):
                spriteType = ObjectType.match(layout[row][col])
                if spriteType == ObjectType.EMPTY:
                    continue

                pos = Position(File.matchIndex(col), Rank.matchIndex(row))
                color = Color.WHITE
                if row < 4:
                    color = Color.BLACK
                gameObject = GameObject(color, spriteType, pos)
                self.add(self.createPiece(gameObject))

    def initTiles(self, layout):
        for row in range(8):
            for col in range(8):
                color = Color.match(layout[row][col])
                pos = Position(File.matchIndex(col), Rank.matchIndex(row))
                self.add(Tile(color, pos))

    def updatePieces(self, surface: Surface):
        for piece in self._pieces:
            self._sprites.change_layer(piece, piece.layer)
        self._sprites.draw(surface)