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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.num = num

    def update(self):
        if self.x > -850:
            self.x -= 1.4
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, win):
        # pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        win.blit(self.img, (self.x, self.y))

    def identifyObstacleType(self):
        return self.type


