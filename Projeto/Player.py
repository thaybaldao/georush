import pygame
from pygame.locals import *
from Settings import *
import os
vec = pygame.math.Vector2

class Player():
    def __init__(self, game):
        self.x = 150
        self.y = 393
        self.width = 49
        self.height = 47
        self.runCount = 0
        self.game = game
        self.image = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.obstacleOnTop = 0

    def jump(self):
        # jump only if standing on a platform
        self.rect.center = (self.rect.centerx, self.rect.centery + 1)

        if self.pos.y != BOTTOM_Y and self.rect.colliderect(self.obstacleOnTop.rect):
            self.rect.center = (self.rect.centerx, self.rect.centery - 1)
            self.vel.y = PLAYER_INITIAL_VEL
        else:
            self.rect.center = (self.rect.centerx, self.rect.centery - 1)

        if self.pos.y == BOTTOM_Y:
            self.vel.y = PLAYER_INITIAL_VEL

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        win.blit(self.image, (self.rect.left, self.rect.top))