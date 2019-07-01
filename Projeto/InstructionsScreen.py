from Screen import *

class InstructionsScreen(Screen):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.title = font.render('INSTRUCTIONS', True, PINK)
        font2 = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)
        self.play = font2.render('Press ENTER or CLICK HERE to play.', True, PURPLE)
        self.comandsInterpreter.add(HighlightAdvanceToGameTextCommand())
        self.comandsInterpreter.add(NotHighlightAdvanceToGameTextCommand())
        self.comandsInterpreter.add(AdvanceToGameTextCommand())

    def updateScreen(self, game):
        game.runner.update(game)

        # making background move
        game.bgX -= 2
        game.bgX2 -= 2
        if game.bgX < game.bg.get_width() * -1:
            game.bgX = game.bg.get_width()
        if game.bgX2 < game.bg.get_width() * -1:
            game.bgX2 = game.bg.get_width()


    def printInstructions(self, game, num, text):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 18)
        ins = font.render(text, True, YELLOW)
        game.screen.blit(ins, (70, 40 + 50*num))


    def drawScreen(self, game):
        self.drawBasicScreen(game)
        game.screen.blit(self.title, (200, 20))
        self.printInstructions(game, 1, '- Click on the spacebar to jump.')
        self.printInstructions(game, 2, '- Avoid the triangles!')
        self.printInstructions(game, 3, '- Jump and land on the platforms if needed.')
        self.printInstructions(game, 4, '- Collect hearts to gain extra lives.')
        self.printInstructions(game, 5, '- Collect stars to be invincible for 15 seconds.')
        self.printInstructions(game, 6, '- Click on the speaker icon to mute game sounds.')
        game.screen.blit(self.play, (280, 410))

        pygame.display.flip()


    def showScreen(self, game):
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.comandsInterpreter.run(game, self)
            self.updateScreen(game)
            self.drawScreen(game)
