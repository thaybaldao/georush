import pygame
from pygame.locals import *
import os

class Obstacle_1:
    img = pygame.image.load(os.path.join('Imagens','Triangulo.png'))
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
