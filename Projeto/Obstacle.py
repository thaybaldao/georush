import pygame
from math import *
from pygame.locals import *
import os

class Obstacle:
    def __init__(self, x, y, width, height, img, type):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img = img
        self.type = type
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.updateHitbox()
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def updateHitbox(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def identifyObstacleType(self):
        return self.type;

    def collisionStatus(self, rect):
        if self.hitbox.colliderect(rect):
            if self.type == 'triangle':
                return 'death'
            else:
                x = self.hitbox.centerx - rect.centerx
                y = rect.centerx - self.hitbox.centerx
                collisionAngle = atan2(y, x)
                maxLateralCollisionAngle = atan2(self.hitbox.height + rect.height, self.hitbox.width + rect.width)

                if collisionAngle > maxLateralCollisionAngle and collisionAngle < pi - maxLateralCollisionAngle:
                    return 'continue'

                return 'death'
