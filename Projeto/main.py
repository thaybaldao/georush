from Player import *
from Obstacles import *
from Settings import *
from StartScreen import*
from InstructionsScreen import*
from ResetScreen import*
from RegularZone import*
from DangerZone import*
from SoundManager import*
from GameState import*
from pygame.locals import *
import pygame
import os
import random

class GameManager:
    def __init__(self):
        # initializing pygame
        pygame.init()

        # setting up sounds
        self.soundManager = SoundManager()

        self.sound = True
        self.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))

        # setting up clock
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(USEREVENT + 1, 500)
        pygame.time.set_timer(USEREVENT + 2, 6000)

        # initializing game constants
        self.numLives = 0
        self.invincible = 0

        # initializing screens
        self.startScreen = StartScreen()
        self.instructionsScreen = InstructionsScreen()
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

        self.initialSpeed = 250
        self.speed = self.initialSpeed

        # allowing spacebar to be pressed
        pygame.key.set_repeat(17, 17)
        self.score = 0
        self.highScore = 0

        self.inDangerZone = False

        self.userQuit = False

        self.timeRegularZoneStarted = 0

        self.timeDangerZoneStarted = 0


    def runZones(self):
        # game Loop
        self.playing = True
        self.score = 0

        if self.sound:
            self.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))

        timeRegularZoneStarted = pygame.time.get_ticks()/1000
        self.inDangerZone = False

        while self.playing:
            currentTime = pygame.time.get_ticks()/1000

            if not self.inDangerZone and currentTime - timeRegularZoneStarted < 5 + 10*random.randrange(0, 2):
                self.inDangerZone = False
                self.regularZone.run(self)
            else:
                if not self.inDangerZone:
                    if self.sound:
                        self.soundManager.playSong(os.path.join('Music', 'DeadLocked.wav'))
                    self.inDangerZone = True
                    timeDangerZoneStarted = pygame.time.get_ticks()/1000
                    self.dangerZone.dangerZoneMessage(self)
                elif self.inDangerZone and currentTime - timeDangerZoneStarted < 15 + 5*random.randrange(0, 2):
                        self.inDangerZone = True
                        self.dangerZone.run(self)
                else:
                    self.inDangerZone = False
                    self.dangerZone.wellDoneMessage(self)
                    if self.sound:
                        self.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))
                    timeRegularZoneStarted = pygame.time.get_ticks()/1000

    def run(self):
        self.startScreen.run(self)

gameManager = GameManager()
gameManager.run()

pygame.quit()
