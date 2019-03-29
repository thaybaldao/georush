from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle3_4(Obstacle):
    def __init__(self):
        super().__init__(990, 334, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle','3')