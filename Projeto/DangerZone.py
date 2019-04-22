from Player import *
from Obstacles import *
from Settings import *
from pygame.locals import *
import pygame
import os
import random


class DangerZone:
    def __init__(self):
        pass

    def drawDangerScreen(self, color, message, x, game):
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(game.screen)
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 55)
        text = font.render(message, True, color)
        game.screen.blit(text, (x, 225))
        pygame.display.flip()

    def printScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        score = font.render("Score: " + str(int(game.score)), True, ORANGE)
        game.screen.blit(score, (265, 10))

    def printInvTime(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        text = font.render(str(int(game.invincible)), True, PINK)
        game.screen.blit(text, (700, 10))

    def run(self, game):
        game.clock.tick(game.speed)
        self.events(game)
        self.update(game)
        self.draw(game)
        game.score = game.score + 0.02

        if game.score > game.highScore:
            game.highScore = game.score

    def events(self, game):
        # Game Loop - events
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # check for closing window
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if game.playing:
                    game.playing = False
                game.running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.runner.jump()

            if event.type == USEREVENT + 2:
                game.speed += 0.5

            if event.type == USEREVENT + 1:
                self.createObstacle(game)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
                    if game.sound:
                        game.sound = False
                        game.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))
                        pygame.mixer.music.stop()
                    else:
                        game.sound = True
                        game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
                        pygame.mixer.music.play(-1)

    def update(self, game):
        game.runner.update(game)

        # making background move
        game.bgX -= 2
        game.bgX2 -= 2
        if game.bgX < game.bg.get_width() * -1:
            game.bgX = game.bg.get_width()
        if game.bgX2 < game.bg.get_width() * -1:
            game.bgX2 = game.bg.get_width()

        # making obstacles disappear
        for obstacle in game.obstacles:
            obstacle.update(True)
            if obstacle.x < -850:
                game.obstacles.pop(game.obstacles.index(obstacle))


    def draw(self, game):
        # Game Loop - draw
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(game.imgSound, (740, 450))

        for obstacle in game.obstacles:
            obstacle.draw(game.screen)

        game.runner.draw(game.screen)

        for life in game.lifebar:
            life.draw(game.screen)

        self.printScore(game)

        if game.invincible > 0:
            self.printInvTime(game)

        # after drawing everything, flip the display
        pygame.display.flip()


    def createObstacle(self, game):
        r = random.randrange(0, 12)
        if len(game.obstacles) == 0 or (game.obstacles[-1].x + game.obstacles[-1].width < 650):
            if r < 4:
                game.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')),
                             'triangle',
                             1))
            elif r < 7:
                game.obstacles.append(
                    Obstacle(810, 375, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')),
                             'triangle',
                             0))
            elif r < 9 and (len(game.obstacles) == 0 or game.obstacles[-1].num != 2):
                game.obstacles.append(
                    Obstacle(810, 245, 35, 36,
                             pygame.image.load(os.path.join('Imagens', 'Triangulo_Invertido_Danger_Zone.png')),
                             'triangle', 2))

