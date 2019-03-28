from Obstacle import *
import os
import pygame
from pygame.locals import *

class Platform(Obstacle):
    def __init__(self):
        super().__init__(810, 300, 526, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle')

    def collisionStatus(self, rect):
        if self.hitbox.colliderect(rect):
            if self.type == 'triangle':
                return 'death'
            else:
                x = self.hitbox.centerx - rect.centerx
                y = rect.centerx - self.hitbox.centerx
                collisionAngle = atan2(y, x)
                maxLateralCollisionAngle = atan2(self.hitbox.height + rect.height,
                                                 self.hitbox.width + rect.width)

                if collisionAngle > maxLateralCollisionAngle and collisionAngle < pi - maxLateralCollisionAngle:
                    return 'continue'

                return 'death'