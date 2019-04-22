import pygame
import os


class StartScreen:
    def __init__(self):
        self.runScreen = False
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.inst = pygame.image.load(os.path.join('Imagens', 'Instrucoes.png'))

    def showScreen(self, game):
        # game splash/start screen
        self.runScreen = True
        if game.sound:
            pygame.mixer.Sound.play(game.menuSound, -1)
        while self.runScreen:
            game.clock.tick(game.speed)
            self.drawScreen(game)
            self.updateScreen(game)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # highlight hovering the button
                if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
                else:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[
                    pygame.K_ESCAPE]:
                    self.runScreen = False
                    game.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                        self.runScreen = False
                        game.timeRunningStarted = pygame.time.get_ticks() / 1000
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

    def updateScreen(self, game):
        game.runner.update(game)

        # making background move
        game.bgX -= 2
        game.bgX2 -= 2
        if game.bgX < game.bg.get_width() * -1:
            game.bgX = game.bg.get_width()
        if game.bgX2 < game.bg.get_width() * -1:
            game.bgX2 = game.bg.get_width()

    def drawScreen(self, game):
        game.screen.blit(game.bg, (game.bgX, 0))
        game.screen.blit(game.bg, (game.bgX2, 0))
        game.screen.blit(self.play, (340, 140))
        game.screen.blit(self.inst, (75, 290))
        game.screen.blit(self.title, (225, 50))
        game.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(game.screen)
        pygame.display.flip()







