from Player import *
from Obstacles import *
from Settings import *
from StartScreen import*
from ResetScreen import*
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

        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        self.lifes = []
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


    def drawDangerZoneScreen(self, color, message, x):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(self.imgSound, (740, 450))
        self.runner.draw(self.screen)
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 55)

        text = font.render(message, True, color)

        self.screen.blit(text, (x, 225))
        pygame.display.flip()


    def printScore(self):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        score = font.render("Score: "+str(int(self.score)), True, ORANGE)
        self.screen.blit(score, (265, 10))

    def printInvTime(self):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
        text = font.render(str(int(self.invincible)), True, PINK)
        self.screen.blit(text, (700, 10))

    def run(self):
        # Game Loop
        self.playing = True
        if self.sound:
            pygame.mixer.music.play(-1)
        while self.playing:
            currentTime = pygame.time.get_ticks()/1000

            if not self.inDangerZone and currentTime - self.timeRunningStarted < 20:
                self.inDangerZone = False
                self.runGame()
            else:
                if not self.inDangerZone:
                    self.inDangerZone = True
                    self.timeDangerZoneStarted = pygame.time.get_ticks()/1000
                    game.obstacles.clear()
                    pygame.time.wait(500)
                    self.drawDangerZoneScreen(PURPLE, 'DANGER ZONE!', 115)
                    pygame.time.wait(400)
                    self.drawDangerZoneScreen(VIOLET, 'DANGER ZONE!', 115)
                    pygame.time.wait(500)
                    self.drawDangerZoneScreen(PURPLE, 'DANGER ZONE!', 115)
                    pygame.time.wait(400)

                elif self.inDangerZone and currentTime - self.timeDangerZoneStarted < 10:
                        self.inDangerZone = True
                        self.runGame()
                else:
                    self.inDangerZone = False
                    game.obstacles.clear()
                    pygame.time.wait(500)
                    self.drawDangerZoneScreen(PURPLE, 'WELL DONE!', 160)
                    pygame.time.wait(400)
                    self.drawDangerZoneScreen(VIOLET, 'WELL DONE!', 160)
                    pygame.time.wait(500)
                    self.drawDangerZoneScreen(PURPLE, 'WELL DONE!', 160)
                    pygame.time.wait(400)
                    self.timeRunningStarted = pygame.time.get_ticks()/1000
            # self.runGame()


    def runGame(self):
        self.clock.tick(self.speed)
        self.events()
        self.update()
        self.draw()
        if self.inDangerZone == False:
            self.score = self.score + 0.01
        else:
            self.score = self.score + 0.02
        if self.score > self.highScore:
            self.highScore = self.score


    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            # check for closing window
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.runner.jump()

            if event.type == USEREVENT + 2:
                self.speed += 0.5

            if event.type == USEREVENT + 1:
                if not self.inDangerZone:
                    self.createObstacle()
                else:
                    self.createObstacleDangerZone()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
                    if self.sound:
                        self.sound = False
                        self.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))
                        pygame.mixer.music.stop()
                    else:
                        self.sound = True
                        self.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
                        pygame.mixer.music.play(-1)

    # def printInstructions(self):
    #     font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)
    #
    #     text1 = font.render("- Press the spacebar to jump.\n- Avoid the triangles!\n- Jump and land on the platforms if necessary.\n- Collect hearts to own extra lives.\n- Collect stars to be unbeatable in the game for 15 seconds.\n - Click on the speaker icon at the right bottom to mute the game sounds.", True, PURPLE)
    #
    #     self.screen.blit(text1, (20, 20))

    def update(self):
        self.runner.update(self)

        # making background move
        self.bgX -= 2
        self.bgX2 -= 2
        if self.bgX < self.bg.get_width() * -1:
            self.bgX = self.bg.get_width()
        if self.bgX2 < self.bg.get_width() * -1:
            self.bgX2 = self.bg.get_width()

        # making obstacles disappear
        for obstacle in self.obstacles:
            obstacle.update(self.inDangerZone)
            if obstacle.x < -850:
                self.obstacles.pop(self.obstacles.index(obstacle))

        if not self.inDangerZone:
            for life in self.lifes:
                life.update(False)
                if life.x < -850:
                    self.lifes.pop(self.lifes.index(life))

            for boost in self.boost:
                boost.update(False)
                if boost.x < -850:
                    self.boost.pop(self.boost.index(boost))

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(self.imgSound, (740, 450))

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        self.runner.draw(self.screen)

        if not self.inDangerZone:
            for life in self.lifes:
                life.draw(self.screen)
            for boost in self.boost:
                boost.draw(self.screen)

            for life in self.lifebar:
                life.draw(self.screen)

        self.printScore()

        if self.invincible > 0:
            self.printInvTime()

        # after drawing everything, flip the display
        pygame.display.flip()

    def createObstacle(self):
        r = random.randrange(0, 6)
        l = random.randrange(0, 18)
        i = random.randrange(0, 20)
        if len(self.obstacles) == 0 or (self.obstacles[-1].num < 2 and self.obstacles[-1].x + self.obstacles[-1].width < 600) or (self.obstacles[-1].x + self.obstacles[-1].width < 480):
            if r == 0:
                self.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             0))
                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    self.boost.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 1:
                self.obstacles.append(
                    Obstacle(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')),
                             'triangle', 1))

                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    self.boost.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 2 and (len(self.obstacles) == 0 or (self.obstacles[-1].num != 2 and self.obstacles[-1].num != 4)):
                self.obstacles.append(
                    Obstacle(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')),
                             'rectangle', 2))
                self.obstacles.append(
                    Obstacle(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')),
                             'rectangle', 2))
                self.obstacles.append(
                    Obstacle(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')),
                             'rectangle', 2))
                self.obstacles.append(
                    Obstacle(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))
                self.obstacles.append(
                    Obstacle(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))

                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    self.boost.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 3:
                self.obstacles.append(
                    Obstacle(810, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')), 'rectangle',
                             3))
                self.obstacles.append(
                    Obstacle(1300, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),
                             'rectangle', 3))
                self.obstacles.append(
                    Obstacle(1197, 409, 99, 29, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')), 'triangle',
                             3))
                self.obstacles.append(
                    Obstacle(990, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                self.obstacles.append(
                    Obstacle(1480, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    self.boost.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 4 and (len(self.obstacles) == 0 or (self.obstacles[-1].num != 2 and self.obstacles[-1].num != 4)):
                self.obstacles.append(
                    Obstacle(810, 408, 303, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')),
                             'triangle', 4))
                self.obstacles.append(
                    Obstacle(810, 380, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                self.obstacles.append(
                    Obstacle(935, 320, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                self.obstacles.append(
                    Obstacle(1060, 260, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    self.boost.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 5:
                self.obstacles.append(
                    Obstacle(810, 350, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle',
                             5))
                self.obstacles.append(
                    Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')), 'triangle',
                             5))
                if l == 0 and self.numLives < 5:
                    self.lifes.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    self.boost.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))
                    
    def createObstacleDangerZone(self):
        r = random.randrange(0, 12)
        if len(self.obstacles) == 0 or (self.obstacles[-1].x + self.obstacles[-1].width < 650):
            if r < 4:
                self.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')), 'triangle',
                             1))
            elif r < 7:
                self.obstacles.append(
                    Obstacle(810, 375, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')), 'triangle',
                             0))
            elif r < 9 and (len(self.obstacles) == 0 or self.obstacles[-1].num != 2):
                self.obstacles.append(
                    Obstacle(810, 245, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo_Invertido_Danger_Zone.png')),
                             'triangle', 2))


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
