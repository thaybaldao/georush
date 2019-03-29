from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle2_1(Obstacle):
    def __init__(self):
        super().__init__(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')), 'rectangle')