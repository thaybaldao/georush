import pygame
from pygame.locals import *
from Settings import *
import os
vec = pygame.math.Vector2

class Player():
    def __init__(self, game):
        self.x = 150
        self.y = BOTTOM_Y
        self.width = 49
        self.height = 47
        self.runCount = 0
        self.game = game
        self.image = pygame.image.load(os.path.join('Imagens','Personagem_Principal.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.obstacleOnTop = 0
        self.timeJumpStarted = 0
        self.isJumping = False
        self.lastY = BOTTOM_Y

    def jump(self):
        if self.isJumping == False:
            self.rect.center = (self.rect.centerx, self.rect.centery - 1)
            self.timeJumpStarted = pygame.time.get_ticks()/1000
            self.isJumping = True

    def checkCollisions(self, game):
        for obstacle in game.obstacles:
            obstacle.update()
            if self.rect.colliderect(obstacle):
                if obstacle.type == 'rectangle' and self.isJumping == True and self.lastY < self.y:
                    self.y = obstacle.rect.top
                    self.obstacleOnTop = obstacle
                    self.isJumping = False
                else:
                    self.obstacleOnTop = 0
                    if game.playing:
                        game.playing = False
                    game.running = False

    def update(self, game):
        if self.isJumping:
            if self.y <= BOTTOM_Y:
                dt = (pygame.time.get_ticks()/1000 - self.timeJumpStarted)
                self.y = self.y - PLAYER_INITIAL_VEL*dt + PLAYER_GRAV*dt*dt/2
            else:
                self.y = BOTTOM_Y
                self.isJumping = False

        self.checkCollisions(game)

        self.rect.center = (self.x, self.y)

        self.lastY = self.y

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        win.blit(self.image, (self.rect.left, self.rect.top))