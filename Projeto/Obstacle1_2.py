from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle1_2(Obstacle):
    def __init__(self):
        super().__init__(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')), 'triangle')

