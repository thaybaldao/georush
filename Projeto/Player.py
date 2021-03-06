import pygame
from Settings import *
from Obstacles import *
import os
vec = pygame.math.Vector2

class Player():
    def __init__(self, game):
        self.x = 150
        self.y = 200
        self.width = 49
        self.height = 47
        self.runCount = 0
        self.game = game
        self.image = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, PLAYER_GRAV)
        self.obstacleOnTop = 0

    def jump(self):
        # jump only if standing on a platform
        self.rect.center = (self.rect.centerx, self.rect.centery + 1)

        if self.obstacleOnTop != 0 and self.pos.y != BOTTOM_Y and self.rect.colliderect(self.obstacleOnTop.rect):
            self.rect.center = (self.rect.centerx, self.rect.centery - 1)
            self.vel.y = PLAYER_INITIAL_VEL
        else:
            self.rect.center = (self.rect.centerx, self.rect.centery - 1)

        if self.pos.y == BOTTOM_Y:
            self.vel.y = PLAYER_INITIAL_VEL

    def checkCollisions(self, game):
        for obstacle in game.obstacles:
            obstacle.checkCollisions(game)

        for life in game.lives:
            life.checkCollisions(game)

        for boost in game.boost:
            boost.checkCollisions(game)


    def update(self, game):
        # equations of motion
        dt = game.initialSpeed*0.8/game.speed

        self.vel += self.acc*dt
        self.pos += self.vel*dt

        self.rect.midbottom = self.pos

        if self.pos.y >= BOTTOM_Y:
            self.pos.y = BOTTOM_Y
            self.vel.y = 0

        self.checkCollisions(game)

        if game.invincible > 0:
            game.invincible = game.invincible - 0.01

            if game.invincible > 4:
                self.image = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel.png'))

            else: self.image = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal.png'))


    def draw(self, win):
        win.blit(self.image, (self.rect.left, self.rect.top))
