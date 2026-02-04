import pygame
import os
from src.Data.Enums.Color import Color
from src.Data.Enums.Layer import Layer
from src.Data.Enums.ObjectType import ObjectType
from src.Data.GameObjects.GameObject import GameObject
from src.Data.Position.Position import Position
from src.UI.Display.DisplayWindow import DisplayWindow


class Board(GameObject):
    def __init__(self, color: Color, objectType: ObjectType, position: Position):
        super().__init__(color, objectType, position)

        self._layer = Layer.TILE.value
        self._scale = (DisplayWindow().getTileScalingFactor(), DisplayWindow().getTileScalingFactor())
        if self.objectType != ObjectType.EMPTY:
            self.makeSprite()


    def makeSprite(self):

        path = os.path.join("src", "Assets", "PNGs", f"{self.color.value}{self.objectType.value}.png")
        self._image = pygame.image.load(path)
        self._image = pygame.transform.smoothscale(self._image, self._scale)
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._position.file.value, self._position.rank.value)

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: Color):
        self._color = color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: Position):
        self._position = position

    @property
    def objectType(self):
        return self._objectType

    @objectType.setter
    def objectType(self, spriteType: ObjectType):
        self._objectType = spriteType