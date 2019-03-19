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
        # hitbox(x_right, x_left, y_top, y_bottom)
        self.hitbox = (self.x + width/2, self.x - width/2, self.y + height/2, self.y - height/2)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

