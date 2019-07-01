from Obstacles import *
from Settings import *
from Screen import *
import pygame
from pygame.locals import *
import os
from SoundBehavior import*

class Zone(Screen):
    def __init__(self):
        self.soundBehavior = None


    def computeScore(self, game):
        game.score += 0.01


    def jumpBehavior(self, game, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.runner.jump()


    def interpretEvents(self, game):
        for event in pygame.event.get():
            if event.type == USEREVENT + 2:
                game.speed += 0.5

            if event.type == USEREVENT + 1:
                self.createObstacle(game)

            pos = pygame.mouse.get_pos()

            self.quitGameBehavior(game, event)

            self.jumpBehavior(game, event)

            self.soundBehavior.soundButtonBehavior(game, pos, event)


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
        game.screen.blit(score, (265, 10))


    def printInvTime(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 25)
        text = font.render("Invincible Time: " + str(int(game.invincible) - 4), True, PURPLE)
        game.screen.blit(text, (10, 455))


    def basicZoneDraw(self, game):
        self.drawBasicScreen(game)

        # draw obstacles
        for obstacle in game.obstacles:
            obstacle.draw(game.screen)

        # draw lifebar
        for life in game.lifebar:
            life.draw(game.screen)

        # print current score
        self.printScore(game)

        # print invincible time if applies
        if game.invincible > 4:
            self.printInvTime(game)


    def run(self, game):
        game.clock.tick(game.speed)

        self.interpretEvents(game)
        self.update(game)
        self.computeScore(game)
        self.draw(game)

        if game.score > game.highScore:
            game.highScore = game.score