import pygame

from src.Data.Enums.AnimationStatus import AnimationStatus
from src.Data.Enums.Layer import Layer
from src.Data.GameObjects.Pieces.Piece import Piece
from src.Data.Position.Position import Position
from src.Repo.MatchRepo import MatchRepo


class Animation:
    def __init__(self, piece: Piece, targetPos: Position):
        self.piece = piece
        self.targetPos = targetPos
        self.vectorialCurrentPos = pygame.math.Vector2(piece.rect.topleft)
        self.displacement = self.piece.displacement
        self.vectorialTargetPos = self.makeVectorialTargetPos()
        self.clock = None
        self.animationStatus = AnimationStatus.INIT

        totalDistance = (self.vectorialTargetPos - self.vectorialCurrentPos).length()
        desiredDuration = 0.15
        self.speed = max(totalDistance / desiredDuration, 1)

    def makeVectorialTargetPos(self):
        target_x_pixels = self.targetPos.file.value
        target_y_pixels = self.targetPos.rank.value
        return pygame.math.Vector2(target_x_pixels + self.displacement, target_y_pixels + self.displacement)

    def init(self):
        self.piece.layer = Layer.MOVING_PIECE.value
        self.piece.position = self.targetPos
        self.piece.rect.topleft = (int(self.vectorialCurrentPos.x), int(self.vectorialCurrentPos.y))
        self.clock = pygame.time.Clock()

    def run(self):
        timeDelta = self.clock.tick(360) / 1000.0
        direction = self.vectorialTargetPos - self.vectorialCurrentPos
        distance = direction.length()
        if distance < self.speed * timeDelta:
            self.vectorialCurrentPos = self.vectorialTargetPos
            self.piece.position = self.targetPos
            return False
        else:
            direction = direction.normalize()
            self.vectorialCurrentPos += direction * self.speed * timeDelta
            self.piece.rect.topleft = (int(self.vectorialCurrentPos.x), int(self.vectorialCurrentPos.y))
            return True

    def finished(self):
        self.piece.layer = Layer.STATIC_PIECE.value

    def execute(self) -> bool:
        match self.animationStatus:
            case AnimationStatus.INIT:
                self.init()
                self.animationStatus = AnimationStatus.RUNNING
            case AnimationStatus.RUNNING:
                if not self.run():
                    self.animationStatus = AnimationStatus.FINISHED
            case AnimationStatus.FINISHED:
                self.finished()
                return True
        return False



