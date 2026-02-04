import pygame

from src.Data.Enums.Color import Color
from src.Data.Enums.PieceType import PieceType
from src.Data.Piece.Position import Position
from src.UI.Display.DisplayWindow import DisplayWindow


class Piece(pygame.sprite.Sprite):
    def __init__(self, color: Color, pieceType: PieceType, position: Position):
        super().__init__()
        self._color = color
        self._pieceType = pieceType
        self._position = position
        self._image = pygame.image.load(f"src\\Assets\\{color.value}_{pieceType.value}.png")
        self._image = pygame.transform.smoothscale(self._image, DisplayWindow().getPieceScale())
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._position.file.value, self._position.rank.value)

    def moveset(self) -> list[Position]:
        pass