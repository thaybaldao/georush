from Obstacle import *
import os
import pygame
from pygame.locals import *

class Obstacle2_3(Obstacle):
    def __init__(self):
        super().__init__(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')), 'rectangle','2')