import pygame

from src.UI.Display.DisplayConstants import DisplayConstants


class DisplayWindow:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, width = DisplayConstants.SCREEN_WIDTH, height = DisplayConstants.SCREEN_HEIGHT, name = DisplayConstants.SCREEN_TITLE):
        if not hasattr(self, "_initialized"):
            self._gameObjects = None
            self._initialized = True
            self._width = width
            self._height = height
            self._name = name
            pygame.display.set_caption(self._name)
            self._screen = pygame.display.set_mode((self._width, self._height))

    def setGameObjects(self, gameObjects):
        self._gameObjects = gameObjects

    def update(self):
        self._gameObjects.updatePieces(self._screen)
        pygame.display.flip()

