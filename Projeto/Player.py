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
        self.x = 150
        self.y = 393
        self.width = 49
        self.height = 47
        self.runCount = 0
        self.jumping = False
        self.vel = 15
        self.jumpCount = 0
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def updateHitbox(self):
        # hitbox(left, top, width, height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
                 
    def updatePlayer(self):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.8
            self.jumpCount += 1
            if self.jumpCount > 99:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        self.updateHitbox()

    def draw(self, win):
        self.updatePlayer()
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.run, (self.x, self.y))