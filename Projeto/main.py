from Player import *
from Obstacle1 import *
from Obstacle1_2 import *
from Obstacle2 import *
from Obstacle3 import *
from Obstacle4 import *
from Platform import *
from Obstacle import *
import pygame
from pygame.locals import *
import os
import random

# initializing pygame
pygame.init()

# creating game window
W, H = 800, 500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Geo Rush')

# creating background
bg = pygame.image.load(os.path.join('Imagens','Background.png')).convert()
bgX = 0
bgX2 = bg.get_width()
speed = 50

# creating obstacles vector
obstacles = []

# setting up clock
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT + 1, 500)
pygame.time.set_timer(USEREVENT + 2, 6000)

# creating runner
runner = Player()

collisions = 'False'

def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))

    runner.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.update()

# starting game
run = True

# main loop
while run:

    for obstacle in obstacles:
        if obstacle.x < -850:
            obstacles.pop(obstacles.index(obstacle))
        else:
            obstacle.x -= 1.4

    bgX -= 2
    bgX2 -= 2

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            run = False
            break

        if event.type == USEREVENT + 1:
            speed += 1

        if event.type == USEREVENT + 2:
            r = random.randrange(0, 6)
            if r == 0: ##Está com bug, aparecendo muito próximo e estão colidindo
                obstacles.append(Obstacle1())
            elif r == 1:
                obstacles.append(Obstacle1_2())
            elif r == 2:
                obstacles.append(Obstacle2())
            elif r == 3:
                obstacles.append(Obstacle3())
            elif r == 4:
                obstacles.append(Obstacle4())
            elif r == 5:
               obstacles.append(Platform())

        keys = pygame.key.get_pressed()

        if runner.x < W - runner.width - runner.vel:
            if keys[pygame.K_SPACE]:
                if not (runner.jumping):
                    runner.jumping = True

    if run != False:
        redrawWindow()

    clock.tick(speed)