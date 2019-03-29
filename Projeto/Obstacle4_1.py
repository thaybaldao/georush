from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle4_1(Obstacle):
    def __init__(self):
        super().__init__(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')), 'rectangle')
