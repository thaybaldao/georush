from Screen import *

class ResetScreen(Screen):
    def __init__(self):
        super().__init__()
        self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))
        self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))
        self.tryAgain = pygame.image.load(os.path.join('Imagens', 'Best_Score.png'))
        self.gameOver = pygame.image.load(os.path.join('Imagens', 'Game_Over.png'))
        self.retry = False
        self.comandsInterpreter = CommandsInterpreter()
        self.comandsInterpreter.add(QuitGameCommand())
        self.comandsInterpreter.add(HighlightReplayButtonCommand())
        self.comandsInterpreter.add(NotHighlightReplayButtonCommand())
        self.comandsInterpreter.add(ReplayButtonCommand())
        self.comandsInterpreter.add(HighlightXButtonCommand())
        self.comandsInterpreter.add(NotHighlightXButtonCommand())
        self.comandsInterpreter.add(XButtonCommand())
        self.comandsInterpreter.add(SoundButtonCommand())


    def showScreen(self, game):
        pygame.mixer.Channel(0).set_volume(1)
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.comandsInterpreter.run(game, self)
            game.runner.update(game)
            self.drawScreen(game)


    def printFinalScore(self, game):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        currentScore = font.render("Your Score: " + str(int(game.score)), True, PURPLE)
        bestScore = font.render("Best Score: " + str(int(game.highScore)), True, PURPLE)
        game.screen.blit(currentScore, (180, 300))
        game.screen.blit(bestScore, (180, 350))


    def drawScreen(self, game):
        self.drawBasicScreen(game)

        game.screen.blit(self.reset, (205, 140))
        game.screen.blit(self.stop, (455, 140))
        game.screen.blit(self.gameOver, (190, 50))

        self.printFinalScore(game)

        pygame.display.flip()






