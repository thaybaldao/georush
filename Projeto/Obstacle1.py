from Background import *
import os
import pygame
from pygame.locals import *

class Obstacle1(Background):
    def __init__(self):
        super().__init__(810, 395, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle')


