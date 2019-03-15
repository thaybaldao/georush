from player import *
from obstacle_1 import *
from obstacle_2 import *
import pygame
from pygame.locals import *
import os
import random

pygame.init()

W, H = 800, 500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Geo Rush')

bg = pygame.image.load(os.path.join('Imagens','Background.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    runner.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)
    pygame.display.update()

pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, 3000)
speed = 50
run = True
runner = Player(30,378,75,75)
obstacles = []

while run:

    for obstacle in obstacles:
        if obstacle.x < -350:
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
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == USEREVENT+1:
            speed += 1
        if event.type == USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0: ##Está com bug, aparecendo muito próximo e estão colidindo
                obstacles.append(Obstacle_1(810, 395, 50,50))
            elif r == 1:
                obstacles.append(Obstacle_2(810, 235, 338, 219))

    if run != False:
        redrawWindow()

    clock.tick(speed)