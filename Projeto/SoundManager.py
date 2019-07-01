import pygame
import os
vec = pygame.math.Vector2

class SoundManager():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)


    def playSong(self, song):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song), -1, fade_ms=200)


    def playSoundEffect(self, effect):
        pygame.mixer.Channel(0).set_volume(0.3)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(effect), 0)
        pygame.mixer.Channel(0).set_volume(1)


    def playDeath(self, effect):
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(effect), 0)