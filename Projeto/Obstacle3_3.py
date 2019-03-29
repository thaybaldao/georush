from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle3_3(Obstacle):
    def __init__(self):
        super().__init__(1197, 409, 99, 29, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')), 'rectangle','3')