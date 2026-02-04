import pygame

from src.Data.Enums.Color import Color
from src.Data.Enums.Layer import Layer
from src.Data.Enums.SpriteType import SpriteType
from src.Data.Position.Position import Position
from src.UI.Display.DisplayWindow import DisplayWindow


class GameObject(pygame.sprite.Sprite):
    def __init__(self, color: Color, spriteType: SpriteType, position: Position):
        super().__init__()
        self._color = color
        self._spriteType = spriteType
        self._position = position

        self._layer = Layer.DEFAULT.value

        self._image = pygame.image.load(f"src\\Assets\\{color.value}_{spriteType.value}.png")
        pieceScale = (DisplayWindow().getScalingFactor(), DisplayWindow().getScalingFactor())
        self._image = pygame.transform.smoothscale(self._image, pieceScale)
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._position.file.value, self._position.rank.value)

    @property
    def image(self):
        return self._image
    @property
    def rect(self):
        return self._rect

    def moveset(self) -> list[Position]:
        pass