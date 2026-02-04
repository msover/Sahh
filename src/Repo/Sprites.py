import pygame

from src.Data.Piece.Piece import Piece
from src.UI.Display.DisplayWindow import DisplayWindow


class Sprites:
    def __init__(self):
        self._sprites = pygame.sprite.Group()

    def addPiece(self, piece: Piece):
        self._sprites.add(piece)
    def removePiece(self, piece: Piece):
        self._sprites.remove(piece)

    def draw(self):
        self._sprites.draw(DisplayWindow().getSurface())
        DisplayWindow().update()