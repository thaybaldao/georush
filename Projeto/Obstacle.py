import pygame
from math import *
from pygame.locals import *
import os

class Obstacle:
    def __init__(self, x, y, width, height, img, type, num):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img = img
        self.type = type
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.num = num

    def draw(self, win):
        self.updateHitbox()
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def updateHitbox(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def identifyObstacleType(self):
        return self.type;


