from Screen import *

class StartScreen(Screen):
    def __init__(self):
        super().__init__()
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)


    def playButtonBehavior(self, event, pos):
        # highlight hovering the play button
        if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
            self.play = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
        else:
            self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if user wants to play
            if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                self.runScreen = False


    def instructionsButtonBehavior(self, event, pos, game):
        # highlight the instructions text
        if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
            self.inst = self.font.render('INSTRUCTIONS', True, YELLOW)
        else:
            self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if user wants to see instructions
            if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
                self.runScreen = False
                game.instructionsScreen.runScreen = True


    def interpretEvents(self, game):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            self.playButtonBehavior(event, pos)

            self.instructionsButtonBehavior(event, pos, game)

            self.soundBehavior.soundButtonBehavior(game, pos, event)

            self.quitGameBehavior(game, event)


    def drawScreen(self, game):
        self.drawBasicScreen(game)
        game.screen.blit(self.play, (340, 140))
        game.screen.blit(self.inst, (200, 290))
        game.screen.blit(self.title, (225, 50))
        pygame.display.flip()


    def showScreen(self, game):
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.interpretEvents(game)
            self.basicScreenUpdate(game)
            self.drawScreen(game)





