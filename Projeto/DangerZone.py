from Zone import *


class DangerZone(Zone):
    def __init__(self):
        self.soundBehavior = SoundBehaviorDangZone()
        self.basicInitialization()
        self.commandsMediator.add(JumpCommand())


    def computeScore(self, game):
        game.score += 0.02


    def update(self, game):
        self.basicZoneUpdate(game)


    def createObstacle(self, game):
        r = random.randrange(0, 1000)
        if len(game.obstacles) == 0 or (game.obstacles[-1].x + game.obstacles[-1].width < 650):
            if r < 4:
                game.obstacles.append(TriObs(810,405,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')), 1))
            elif r < 7:
                game.obstacles.append(TriObs(810,375,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo_Danger_Zone.png')), 0))
            elif r < 9 and (len(game.obstacles) == 0 or game.obstacles[-1].num != 2):
                game.obstacles.append(TriObs(810,245,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo_Invertido_Danger_Zone.png')), 2))


    def drawDangerScreen(self, color, message, x, game):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.screen.blit(game.imgSound, (740, 450))
        game.runner.draw(self.screen)
        font = pygame.font.Font(os.path.join('Imagens', '04B_30__.TTF'), 55)
        text = font.render(message, True, color)
        self.screen.blit(text, (x, 225))
        pygame.display.flip()

    def dangerZoneMessage(self, game):
        game.obstacles.clear()
        pygame.time.wait(500)
        self.drawDangerScreen(PURPLE, 'DANGER ZONE!', 115, game)
        pygame.time.wait(400)
        self.drawDangerScreen(YELLOW, 'DANGER ZONE!', 115, game)
        pygame.time.wait(500)
        self.drawDangerScreen(PURPLE, 'DANGER ZONE!', 115, game)
        pygame.time.wait(400)

    def wellDoneMessage(self, game):
        game.obstacles.clear()
        pygame.time.wait(500)
        self.drawDangerScreen(PURPLE, 'WELL DONE!', 160, game)
        pygame.time.wait(400)
        self.drawDangerScreen(YELLOW, 'WELL DONE!', 160, game)
        pygame.time.wait(500)
        self.drawDangerScreen(PURPLE, 'WELL DONE!', 160, game)
        pygame.time.wait(400)


    def draw(self, game):
        self.basicZoneDraw(game)

        # after drawing everything, flip the display
        pygame.display.flip()