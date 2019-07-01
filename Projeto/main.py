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

class Game:
    def __init__(self, highScore, pastSound):
        # initializing pygame
        pygame.init()

        # setting up sounds
        self.soundManager = SoundManager()
        self.pastSound = pastSound

        if self.pastSound:
            self.sound = True
            self.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        else:
            self.sound = False
            self.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))


        # setting up clock
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(USEREVENT + 1, 500)
        pygame.time.set_timer(USEREVENT + 2, 6000)

        # initializing game constants
        self.running = True
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

        self.inDangerZone = False
        self.timeRegularZoneStarted = pygame.time.get_ticks() / 1000
        self.timeDangerZoneStarted = 0

        # allowing spacebar to be pressed
        pygame.key.set_repeat(17, 17)
        self.score = 0
        self.highScore = highScore

    def run(self):
        # game Loop
        self.playing = True

        if self.sound:
            self.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))

        self.timeRegularZoneStarted = pygame.time.get_ticks()/1000

        while self.playing:
            currentTime = pygame.time.get_ticks()/1000


            if not self.inDangerZone and currentTime - self.timeRegularZoneStarted < 5 + 10*random.randrange(0, 2):
                self.inDangerZone = False
                self.regularZone.run(self)
            else:
                if not self.inDangerZone:
                    if self.sound:
                        self.soundManager.playSong(os.path.join('Music', 'DeadLocked.wav'))
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
                elif self.inDangerZone and currentTime - self.timeDangerZoneStarted < 15 + 5*random.randrange(0, 2):
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
                    if self.sound:
                        self.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))
                    self.timeRegularZoneStarted = pygame.time.get_ticks()/1000

highScore = 0
game = Game(highScore, True)
game.startScreen.run(game)

if not game.startScreen.runScreen and game.instructionsScreen.runScreen:
    game.instructionsScreen.run(game)

while game.running and not game.resetScreen.runScreen:
    game.run()

while game.resetScreen.retry:
    highScore = game.highScore
    soundPast = game.sound
    del game
    game = Game(highScore, soundPast)
    game.sound = soundPast

    while game.running and not game.resetScreen.runScreen:
        game.run()

pygame.quit()
