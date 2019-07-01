from Screen import *

class StartScreen(Screen):
    def __init__(self):
        super().__init__()
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.inst = self.font.render('INSTRUCTIONS', True, PURPLE)
        self.comandsInterpreter.add(HighlightPlayButtonCommand())
        self.comandsInterpreter.add(NotHighlightPlayButtonCommand())
        self.comandsInterpreter.add(PlayButtonCommand())
        self.comandsInterpreter.add(HighlightInstructionsButtonCommand())
        self.comandsInterpreter.add(NotHighlightInstructionsButtonCommand())
        self.comandsInterpreter.add(InstructionsButtonCommand())


    def draw(self, game):
        self.drawBasicScreen(game)
        self.screen.blit(self.play, (340, 140))
        self.screen.blit(self.inst, (200, 290))
        self.screen.blit(self.title, (225, 50))
        pygame.display.flip()


    def run(self, game):
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.comandsInterpreter.run(game, self)
            self.basicScreenUpdate(game)
            self.draw(game)





