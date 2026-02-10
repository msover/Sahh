from src.Data.Enums.Visual.Color import Color
from src.Data.Enums.GameState import GameState


class MatchRepo:
    def __init__(self):
        self.turnColor = Color.WHITE
        self.gameState = GameState.CHOOSE_PIECE
        self.whiteState = GameState.IDLE
        self.blackState = GameState.IDLE

    def switchTurn(self):
        match self.turnColor:
            case Color.WHITE:
                self.turnColor = Color.BLACK
                return
            case Color.BLACK:
                self.turnColor = Color.WHITE
                return