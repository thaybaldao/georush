from Settings import *
from SoundBehavior import*
from UserCommands import *

class Screen:
    def __init__(self):
        self.soundBehavior = SoundBehaviorScreen()
        self.basicInitialization()

    def basicInitialization(self):
        self.commandsMediator = CommandsMediator()
        self.commandsMediator.add(QuitGameCommand())
        self.commandsMediator.add(SoundButtonCommand())

        # creating game window
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(TITLE)

        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()

        self.runScreen = True


    def startScreenSound(self, game):
        if game.sound:
            game.soundManager.playSong(os.path.join('Music', 'menuLoop.wav'))

    def basicScreenUpdate(self, game):
        game.runner.update(game)

        # making background move
        self.bgX -= 2
        self.bgX2 -= 2
        if self.bgX < self.bg.get_width() * -1:
            self.bgX = self.bg.get_width()
        if self.bgX2 < self.bg.get_width() * -1:
            self.bgX2 = self.bg.get_width()


    def drawBasicScreen(self, game):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(self.screen)






