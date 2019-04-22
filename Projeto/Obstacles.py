import pygame
from math import *
from pygame.locals import *
import os
import random

class Obstacle:
    def __init__(self, x, y, width, height, img, type, num):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img = img
        self.type = type
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.num = num
        if(self.num == 0):
            self.speedDangerZone = 1.4 + 0.2*random.randrange(8, 9)
        elif(self.num == 1):
            self.speedDangerZone = 1.4 + 0.2 * random.randrange(6, 7)
        else:
            self.speedDangerZone = 1.4 + 0.2 * random.randrange(5, 6)

    def update(self, inDangerZone):
        if self.x > -850:
            if inDangerZone:
                self.x -= self.speedDangerZone
            else:
                self.x -= 1.4
        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self, win):
        # pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        win.blit(self.img, (self.x, self.y))

    def identifyObstacleType(self):
        return self.type


