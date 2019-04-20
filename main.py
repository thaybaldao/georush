from Player import *
from Obstacles import *
from Settings import *
from pygame.locals import *
import pygame
import os
import random

class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()
        pygame.mixer.init()
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
        self.collisions = False
        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.speed = 150
        self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.reset = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.stop = pygame.image.load(os.path.join('Imagens', 'Play.png'))
        self.inst = pygame.image.load(os.path.join('Imagens', 'Instrucoes.png'))
        self.try_again = pygame.image.load(os.path.join('Imagens', 'Instrucoes.png'))
        self.title = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))
        self.game_over = pygame.image.load(os.path.join('Imagens', 'Titulo.png'))


    def show_start_screen(self):
        # game splash/start screen
        self.run_start_screen = True
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


    def update_start_screen(self):
        self.runner.update()

        if self.runner.pos.y >= BOTTOM_Y:
            self.runner.pos.y = BOTTOM_Y
            self.runner.vel.y = 0

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


    def show_reset_screen(self):
        # game over/continue
        self.run_reset_screen = True
        while self.run_reset_screen:
            self.clock.tick(self.speed)
            self.draw_reset_screen()
            self.update_start_screen()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # highlight hovering the button
                if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
                else:
                    self.reset = pygame.image.load(os.path.join('Imagens', 'Play.png'))
                if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'Play1.png'))
                else:
                    self.stop = pygame.image.load(os.path.join('Imagens', 'Play.png'))
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

    def draw_reset_screen(self):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(self.reset, (205, 140))
        self.screen.blit(self.stop, (455, 140))
        self.screen.blit(self.try_again, (75, 290))
        self.screen.blit(self.game_over, (225, 50))
        self.runner.draw(self.screen)
        pygame.display.flip()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(self.speed)
            self.events()
            self.update()
            self.draw()

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

            if event.type == USEREVENT + 1:
                self.speed += 1

            if event.type == USEREVENT + 2:
                r = random.randrange(0, 6)
                if r == 0:
                    self.obstacles.append(Obstacle(810, 395, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle', '1'))
                elif r == 1:
                    self.obstacles.append(Obstacle(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')), 'triangle','1_2'))
                elif r == 2:
                   if len(self.obstacles) == 0:
                       self.obstacles.append(Obstacle(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')), 'rectangle','2'))
                       self.obstacles.append(Obstacle(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')), 'rectangle', '2'))
                       self.obstacles.append(Obstacle(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')), 'rectangle','2'))
                       self.obstacles.append(Obstacle(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'triangle','2'))
                       self.obstacles.append(Obstacle(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'triangle','2'))
                   elif self.obstacles[len(self.obstacles) - 1].num != '4':
                        self.obstacles.append(Obstacle(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')), 'rectangle', '2'))
                        self.obstacles.append(Obstacle(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')), 'rectangle', '2'))
                        self.obstacles.append(Obstacle(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')), 'rectangle', '2'))
                        self.obstacles.append(Obstacle(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'triangle', '2'))
                        self.obstacles.append(Obstacle(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'triangle', '2'))
                elif r == 3:
                    self.obstacles.append(Obstacle(810, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')), 'rectangle','3'))
                    self.obstacles.append(Obstacle(1300, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')), 'rectangle','3'))
                    self.obstacles.append(Obstacle(1197, 409, 99, 29, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')), 'triangle','3'))
                    self.obstacles.append(Obstacle(990, 334, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle','3'))
                    self.obstacles.append(Obstacle(1480, 334, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle','3'))
                elif r == 4:
                    if len(self.obstacles) == 0:
                        self.obstacles.append(Obstacle(810, 408, 400, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')), 'triangle','4'))
                        self.obstacles.append(Obstacle(810, 370, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(935, 325, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(1060, 280, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(1185, 235, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                    elif self.obstacles[len(self.obstacles) - 1].num != '2':
                        self.obstacles.append(
                            Obstacle(810, 408, 400, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')),
                                     'triangle', '4'))
                        self.obstacles.append(
                            Obstacle(810, 370, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                                     'rectangle', '4'))
                        self.obstacles.append(
                            Obstacle(935, 325, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                                     'rectangle', '4'))
                        self.obstacles.append(
                            Obstacle(1060, 280, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                                     'rectangle', '4'))
                        self.obstacles.append(
                            Obstacle(1185, 235, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                                     'rectangle', '4'))
                elif r == 5:
                    self.obstacles.append(Obstacle(810, 300, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle', '5'))
                    self.obstacles.append(Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')), 'triangle', '5'))

    def checkCollisions(self):
        for obstacle in self.obstacles:
            obstacle.update()
            if self.runner.rect.colliderect(obstacle):
                if obstacle.type == 'rectangle' and self.runner.vel.y > 0:
                    self.runner.pos.y = obstacle.rect.top
                    self.runner.vel.y = 0
                    self.runner.obstacleOnTop = obstacle
                else:
                    game.show_reset_screen()
                    if self.playing:
                        self.playing = False
                    self.running = False



    def update(self):
        self.runner.update()

        if self.runner.pos.y >= BOTTOM_Y:
            self.runner.pos.y = BOTTOM_Y
            self.runner.vel.y = 0

        self.checkCollisions()

        # making background move
        self.bgX -= 2
        self.bgX2 -= 2
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

    def draw(self):
        # Game Loop - draw

        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))

        self.runner.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)


        # *after* drawing everything, flip the display
        pygame.display.flip()


game = Game()
game1 = Game()
game.show_start_screen()

while game.running and not game.run_start_screen and not game.run_reset_screen:
    game.run()

while game.retry:
    del game
    game = Game()
    while game.running and not game.run_start_screen and not game.run_reset_screen:
        game.run()
#game = Game()
#game.show_go_screen()
#while game.running and not game.run_start_screen:
#    game.run()

pygame.quit()






