from Screen import *

class StartScreen(Screen):
    def __init__(self):
        super().__init__()
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)
        self.commandsMediator.add(HighlightPlayButtonCommand())
        self.commandsMediator.add(NotHighlightPlayButtonCommand())
        self.commandsMediator.add(PlayButtonCommand())
        self.commandsMediator.add(HighlightInstructionsButtonCommand())
        self.commandsMediator.add(NotHighlightInstructionsButtonCommand())
        self.commandsMediator.add(InstructionsButtonCommand())


    def draw(self, game):
        self.drawBasicScreen(game)
        self.screen.blit(self.play, (340, 140))
        self.screen.blit(self.inst, (200, 290))
        self.screen.blit(self.title, (225, 50))
        pygame.display.flip()


    def run(self, game):
        self.startScreenSound(game)

        while not game.userQuit and self.runScreen:
            game.clock.tick(game.speed)
            self.basicScreenUpdate(game)
            self.draw(game)
            self.commandsMediator.run(game, self)





