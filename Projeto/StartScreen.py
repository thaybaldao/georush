from Screen import *

class StartScreen(Screen):
    def __init__(self):
        self.runScreen = False
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.inst = pygame.image.load(os.path.join('Imagens', 'Instrucoes.png'))

    def showScreen(self, game):
        self.runScreen = True
        self.startScreenSound(game, game.menuSound)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.drawScreen(game)
            self.updateScreen(game)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                # highlight hovering the play button
                if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
                else:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))

                #  check if user wants to quit
                self.quitGameBehavior(game, event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if user wants to play
                    if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                        self.runScreen = False
                        game.timeRunningStarted = pygame.time.get_ticks() / 1000

                    self.soundButtonBehavior(game, event, pos)

        self.endScreenSound(game, game.menuSound)

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
        self.drawBasicScreen(game)
        game.screen.blit(self.play, (340, 140))
        game.screen.blit(self.inst, (75, 290))
        game.screen.blit(self.title, (225, 50))
        pygame.display.flip()







