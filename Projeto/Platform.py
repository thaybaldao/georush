from Background import *
import os
import pygame
from pygame.locals import *

class Platform(Background):
    def __init__(self):
        super().__init__(810, 300, 303, 200, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')))