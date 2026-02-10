import os

import pygame

from src.Data.Enums.Visual.Color import Color
from src.Data.Enums.Visual.Layer import Layer
from src.Data.Enums.Visual.ObjectType import ObjectType
from src.Data.GameObjects.GameObject import GameObject
from src.Data.GameObjects.MovesetOption import MovesetOption
from src.Data.Position.Position import Position
from src.UI.Display.DisplayConstants import DisplayConstants


class Piece(GameObject):
    def __init__(self, color: Color, objectType: ObjectType, position: Position):
        super().__init__(color, objectType, position)

        self._layer = Layer.STATIC_PIECE.value


        self._scale = (DisplayConstants.PIECE_SCALING_FACTOR, DisplayConstants.PIECE_SCALING_FACTOR)
        self._displacement = (DisplayConstants.TILE_SCALING_FACTOR - DisplayConstants.TILE_SCALING_FACTOR) / 2
        if self.objectType != ObjectType.EMPTY:
            self.makeSprite()

    def makeSprite(self):
        path = os.path.join("src", "Assets", "PNGs", f"{self.color.value}{self.objectType.value}.png")
        self._image = pygame.image.load(path)
        self._image = pygame.transform.smoothscale(self._image, self._scale)
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._position.file.value + self._displacement,
                              self._position.rank.value + self._displacement)

    def moveset(self) -> list[MovesetOption]:
        pass

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect):
        self._rect = rect

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
        self._rect.topleft = (self._position.file.value + self._displacement, self._position.rank.value + self._displacement)

    @property
    def displacement(self):
        return self._displacement

    @property
    def objectType(self):
        return self._objectType

    @objectType.setter
    def objectType(self, spriteType: ObjectType):
        self._objectType = spriteType

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, layer: Layer):
        self._layer = layer