from Screen import *

class StartScreen(Screen):
    def __init__(self):
        self.runScreen = False
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)


    def showScreen(self, game):
        self.runScreen = True
        self.startScreenSound(game)

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

                # highlight the instructions text
                if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
                    self.inst = self.font.render('INSTRUCTIONS', True, YELLOW)
                else:
                    self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)

                #  check if user wants to quit
                self.quitGameBehavior(game, event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if user wants to play
                    if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                        self.runScreen = False
                        game.timeRunningStarted = pygame.time.get_ticks() / 1000

                    # check if user wants to see instructions
                    if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
                        self.runScreen = False
                        game.instructionsScreen.runScreen = True

                    self.soundButtonBehavior(game, event, pos)

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
        game.screen.blit(self.inst, (200, 290))
        game.screen.blit(self.title, (225, 50))
        pygame.display.flip()








