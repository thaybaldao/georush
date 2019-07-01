from Settings import *
from SoundBehavior import*
import pygame
import os

class Screen:
    def __init__(self):
        self.runScreen = False
        self.soundBehavior = SoundBehaviorScreen()

    def startScreenSound(self, game):
        if game.sound:
            game.soundManager.playSong(os.path.join('Music', 'menuLoop.wav'))


    def quitGameBehavior(self, game, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.runScreen = False
            game.running = False
            game.retry = False


    def basicScreenUpdate(self, game):
        game.runner.update(game)

        # making background move
        game.bgX -= 2
        game.bgX2 -= 2
        if game.bgX < game.bg.get_width() * -1:
            game.bgX = game.bg.get_width()
        if game.bgX2 < game.bg.get_width() * -1:
            game.bgX2 = game.bg.get_width()


    def drawBasicScreen(self, game):
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(game.screen)







