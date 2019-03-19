import pygame
from pygame.locals import *
import os

class Player:
    run = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0
        self.jumping = False
        self.running = False
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
        elif self.running:
            self.x += self.vel;
            win.blit(self.run, (self.x, self.y))
            self.running = False
        else:
            win.blit(self.run, (self.x, self.y))

