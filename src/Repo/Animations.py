from src.Data.Enums.File import File
from src.Data.Enums.Rank import Rank
from src.GameController.Animation.Animation import Animation


class Animations:
    def __init__(self):
        self._animations: list[Animation] = []

    def queue(self, animation: Animation):
        if animation.targetPos.rank == Rank.NaN or animation.targetPos.file == File.NaN:
            return
        self._animations.append(animation)

    def isEmpty(self) -> bool:
        return len(self._animations) == 0

    def execute(self):
        if not len(self._animations):
            return
        animation = self._animations[-1]
        completionStatus = animation.execute()
        if completionStatus:
            self._animations.pop(-1)
