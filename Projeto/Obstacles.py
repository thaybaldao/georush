import pygame
import random
from Settings import *
from GameState import *
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
        win.blit(self.img, (self.x, self.y))

    def identifyObstacleType(self):
        return self.type

    def checkCollisions(self, game):
        pass


class RectObs(Obstacle):
    def __init__(self, x, y, width, height, img, num):
        super().__init__(x,y,width,height,img,'rectangle',num)

    def checkCollisions(self, game):
        if game.runner.rect.colliderect(self):
            if game.runner.vel.y > 0 and game.runner.pos.y - TOLERANCE <= self.rect.top:
                game.runner.pos.y = self.rect.top
                game.runner.vel.y = 0
                game.runner.obstacleOnTop = self
            elif not GameState().invincible(game):
                if GameState().haveExtraLives(game):
                    game.numLives -= 1
                    game.lifebar.pop()
                    game.obstacles.clear()
                    game.lives.clear()
                    game.boost.clear()
                else:
                    if game.sound:
                        game.soundManager.playDeath(os.path.join('Music', 'death.wav'))
                        pygame.time.wait(3100)
                    game.lives.clear()
                    game.obstacles.clear()
                    game.lifebar.clear()
                    game.resetScreen.run(game)
                    if game.playing:
                        game.playing = False

class TriObs(Obstacle):
    def __init__(self, x, y, width, height, img, num):
        super().__init__(x,y,width,height,img,'triangle',num)
        self.speedDangerZone()

    def speedDangerZone(self):
        if (self.num == 0):
            self.speedDangerZone = 1.4 + 0.2 * random.randrange(9, 10)
        elif (self.num == 1):
            self.speedDangerZone = 1.4 + 0.2 * random.randrange(7, 8)
        else:
            self.speedDangerZone = 1.4 + 0.2 * random.randrange(6, 7)

    def update(self, inDangerZone):
        if self.x > -850:
            if inDangerZone:
                self.x -= self.speedDangerZone
            else:
                self.x -= 1.4
        self.rect.x = self.x
        self.rect.y = self.y

    def checkCollisions(self, game):
        if game.runner.rect.colliderect(self) and not GameState().invincible(game):
            if GameState().haveExtraLives(game):
                game.numLives -= 1
                game.lifebar.pop()
                game.obstacles.clear()
                game.lives.clear()
                game.boost.clear()
            else:
                if game.sound:
                    game.soundManager.playDeath(os.path.join('Music', 'death.wav'))
                    pygame.time.wait(3100)
                game.lives.clear()
                game.obstacles.clear()
                game.lifebar.clear()
                game.resetScreen.run(game)
                if game.playing:
                    game.playing = False


class Life(Obstacle):
    def __init__(self, x, y):
        super().__init__(x,y,46,39,pygame.image.load(os.path.join('Imagens', 'Vida.png')),'life','x')

    def checkCollisions(self, game):
        if game.runner.rect.colliderect(self):
            game.numLives += 1
            if game.sound:
                game.soundManager.playSoundEffect(os.path.join('Music', 'life.wav'))
            n = 46 * (game.numLives - 1)
            game.lifebar.append(Life(25 + n, 25))
            game.lives.pop(game.lives.index(self))


class Boost(Obstacle):
    def __init__(self, x, y):
        super().__init__(x,y,46,39,pygame.image.load(os.path.join('Imagens', 'Star.png')),'boost','x')

    def checkCollisions(self, game):
        if game.runner.rect.colliderect(self):
            if game.sound:
                game.soundManager.playSoundEffect(os.path.join('Music', 'boost.wav'))
            game.invincible = 19
            game.boost.pop(game.boost.index(self))
