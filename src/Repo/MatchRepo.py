from src.Data.Enums.Color import Color
from src.Data.Enums.GameState import GameState


class MatchRepo:
    def __init__(self):
        self.turn = Color.WHITE
        self.gameState = GameState.CHOOSE_PIECE
        self.whiteState = GameState.IDLE
        self.blackState = GameState.IDLE

    def switchTurn(self):
        match self.turn:
            case Color.WHITE:
                self.turn = Color.BLACK
                return
            case Color.BLACK:
                self.turn = Color.WHITE
                return