from Obstacles import *
from Settings import *
from Screen import *
import pygame
from pygame.locals import *
import os
from SoundBehavior import*

class Zone(Screen):
    def __init__(self):
        pass


    def computeScore(self, game):
        game.score += 0.01


    def createObstacle(self, game):
        pass


    def basicZoneUpdate(self, game):
        self.basicScreenUpdate(game)

        # making obstacles disappear
        for obstacle in game.obstacles:
            if obstacle.type == 'triangle':
                obstacle.update(game.inDangerZone)
            else:
                obstacle.update()
            if obstacle.x < -850:
                game.obstacles.pop(game.obstacles.index(obstacle))


    def printScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        score = font.render("Score: " + str(int(game.score)), True, ORANGE)
        self.screen.blit(score, (265, 10))


    def printInvTime(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 25)
        text = font.render("Invincible Time: " + str(int(game.invincible) - 4), True, PURPLE)
        self.screen.blit(text, (10, 455))


    def basicZoneDraw(self, game):
        self.drawBasicScreen(game)

        # draw obstacles
        for obstacle in game.obstacles:
            obstacle.draw(self.screen)

        # draw lifebar
        for life in game.lifebar:
            life.draw(self.screen)

        # print current score
        self.printScore(game)

        # print invincible time if applies
        if game.invincible > 4:
            self.printInvTime(game)


    def run(self, game):
        game.clock.tick(game.speed)
        self.createObstacle(game)
        self.update(game)
        self.computeScore(game)
        self.draw(game)
        self.commandsInterpreter.run(game, self)

