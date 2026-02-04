import pygame.sprite

from src.Data.Enums.Color import Color
from src.Data.Position.Rank import Rank
from src.Data.Enums.SpriteType import SpriteType
from src.Data.Position.File import File
from src.Data.GameObjects.GameObject import GameObject
from src.Data.Position.Position import Position
from src.Repo.GameObjects import GameObjects




sprites = GameObjects()
#piece = GameObject(Color.WHITE, SpriteType.BISHOP, Position(File.A, Rank.ONE))
square = GameObject(Color.match(0), SpriteType.TILE, Position(File.A, Rank.ONE))
#sprites.addGameObject(piece)
#sprites.add(square)
sprites.setTiles()
sprites.draw()



while True:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                quit()