import os

import pygame

from src.Data.Enums.Color import Color
from src.Data.Enums.Layer import Layer
from src.Data.Enums.ObjectType import ObjectType
from src.Data.GameObjects.GameObject import GameObject
from src.Data.Position.Position import Position
from src.UI.Display.DisplayWindow import DisplayWindow


class PossibleMove(GameObject):
    def __init__(self, position: Position):
        super().__init__(Color.BLACK,ObjectType.POSSIBLE_MOVE, position)
        self._layer = Layer.POSSIBLE_MOVE.value
        self._scale = (DisplayWindow().getPossibleMoveScalingFactor(), DisplayWindow().getPossibleMoveScalingFactor())
        self._displacement = (DisplayWindow().getTileScalingFactor() - DisplayWindow().getPossibleMoveScalingFactor()) / 2
        self.makeSprite()

    def makeSprite(self):
        path = os.path.join("src", "Assets", "PNGs", "pm.png")
        self._image = pygame.image.load(path)
        self._image = pygame.transform.smoothscale(self._image, self._scale)
        self._rect = self._image.get_rect()
        self._rect.topleft = (self._position.file.value + self._displacement, self._position.rank.value + self._displacement)