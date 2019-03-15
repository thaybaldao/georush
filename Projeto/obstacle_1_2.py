from obstacle_1 import *
import os
import pygame
from pygame.locals import *

class Obstacle_1_2(Obstacle_1):
    img = pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png'))