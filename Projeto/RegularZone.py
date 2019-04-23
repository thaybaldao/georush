from Player import *
from Obstacles import *
from Settings import *
from pygame.locals import *
import pygame
import os
import random

class RegularZone:
    def __init__(self):
        pass

    def printScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        score = font.render("Score: " + str(int(game.score)), True, ORANGE)
        game.screen.blit(score, (265, 10))

    def printInvTime(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 25)
        text = font.render("Invincible Time: "+str(int(game.invincible) - 4), True, PURPLE)
        game.screen.blit(text, (10, 455))

    def run(self, game):
        game.clock.tick(game.speed)
        self.events(game)
        self.update(game)
        self.draw(game)
        game.score = game.score + 0.01

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
            obstacle.update(False)
            if obstacle.x < -850:
                game.obstacles.pop(game.obstacles.index(obstacle))

        for life in game.lives:
            life.update(False)
            if life.x < -850:
                game.lives.pop(game.lives.index(life))

        for boost in game.boost:
            boost.update(False)
            if boost.x < -850:
                game.boost.pop(game.boost.index(boost))

    def draw(self, game):
        # Game Loop - draw
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(game.imgSound, (740, 450))

        for obstacle in game.obstacles:
            obstacle.draw(game.screen)

        game.runner.draw(game.screen)


        for life in game.lives:
            life.draw(game.screen)
        for boost in game.boost:
            boost.draw(game.screen)

        for life in game.lifebar:
            life.draw(game.screen)

        self.printScore(game)

        if game.invincible > 4:
            self.printInvTime(game)

        # after drawing everything, flip the display
        pygame.display.flip()

    def createObstacle(self, game):
        r = random.randrange(0, 6)
        l = random.randrange(0, 18)
        i = random.randrange(0, 20)
        if len(game.obstacles) == 0 or (
                game.obstacles[-1].num < 2 and game.obstacles[-1].x + game.obstacles[-1].width < 600) or (
                game.obstacles[-1].x + game.obstacles[-1].width < 480):
            if r == 0:
                game.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             0))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 1:
                game.obstacles.append(
                    Obstacle(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')),
                             'triangle', 1))

                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 2 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(
                    Obstacle(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))
                game.obstacles.append(
                    Obstacle(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))

                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    game.boost.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 3:
                game.obstacles.append(
                    Obstacle(810, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),
                             'rectangle',
                             3))
                game.obstacles.append(
                    Obstacle(1300, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),
                             'rectangle', 3))
                game.obstacles.append(
                    Obstacle(1197, 409, 99, 29, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')),
                             'triangle',
                             3))
                game.obstacles.append(
                    Obstacle(990, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                game.obstacles.append(
                    Obstacle(1480, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 4 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(
                    Obstacle(810, 408, 303, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')),
                             'triangle', 4))
                game.obstacles.append(
                    Obstacle(810, 380, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                game.obstacles.append(
                    Obstacle(935, 320, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                game.obstacles.append(
                    Obstacle(1060, 260, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    game.boost.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 5:
                game.obstacles.append(
                    Obstacle(810, 350, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')),
                             'rectangle',
                             5))
                game.obstacles.append(
                    Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')),
                             'triangle',
                             5))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))