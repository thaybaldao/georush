from Background import *
import os
import pygame
from pygame.locals import *

class Obstacle2(Background):
    def __init__(self):
        super().__init__(810, 240, 303, 200, pygame.image.load(os.path.join('Imagens', 'Obstaculo2.png')), 'rectangle')
