import pygame
from pygame.locals import *
import os

class Background:
    def __init__(self, x, y, width, height, img):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img = img

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
