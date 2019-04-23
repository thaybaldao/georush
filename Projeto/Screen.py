from Settings import *
import pygame
import os

class Screen:
    def __init__(self):
        self.runScreen = False

    def startScreenSound(self, game):
        if game.sound:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('menuLoop.wav'), -1)

    # def endScreenSound(self, game, song):
    #     if game.sound:
    #         pygame.mixer.Sound.fadeout(song, 300)


    def quitGameBehavior(self, game, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.runScreen = False
            game.running = False
            game.retry = False


    def soundButtonBehavior(self, game, event, pos):
            if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
                if game.sound:
                    game.sound = False
                    game.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))
                    pygame.mixer.Channel(0).stop()
                    pygame.mixer.Channel(1).stop()
                else:
                    game.sound = True
                    game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('menuLoop.wav'), -1)


    def drawBasicScreen(self, game):
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(game.screen)







