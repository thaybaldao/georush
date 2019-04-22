import pygame
import os
from Settings import *


class ResetScreen:
    def __init__(self):
        self.runScreen = False
        self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))
        self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))
        self.tryAgain = pygame.image.load(os.path.join('Imagens', 'Best_Score.png'))
        self.gameOver = pygame.image.load(os.path.join('Imagens', 'Game_Over.png'))
        self.retry = False

    def showScreen(self, game):
        # game over/continue
        self.runScreen = True
        if game.sound:
            pygame.mixer.Sound.play(game.menuSound, -1)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.drawScreen(game)
            game.runner.update(game)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                # highlight hovering the button
                if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Replay1.png'))
                else:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))

                if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'X_button1.png'))
                else:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[
                    pygame.K_ESCAPE]:
                    self.runScreen = False
                    self.retry = False
                    game.running = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                        self.retry = True
                        self.runScreen = False
                        game.timeRunningStarted = pygame.time.get_ticks() / 1000
                        game.inDangerZone = False

                    if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                        self.retry = False
                        self.runScreen = False
                        game.running = False
                        break

                    if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
                        if game.sound:
                            game.sound = False
                            game.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))
                            pygame.mixer.Sound.stop(game.menuSound)
                        else:
                            game.sound = True
                            game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
                            pygame.mixer.Sound.play(game.menuSound, -1)

        if game.sound:
            pygame.mixer.Sound.fadeout(game.menuSound, 300)

    def drawScreen(self, game):
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(self.reset, (205, 140))
        game.screen.blit(self.stop, (455, 140))
        game.screen.blit(self.gameOver, (190, 50))
        game.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(game.screen)
        self.printFinalScore(game)
        pygame.display.flip()


    def printFinalScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        currentScore = font.render("Your Score: " + str(int(game.score)), True, PURPLE)
        bestScore = font.render("Best Score: " + str(int(game.highScore)), True, PURPLE)
        game.screen.blit(currentScore, (180, 300))
        game.screen.blit(bestScore, (180, 350))







