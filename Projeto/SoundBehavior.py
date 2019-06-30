import pygame
import os

class SoundBehavior():
    def setNoSoundBehavior(self, game):
        game.sound = False
        game.imgSound = pygame.image.load(os.path.join('Imagens', 'No_Sound.png'))
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(1).stop()

    def setSoundBehavior(self,game):
        pass

    def soundButtonBehavior(self, game, pos):
        if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
            if game.sound:
                self.setNoSoundBehavior(game)
            else:
                self.setSoundBehavior(game)

class SoundBehaviorScreen(SoundBehavior):
    def setSoundBehavior(self,game):
        game.sound = True
        game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        game.soundManager.playSong(os.path.join('Music', 'menuLoop.wav'))

class SoundBehaviorRegZone(SoundBehavior):
    def setSoundBehavior(self,game):
        game.sound = True
        game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        game.soundManager.playSong(os.path.join('Music', 'BackOnTrack.wav'))

class SoundBehaviorDangZone(SoundBehavior):
    def setSoundBehavior(self,game):
        game.sound = True
        game.imgSound = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        game.soundManager.playSong(os.path.join('Music', 'DeadLocked.wav'))