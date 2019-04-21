from Player import *
from Obstacles import *
from Settings import *
from pygame.locals import *
import pygame
import os
import random

class Game:
    def __init__(self, highScore):
        # initializing pygame
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('BackOnTrack.wav')
        self.menu_sound = pygame.mixer.Sound('menuLoop.wav')
        # creating game window
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(TITLE)
        # setting up clock
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(USEREVENT + 1, 500)
        pygame.time.set_timer(USEREVENT + 2, 6000)
        self.running = True
        self.run_start_screen = False

        self.run_reset_screen = False
        self.retry = False

        self.n_lifes = 0

        self.collisions = False
        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        self.lifes = []
        self.lifebar = []
        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.initialSpeed = 250
        self.speed = self.initialSpeed
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))
        self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))
        self.inst = pygame.image.load(os.path.join('Imagens', 'Instrucoes.png'))
        self.try_again = pygame.image.load(os.path.join('Imagens', 'Best_Score.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.game_over = pygame.image.load(os.path.join('Imagens', 'Game_Over.png'))
        pygame.key.set_repeat(17, 17)

        # setting score
        self.score = 0
        self.highScore = highScore


    def showStartScreen(self):
        # game splash/start screen
        self.run_start_screen = True
        pygame.mixer.Sound.play(self.menu_sound, -1)
        while self.run_start_screen:
            self.clock.tick(self.speed)
            self.draw_start_screen()
            self.update_start_screen()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # highlight hovering the button
                if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
                else:
                    self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.run_start_screen = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                        self.run_start_screen = False
                if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.run_start_screen = False
        pygame.mixer.Sound.fadeout(self.menu_sound, 300)


    def update_start_screen(self):
        self.runner.update(self)

        # making background move
        self.bgX -= 2
        self.bgX2 -= 2
        if self.bgX < self.bg.get_width() * -1:
            self.bgX = self.bg.get_width()
        if self.bgX2 < self.bg.get_width() * -1:
            self.bgX2 = self.bg.get_width()

    def draw_start_screen(self):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(self.play, (340, 140))
        self.screen.blit(self.inst, (75, 290))
        self.screen.blit(self.title, (225, 50))
        self.runner.draw(self.screen)
        pygame.display.flip()


    def printScore(self):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)

        text = font.render("Score: "+str(int(self.score)), True, ORANGE)

        self.screen.blit(text, (480, 10))



    def printFinalScore(self):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 40)

        text1 = font.render("Your Score: " + str(int(self.score)), True, PURPLE)
        text2 = font.render("Best Score: " + str(int(self.highScore)), True, PURPLE)

        self.screen.blit(text1, (180, 300))
        self.screen.blit(text2, (180, 350))


    def showResetScreen(self):
        # game over/continue
        self.run_reset_screen = True
        pygame.mixer.Sound.play(self.menu_sound, -1)
        while self.run_reset_screen:
            self.clock.tick(self.speed)
            self.draw_reset_screen()
            self.runner.update(self)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # highlight hovering the button
                if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Replay1.png'))
                else:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))
                if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'X_button1.png'))
                else:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[
                    pygame.K_ESCAPE]:
                    self.run_reset_screen = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                        self.retry = True
                        self.run_reset_screen = False
                    if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                        self.run_reset_screen = False
        pygame.mixer.Sound.fadeout(self.menu_sound, 300)

    def draw_reset_screen(self):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(self.reset, (205, 140))
        self.screen.blit(self.stop, (455, 140))
        self.screen.blit(self.game_over, (190, 50))
        self.runner.draw(self.screen)

        self.printFinalScore()

        pygame.display.flip()


    def run(self):
        # Game Loop
        self.playing = True
        pygame.mixer.music.play(-1)
        while self.playing:
            self.clock.tick(self.speed)
            self.events()
            self.update()
            self.draw()
            self.score = (self.score + 0.01)
            if self.score > self.highScore:
                self.highScore = self.score

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.runner.jump()

            if event.type == USEREVENT + 2:
                self.speed += 1

            if event.type == USEREVENT + 1:
                self.createObstacle()

    def update(self):
        self.runner.update(self)

        # making background move
        self.bgX -= 1.5
        self.bgX2 -= 1.5
        if self.bgX < self.bg.get_width() * -1:
            self.bgX = self.bg.get_width()
        if self.bgX2 < self.bg.get_width() * -1:
            self.bgX2 = self.bg.get_width()

        # making obstacles disappear
        for obstacle in self.obstacles:
            if obstacle.x < -850:
                self.obstacles.pop(self.obstacles.index(obstacle))
            else:
                obstacle.x -= 1.4

        for life in self.lifes:
            if life.x < -850:
                self.lifes.pop(self.lifes.index(life))
            else:
                life.x -= 1.4

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))

        self.runner.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        for life in self.lifes:
            life.draw(self.screen)

        for life in self.lifebar:
            life.draw(self.screen)

        self.printScore()

        # *after* drawing everything, flip the display
        pygame.display.flip()


    def createObstacle(self):
        r = random.randrange(0, 6)
        l = random.randrange(0, 7)
        if len(self.obstacles) == 0 or (self.obstacles[-1].num < 2 and self.obstacles[-1].x + self.obstacles[-1].width < 600) or (self.obstacles[-1].x + self.obstacles[-1].width < 480):
            if r == 0:
                self.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             0))
                if l == 0:
                    self.lifes.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))

            elif r == 1:
                self.obstacles.append(
                    Obstacle(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')),
                             'triangle', 1))

                if l == 0:
                    self.lifes.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
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

                if l == 0:
                    self.lifes.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

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
                if l == 0:
                    self.lifes.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
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
                if l == 0:
                    self.lifes.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

            elif r == 5:
                self.obstacles.append(
                    Obstacle(810, 350, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle',
                             5))
                self.obstacles.append(
                    Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')), 'triangle',
                             5))
                if l == 0:
                    self.lifes.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))




highScore = 0
game = Game(highScore)
game.showStartScreen()

while game.running and not game.run_start_screen and not game.run_reset_screen:
    game.run()

while game.retry:
    highScore = game.highScore
    del game
    game = Game(highScore)
    while game.running and not game.run_start_screen and not game.run_reset_screen:
        game.run()

pygame.quit()
