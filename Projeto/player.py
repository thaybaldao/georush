import pygame
from pygame.locals import *
import os

class Player:
    run = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0

    def draw(self, win):
        if self.runCount > 42:
            self.runCount = 0
        win.blit(self.run, (self.x, self.y))
        self.runCount += 1
