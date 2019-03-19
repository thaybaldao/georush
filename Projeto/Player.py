import pygame
from pygame.locals import *
import os

class Player:
    run = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]
    def __init__(self):
        self.x = 30
        self.y = 393
        self.width = 49
        self.height = 47
        self.runCount = 0
        self.jumping = False
        self.vel = 15
        self.jumpCount = 0

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            self.x += self.vel/25
            win.blit(self.run, (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 99:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        else:
            win.blit(self.run, (self.x, self.y))