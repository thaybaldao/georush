from Background import *
import os
import pygame
from pygame.locals import *

class Obstacle3(Background):
    def __init__(self):
        super().__init__(810, 380, 835, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3.png')), 'rectangle')
