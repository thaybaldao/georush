from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle3_5(Obstacle):
    def __init__(self):
        super().__init__(1480, 334, 50, 48, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle','3')