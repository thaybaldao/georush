from Player import *
from Obstacles import *
from Settings import *
from StartScreen import*
from ResetScreen import*
from RegularZone import*
from DangerZone import*
from pygame.locals import *
import pygame
import os
import random

class Game:
    def __init__(self, highScore, pastSound):
        # initializing pygame
        pygame.init()

        # setting up sounds
        pygame.mixer.init()
        pygame.mixer.music.load('BackOnTrack.wav')
        self.menuSound = pygame.mixer.Sound('menuLoop.wav')
        self.pastSound = pastSound
        if self.pastSound:
            self.sound = True
            self.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        else:
            self.sound = False
            self.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))

        # creating game window
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(TITLE)

        # setting up clock
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(USEREVENT + 1, 500)
        pygame.time.set_timer(USEREVENT + 2, 6000)

        # initializing game constants
        self.running = True
        self.numLives = 0
        self.invincible = 0
        self.collisions = False

        # initializing screens
        self.startScreen = StartScreen()
        self.resetScreen = ResetScreen()

        # initializing game zones
        self.regularZone = RegularZone()
        self.dangerZone = DangerZone()

        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        self.lives = []
        self.lifebar = []
        self.boost = []

        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.initialSpeed = 250
        self.speed = self.initialSpeed

        # initializing danger zone
        self.inDangerZone = False
        self.timeRunningStarted = pygame.time.get_ticks() / 1000
        self.timeDangerZoneStarted = 0

        # allowing spacebar to be pressed
        pygame.key.set_repeat(17, 17)

        # setting score
        self.score = 0
        self.highScore = highScore

    def run(self):
        # Game Loop
        self.playing = True
        if self.sound:
            pygame.mixer.music.play(-1)
        while self.playing:
            currentTime = pygame.time.get_ticks()/1000

            if not self.inDangerZone and currentTime - self.timeRunningStarted < 40 + 10*random.randrange(0, 2):
                self.inDangerZone = False
                self.regularZone.run(self)
            else:
                if not self.inDangerZone:
                    self.inDangerZone = True
                    self.timeDangerZoneStarted = pygame.time.get_ticks()/1000
                    game.obstacles.clear()
                    pygame.time.wait(500)
                    self.dangerZone.drawDangerScreen(PURPLE, 'DANGER ZONE!', 115, game)
                    pygame.time.wait(400)
                    self.dangerZone.drawDangerScreen(YELLOW, 'DANGER ZONE!', 115, game)
                    pygame.time.wait(500)
                    self.dangerZone.drawDangerScreen(PURPLE, 'DANGER ZONE!', 115, game)
                    pygame.time.wait(400)

                elif self.inDangerZone and currentTime - self.timeDangerZoneStarted < 10:
                        self.inDangerZone = True
                        self.dangerZone.run(self)
                else:
                    self.inDangerZone = False
                    game.obstacles.clear()
                    pygame.time.wait(500)
                    self.dangerZone.drawDangerScreen(PURPLE, 'WELL DONE!', 160, game)
                    pygame.time.wait(400)
                    self.dangerZone.drawDangerScreen(YELLOW, 'WELL DONE!', 160, game)
                    pygame.time.wait(500)
                    self.dangerZone.drawDangerScreen(PURPLE, 'WELL DONE!', 160, game)
                    pygame.time.wait(400)
                    self.timeRunningStarted = pygame.time.get_ticks()/1000
            # self.runGame()

highScore = 0
game = Game(highScore, True)
game.startScreen.showScreen(game)

while game.running and not game.startScreen.runScreen and not game.resetScreen.runScreen:
    game.run()

while game.resetScreen.retry:
    highScore = game.highScore
    soundPast = game.sound
    del game
    game = Game(highScore, soundPast)
    game.sound = soundPast
    while game.running and not game.startScreen.runScreen and not game.resetScreen.runScreen:
        game.run()

pygame.quit()
