from Obstacles import *
from Settings import *
import pygame
from pygame.locals import *
import os

class Zone:
    def __init__(self):
        pass

    def printScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        score = font.render("Score: " + str(int(game.score)), True, ORANGE)
        game.screen.blit(score, (265, 10))

    def printInvTime(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        text = font.render(str(int(game.invincible)), True, PINK)
        game.screen.blit(text, (700, 10))

    def computeScore(self, game):
        game.score += 0.01

    def run(self, game):
        game.clock.tick(game.speed)

        self.events(game)
        self.update(game)
        self.draw(game)
        self.computeScore(game)

        if game.score > game.highScore:
            game.highScore = game.score

    def events(self, game):
        # Game Loop - events
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # check if user quit
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

    def basicZoneUpdate(self, game):
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
            obstacle.update(game.inDangerZone)
            if obstacle.x < -850:
                game.obstacles.pop(game.obstacles.index(obstacle))

    def basicZoneDraw(self, game):
        # draw background
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))

        # draw sound button
        game.screen.blit(game.imgSound, (740, 450))

        # draw obstacles
        for obstacle in game.obstacles:
            obstacle.draw(game.screen)

        # draw lifebar
        for life in game.lifebar:
            life.draw(game.screen)

        # draw runner
        game.runner.draw(game.screen)


        # print current score
        self.printScore(game)

        # print invincible time if applies
        if game.invincible > 0:
            self.printInvTime(game)