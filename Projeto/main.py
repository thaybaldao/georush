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

class ZoneState:

    def check(self, game, currentTime):
        pass

    def switch(self, game, state):
        pass

    def execute(self, game):
        pass


class RegularZoneState(ZoneState):

    def check(self, game, currentTime):
        if not game.inDangerZone and currentTime - game.timeRegularZoneStarted > 5 + 10*random.randrange(0, 2):
            self.switch(game, DangerZoneState)
        elif not game.inDangerZone:
            self.execute(game)

    def switch(self, game, state):
        if game.sound:
            game.soundManager.playSong(os.path.join('Music', 'DeadLocked.wav'))
        game.inDangerZone = True
        game.timeDangerZoneStarted = pygame.time.get_ticks() / 1000
        game.dangerZone.dangerZoneMessage(game)
        self.__class__ = state

    def execute(self, game):
        game.regularZone.run(game)


class DangerZoneState(ZoneState):

    def check(self, game, currentTime):
        if game.inDangerZone and currentTime - game.timeDangerZoneStarted > 5 + 10 * random.randrange(0, 2):
            self.switch(game, RegularZoneState)
        elif game.inDangerZone:
            self.execute(game)

    def switch(self, game, state):
        game.inDangerZone = False
        game.dangerZone.wellDoneMessage(game)
        if game.sound:
            game.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))
        game.timeRegularZoneStarted = pygame.time.get_ticks() / 1000
        self.__class__ = state

    def execute(self, game):
        game.dangerZone.run(game)


class ZonesStateMachine:
    def __init__(self):
        self.switchZones = []

    def add(self, zone):
        self.switchZones.append(zone)

    def run(self, game):
        game.playing = True
        game.score = 0

        if game.sound:
            game.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))

        game.timeRegularZoneStarted = pygame.time.get_ticks() / 1000
        game.inDangerZone = False

        while game.playing and not game.userQuit:
            currentTime = pygame.time.get_ticks() / 1000
            for c in self.switchZones:
                c.check(game, currentTime)



class GameManager:
    def __init__(self):
        # initializing pygame
        pygame.init()

        # setting up sounds
        self.soundManager = SoundManager()
        self.sound = True
        self.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))

        # setting up clock and speed
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(USEREVENT + 1, 500)
        pygame.time.set_timer(USEREVENT + 2, 6000)
        self.initialSpeed = 250
        self.speed = self.initialSpeed

        # initializing game constants
        self.numLives = 0
        self.invincible = 0
        self.playing = True
        self.userQuit = False

        # initializing screens
        self.startScreen = StartScreen()
        self.instructionsScreen = InstructionsScreen()
        self.resetScreen = ResetScreen()
        self.regularZone = RegularZone()
        self.dangerZone = DangerZone()
        self.inDangerZone = False
        self.timeRegularZoneStarted = 0
        self.timeDangerZoneStarted = 0
        self.zonesStateMachine = ZonesStateMachine()
        self.zonesStateMachine.add(RegularZoneState())
        self.zonesStateMachine.add(DangerZoneState())

        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        self.lives = []
        self.lifebar = []
        self.boost = []

        # allowing spacebar to be pressed
        pygame.key.set_repeat(17, 17)

        # initializing scores
        self.score = 0
        self.highScore = 0

    def run(self):
        self.startScreen.run(self)

gameManager = GameManager()
gameManager.run()

pygame.quit()
