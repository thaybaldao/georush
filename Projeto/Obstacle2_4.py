from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle2_4(Obstacle):
    def __init__(self):
        super().__init__(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')), 'rectangle')