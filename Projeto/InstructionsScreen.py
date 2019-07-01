from Screen import *

class InstructionsScreen(Screen):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.title = font.render('INSTRUCTIONS', True, PINK)
        font2 = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)
        self.play = font2.render('Press ENTER or CLICK HERE to play.', True, PURPLE)
        self.commandsMediator.add(HighlightAdvanceToGameTextCommand())
        self.commandsMediator.add(NotHighlightAdvanceToGameTextCommand())
        self.commandsMediator.add(AdvanceToGameTextCommand())

    def updateScreen(self, game):
        game.runner.update(game)

        # making background move
        self.bgX -= 2
        self.bgX2 -= 2
        if self.bgX < self.bg.get_width() * -1:
            self.bgX = self.bg.get_width()
        if self.bgX2 < self.bg.get_width() * -1:
            self.bgX2 = self.bg.get_width()


    def printInstructions(self, game, num, text):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 18)
        ins = font.render(text, True, YELLOW)
        self.screen.blit(ins, (70, 40 + 50*num))


    def draw(self, game):
        self.drawBasicScreen(game)
        self.screen.blit(self.title, (200, 20))
        self.printInstructions(game, 1, '- Click on the spacebar to jump.')
        self.printInstructions(game, 2, '- Avoid the triangles!')
        self.printInstructions(game, 3, '- Jump and land on the platforms if needed.')
        self.printInstructions(game, 4, '- Collect hearts to gain extra lives.')
        self.printInstructions(game, 5, '- Collect stars to be invincible for 15 seconds.')
        self.printInstructions(game, 6, '- Click on the speaker icon to mute game sounds.')
        self.screen.blit(self.play, (280, 410))

        pygame.display.flip()


    def run(self, game):
        self.startScreenSound(game)

        while not game.userQuit:
            game.clock.tick(game.speed)
            self.updateScreen(game)
            self.draw(game)
            self.commandsMediator.run(game, self)
