import pygame.sprite


from src.Data.Enums.Color import Color
from src.Data.Enums.File import File
from src.Data.Enums.PieceType import PieceType
from src.Data.Enums.Rank import Rank
from src.Data.Piece.Piece import Piece
from src.Data.Piece.Position import Position
from src.Repo.Sprites import Sprites
from src.UI.Display.DisplayWindow import DisplayWindow

DisplayWindow(1600, 800, "Chesss")

sprites = Sprites()
position = Position(Rank.A, File.TWO)
piece = Piece(Color.WHITE, PieceType.KING, position)
sprites.addPiece(piece)
sprites.draw()



while True:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                quit()