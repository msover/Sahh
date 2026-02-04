from src.GameController.GameController import GameController
from src.UI.Display.DisplayWindow import DisplayWindow

gameController = GameController()
DisplayWindow()
while True:
    gameController.update()

