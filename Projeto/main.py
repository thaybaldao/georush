from Player import *
from Obstacle import *
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
        self.collisions = False
        # initializing player and vector for obstacles
        self.runner = Player(self)
        self.obstacles = []
        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.speed = 150

        self.run()


    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

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

            #if event.type == USEREVENT + 1:
            #    self.speed += 1

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
                        self.obstacles.append(Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')), 'triangle','4'))
                        self.obstacles.append(Obstacle(810, 350, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(900, 280, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(990, 210, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                        self.obstacles.append(Obstacle(1080, 130, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle','4'))
                    elif self.obstacles[len(self.obstacles) - 1].num != '2':
                        self.obstacles.append(Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')), 'triangle', '4'))
                        self.obstacles.append(Obstacle(810, 350, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle', '4'))
                        self.obstacles.append(Obstacle(900, 280, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle', '4'))
                        self.obstacles.append(Obstacle(990, 210, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle', '4'))
                        self.obstacles.append(Obstacle(1080, 130, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle', '4'))
                elif r == 5:
                    self.obstacles.append(Obstacle(810, 300, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle', '5'))
                    self.obstacles.append(Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')), 'triangle', '5'))

    def checkCollisions(self):
        for obstacle in self.obstacles:
            obstacle.update()
            if self.runner.rect.colliderect(obstacle):
                if obstacle.type == 'rectangle' and self.runner.vel.y > 0:
                    self.runner.pos.y = obstacle.rect.top
                    self.runner.vel.y = 0
                else:
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
game.show_start_screen()

while game.running:
    game.show_go_screen()

pygame.quit()






