import pygame
from pygame.locals import *
from Obstacles import *
from Settings import *
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
            if obstacle != 0 and self.rect.colliderect(obstacle):
                if obstacle.type == 'rectangle' and self.vel.y > 0 and self.pos.y - TOLERANCE <= obstacle.rect.top:
                    self.pos.y = obstacle.rect.top
                    self.vel.y = 0
                    self.obstacleOnTop = obstacle
                elif int(game.invincible) == 0:
                    if game.numLives == 0:
                        game.lives.clear()
                        game.obstacles.clear()
                        game.lifebar.clear()
                        if game.sound:
                            pygame.mixer.music.fadeout(300)
                        game.resetScreen.showScreen(game)
                        if game.playing:
                            game.playing = False
                        game.running = False
                    else:
                        game.numLives -= 1
                        game.lifebar.pop()
                        game.obstacles.clear()
                        game.lives.clear()
                        game.boost.clear()
            for life in game.lives:
                if game.runner.rect.colliderect(life):
                    game.numLives += 1
                    n = 46 * (game.numLives - 1)
                    game.lifebar.append(
                        Obstacle(25 + n, 25, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                    game.lives.pop(game.lives.index(life))

            for boost in game.boost:
                if game.runner.rect.colliderect(boost):
                    game.invincible = 15
                    game.boost.pop(game.boost.index(boost))


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
            self.image = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel.png'))
        else: self.image = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal.png'))


    def draw(self, win):
        # pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        win.blit(self.image, (self.rect.left, self.rect.top))
