from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle4_5(Obstacle):
    def __init__(self):
        super().__init__(1080, 130, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')), 'rectangle')