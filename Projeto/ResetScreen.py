from Screen import *

class ResetScreen(Screen):
    def __init__(self):
        super().__init__()
        self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))
        self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))
        self.tryAgain = pygame.image.load(os.path.join('Imagens', 'Best_Score.png'))
        self.gameOver = pygame.image.load(os.path.join('Imagens', 'Game_Over.png'))
        self.retry = False


    def replayButtonBehavior(self, event, pos, game):
        # highlight hovering the replay button
        if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
            self.reset = pygame.image.load(os.path.join('Imagens', 'Replay1.png'))
        else:
            self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if user wants to play
            if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                self.runScreen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if user wants to play again
            if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                self.retry = True
                self.runScreen = False
                game.inDangerZone = False


    def xButtonBehavior(self, event, pos, game):
        # highlight hovering the X button
        if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
            self.stop = pygame.image.load(os.path.join('Imagens', 'X_button1.png'))
        else:
            self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))

        if event.type == pygame.MOUSEBUTTONDOWN:

            # check if user wants to quit
            if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                self.retry = False
                self.runScreen = False
                game.running = False


    def interpretEvents(self, game):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            self.replayButtonBehavior(event, pos, game)

            self.xButtonBehavior(event, pos, game)

            self.soundBehavior.soundButtonBehavior(game, pos, event)

            self.quitGameBehavior(game, event)


    def showScreen(self, game):
        pygame.mixer.Channel(0).set_volume(1)
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.interpretEvents(game)
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






