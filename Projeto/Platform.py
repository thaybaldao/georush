from Background import *
import os
import pygame
from pygame.locals import *

class Platform(Background):
    def __init__(self):
        super().__init__(810, 300, 526, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')), 'rectangle')
