from src.Data.Enums.Position.Rank import Rank
from src.Data.Enums.Visual.Color import Color
from src.Data.GameObjects.Pieces.Set.Pawn import Pawn
from src.GameController.GameController import GameController
from src.UI.Display.DisplayWindow import DisplayWindow

gameController = GameController()
DisplayWindow()
while True:
    gameController.update()