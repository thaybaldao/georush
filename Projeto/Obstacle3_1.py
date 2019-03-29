from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle3_1(Obstacle):
    def __init__(self):
        super().__init__(810, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')), 'rectangle')