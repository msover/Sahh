import pygame

class DisplayWindow:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, width = None, height = None, name = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self._width = width
            self._height = height
            self._name = name
            self._screen = pygame.display.set_mode((self._width, self._height))
            pygame.display.set_caption(self._name)

    def clear(self):
        self._screen.fill((0, 0, 0))

    def update(self):
        pygame.display.flip()

    def getSurface(self) -> pygame.Surface:
        return self._screen

    def getPieceScale(self) -> tuple[float, float]:
        #return self._width / 8, self._height / 8
        return 100, 100