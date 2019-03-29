from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle2_5(Obstacle):
    def __init__(self):
        super().__init__(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'rectangle')