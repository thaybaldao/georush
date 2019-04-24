from Screen import *

class InstructionsScreen(Screen):
    def __init__(self):
        self.runScreen = False
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        self.title = font.render('INSTRUCTIONS', True, PINK)
        font2 = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)
        self.play = font2.render('Press ENTER or CLICK HERE to play.', True, PURPLE)


    def showScreen(self, game):
        self.runScreen = True
        self.startScreenSound(game)

        while self.runScreen:
            game.clock.tick(game.speed)
            self.drawScreen(game)
            self.updateScreen(game)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)

                # highlight the play text
                if pos[0] > 280 and pos[0] < 780 and pos[1] > 410 and pos[1] < 430:
                    self.play = font.render('Press ENTER or CLICK HERE to play.', True, YELLOW)
                else:
                    self.play = font.render('Press ENTER or CLICK HERE to play.', True, PURPLE)

                #  check if user wants to quit
                self.quitGameBehavior(game, event)

                # check if user wants to play
                if event.type==pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_RETURN]:
                    self.runScreen = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 280 and pos[0] < 780 and pos[1] > 410 and pos[1] < 430:
                        self.runScreen = False


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
        game.screen.blit(self.title, (200, 20))
        self.printInstructions(game, 1, '- Click on the spacebar to jump.')
        self.printInstructions(game, 2, '- Avoid the triangles!')
        self.printInstructions(game, 3, '- Jump and land on the platforms if needed.')
        self.printInstructions(game, 4, '- Collect hearts to gain extra lives.')
        self.printInstructions(game, 5, '- Collect stars to be invincible for 15 seconds.')
        self.printInstructions(game, 6, '- Click on the speaker icon to mute game sounds.')
        game.screen.blit(self.play, (280, 410))

        pygame.display.flip()

    def printInstructions(self, game, num, text):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 18)
        ins = font.render(text, True, YELLOW)
        game.screen.blit(ins, (70, 40 + 50*num))
