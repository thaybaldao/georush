from Zone import *

class RegularZone(Zone):
    def __init__(self):
        pass

    def update(self, game):
        self.basicZoneUpdate(game)

        # make lives dissapear
        for life in game.lives:
            life.update(False)
            if life.x < -850:
                game.lives.pop(game.lives.index(life))

        # make boosters dissapear
        for boost in game.boost:
            boost.update(False)
            if boost.x < -850:
                game.boost.pop(game.boost.index(boost))

    def draw(self, game):
        self.basicZoneDraw(game)

        # draw lives
        for life in game.lives:
            life.draw(game.screen)

        # draw boosters
        for boost in game.boost:
            boost.draw(game.screen)

        # after drawing everything, flip the display
        pygame.display.flip()

    def createObstacle(self, game):
        r = random.randrange(0, 6)
        l = random.randrange(0, 18)
        i = random.randrange(0, 20)
        if len(game.obstacles) == 0 or (
                game.obstacles[-1].num < 2 and game.obstacles[-1].x + game.obstacles[-1].width < 600) or (
                game.obstacles[-1].x + game.obstacles[-1].width < 480):
            if r == 0:
                game.obstacles.append(
                    Obstacle(810, 405, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             0))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(950, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 1:
                game.obstacles.append(
                    Obstacle(810, 245, 118, 48, pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')),
                             'triangle', 1))

                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(810, 400, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 2 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(
                    Obstacle(810, 375, 45, 64, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(940, 314, 45, 126, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(1070, 243, 45, 197, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')),
                             'rectangle', 2))
                game.obstacles.append(
                    Obstacle(858, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))
                game.obstacles.append(
                    Obstacle(988, 409, 82, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),
                             'triangle', 2))

                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    game.boost.append(
                        Obstacle(940, 275, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 3:
                game.obstacles.append(
                    Obstacle(810, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),
                             'rectangle',
                             3))
                game.obstacles.append(
                    Obstacle(1300, 380, 379, 60, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),
                             'rectangle', 3))
                game.obstacles.append(
                    Obstacle(1197, 409, 99, 29, pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')),
                             'triangle',
                             3))
                game.obstacles.append(
                    Obstacle(990, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                game.obstacles.append(
                    Obstacle(1480, 347, 35, 36, pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 'triangle',
                             3))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(900, 340, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 4 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(
                    Obstacle(810, 408, 303, 33, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')),
                             'triangle', 4))
                game.obstacles.append(
                    Obstacle(810, 380, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                game.obstacles.append(
                    Obstacle(935, 320, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                game.obstacles.append(
                    Obstacle(1060, 260, 51, 13, pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),
                             'rectangle', 4))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')),
                                 'life', 'x'))

                elif i == 0:
                    game.boost.append(
                        Obstacle(935, 280, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))

            elif r == 5:
                game.obstacles.append(
                    Obstacle(810, 350, 306, 38, pygame.image.load(os.path.join('Imagens', 'Plataforma.png')),
                             'rectangle',
                             5))
                game.obstacles.append(
                    Obstacle(810, 408, 306, 33, pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')),
                             'triangle',
                             5))
                if l == 0 and game.numLives < 5:
                    game.lives.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Vida.png')), 'life',
                                 'x'))
                elif i == 0:
                    game.boost.append(
                        Obstacle(900, 310, 46, 39, pygame.image.load(os.path.join('Imagens', 'Star.png')), 'boost',
                                 'x'))