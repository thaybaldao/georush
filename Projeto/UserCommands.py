import pygame
import os
from Settings import *

class Command:
    def check(self, event, pos, game, screen):
        pass

    def execute(self, game, screen):
        pass


class QuitGameCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.runScreen = False
        game.running = False
        game.retry = False


class HighlightPlayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.play = pygame.image.load(os.path.join('Imagens', 'Play1.png'))

class NotHighlightPlayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] <= 340 or pos[0] >= 468 or pos[1] <= 140 or pos[1] >= 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))

class PlayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 340 and pos[0] < 468 and pos[1] > 140 and pos[1] < 259:
                self.execute(game, screen)

    def execute(self, game, screen):
        screen.runScreen = False


class HighlightInstructionsButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.inst = screen.font.render('INSTRUCTIONS', True, YELLOW)

class NotHighlightInstructionsButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] <= 200 or pos[0] >= 615 or pos[1] <= 290 or pos[1] >= 330:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.inst = screen.font.render('INSTRUCTIONS', True, PURPLE)

class InstructionsButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 200 and pos[0] < 615 and pos[1] > 290 and pos[1] < 330:
                self.execute(game, screen)

    def execute(self, game, screen):
        screen.runScreen = False
        game.instructionsScreen.runScreen = True


class HighlightReplayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.reset = pygame.image.load(os.path.join('Imagens', 'Replay1.png'))

class NotHighlightReplayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] <= 205 or pos[0] >= 333 or pos[1] <= 140 or pos[1] >= 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.reset = pygame.image.load(os.path.join('Imagens', 'Replay.png'))

class ReplayButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 205 and pos[0] < 333 and pos[1] > 140 and pos[1] < 259:
                self.execute(game, screen)

    def execute(self, game, screen):
        screen.retry = True
        screen.runScreen = False
        game.inDangerZone = False


class HighlightXButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.stop = pygame.image.load(os.path.join('Imagens', 'X_button1.png'))

class NotHighlightXButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] <= 455 or pos[0] >= 583 or pos[1] <= 140 or pos[1] >= 259:
            self.execute(game, screen)

    def execute(self, game, screen):
        screen.stop = pygame.image.load(os.path.join('Imagens', 'X_button.png'))

class XButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 455 and pos[0] < 583 and pos[1] > 140 and pos[1] < 259:
                self.execute(game, screen)

    def execute(self, game, screen):
        screen.retry = False
        screen.runScreen = False
        game.running = False


class SoundButtonCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495:
                self.execute(game, screen)

    def execute(self, game, screen):
        if game.sound:
            screen.soundBehavior.setNoSoundBehavior(game)
        else:
            screen.soundBehavior.setSoundBehavior(game)


class JumpCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.execute(game, screen)

    def execute(self, game, screen):
        game.runner.jump()


class HighlightAdvanceToGameTextCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] > 280 and pos[0] < 780 and pos[1] > 410 and pos[1] < 430:
            self.execute(game, screen)

    def execute(self, game, screen):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)
        screen.play = font.render('Press ENTER or CLICK HERE to play.', True, YELLOW)

class NotHighlightAdvanceToGameTextCommand(Command):
    def check(self, event, pos, game, screen):
        if pos[0] <= 280 or pos[0] >= 780 or pos[1] <= 410 or pos[1] >= 430:
            self.execute(game, screen)

    def execute(self, game, screen):
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 17)
        screen.play = font.render('Press ENTER or CLICK HERE to play.', True, PURPLE)

class AdvanceToGameTextCommand(Command):
    def check(self, event, pos, game, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 280 and pos[0] < 780 and pos[1] > 410 and pos[1] < 430:
                self.execute(game, screen)

    def execute(self, game, screen):
        screen.runScreen = False


class CommandsInterpreter:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self, game, screen):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            for c in self.commands:
                c.check(event, pos, game, screen)
