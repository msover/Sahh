import pygame

from src.Data.Enums.Visual.Color import Color
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.Position.Position import Position


class GameObject(pygame.sprite.Sprite):
    def __init__(self, color: Color, objectType: ObjectType, position: Position):
        super().__init__()
        self._color = color
        self._objectType = objectType
        self._position = position
        self._image = None
        self._rect = None
        self._scale = None
        self._displacement = None

    def makeSprite(self):
        pass

    def __str__(self):
        return f"{self._color.name}, {self._objectType.name}, {self._position}"

    def __repr__(self):
        return self.__str__()

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @property
    def objectType(self):
        return self._objectType

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    @image.setter
    def image(self, image: pygame.Surface):
        self._image = image

    @rect.setter
    def rect(self, rect: pygame.Rect):
        self._rect = rect

    @color.setter
    def color(self, color: Color):
        self._color = color

    @position.setter
    def position(self, position: Position):
        self._position = position

    @objectType.setter
    def objectType(self, spriteType: ObjectType):
        self._objectType = spriteType