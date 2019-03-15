from obstacle_1 import *
import os
import pygame
from pygame.locals import *

class Platform(Obstacle_1):
    img = pygame.image.load(os.path.join('Imagens', 'Plataforma.png'))