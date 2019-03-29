from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle2_2(Obstacle):
    def __init__(self):
        super().__init__(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')), 'rectangle')