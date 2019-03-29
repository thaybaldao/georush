from Player import *
from Obstacle1 import *
from Obstacle1_2 import *
from Obstacle2 import *
from Obstacle2_1 import *
from Obstacle2_2 import *
from Obstacle2_3 import *
from Obstacle2_4 import *
from Obstacle2_5 import *
from Obstacle3 import *
from Obstacle3_1 import *
from Obstacle3_2 import *
from Obstacle3_3 import *
from Obstacle3_4 import *
from Obstacle3_5 import *
from Obstacle4 import *
from Obstacle4_1 import *
from Obstacle4_2 import *
from Obstacle4_3 import *
from Obstacle4_4 import *
from Obstacle4_5 import *
from Platform import *
from Platform_1 import *
from Platform_2 import *
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

        collisions = 'False'

    def new(self):
        # initializing player and vector for obstacles
        self.runner = Player()
        self.obstacles = []
        # creating background
        self.bg = pygame.image.load(os.path.join('Imagens', 'Background.png')).convert()
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.speed = 50

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(self.speed)
            self.events()
            self.update()
            self.draw()

    def update(self):
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
                    self.runner.jumping = True

            if event.type == USEREVENT + 1:
                self.speed += 1

            if event.type == USEREVENT + 2:
                r = random.randrange(0, 6)
                if r == 0:
                    self.obstacles.append(Obstacle1())
                elif r == 1:
                    self.obstacles.append(Obstacle1_2())
                elif r == 2:
                   if len(self.obstacles) == 0:
                       self.obstacles.append(
                           Obstacle2(Obstacle2_1(), Obstacle2_2(), Obstacle2_3(), Obstacle2_4(), Obstacle2_5()))
                   elif self.obstacles[len(self.obstacles) - 1].num != '4':
                        self.obstacles.append(
                            Obstacle2(Obstacle2_1(), Obstacle2_2(), Obstacle2_3(), Obstacle2_4(), Obstacle2_5()))
                elif r == 3:
                    self.obstacles.append(
                        Obstacle3(Obstacle3_1(), Obstacle3_2(), Obstacle3_3(), Obstacle3_4(), Obstacle3_5()))
                elif r == 4:
                    if len(self.obstacles) == 0:
                        self.obstacles.append(
                            Obstacle4(Obstacle4_1(), Obstacle4_2(), Obstacle4_3(), Obstacle4_4(), Obstacle4_5()))
                    elif self.obstacles[len(self.obstacles) - 1].num != '2':
                        self.obstacles.append(
                            Obstacle4(Obstacle4_1(), Obstacle4_2(), Obstacle4_3(), Obstacle4_4(), Obstacle4_5()))
                elif r == 5:
                    self.obstacles.append(Platform(Platform_1(), Platform_2()))

            for obstacle in self.obstacles:
                if obstacle.collisionStatus(self.runner.hitbox) == 'continue' or obstacle.collisionStatus(
                        self.runner.hitbox) == 'death':
                    print("colission status: ", obstacle.collisionStatus(self.runner.hitbox), "\n\n")
                # if obstacle.collisionStatus(runner.hitbox) == 'death':
                #    runner.jumping = False
                #    run = False




    def draw(self):
        # Game Loop - draw

        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))

        self.runner.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

game = Game()
game.show_start_screen()
game.new()

while game.running:
    game.show_go_screen()

pygame.quit()






