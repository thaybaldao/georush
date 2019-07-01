from Zone import *

class RegularZone(Zone):
    def __init__(self):
        self.soundBehavior = SoundBehaviorRegZone()
        self.basicInitialization()
        self.commandsMediator.add(JumpCommand())


    def update(self, game):
        self.basicZoneUpdate(game)

        # make lives dissapear
        for life in game.lives:
            life.update()
            if life.x < -850:
                game.lives.pop(game.lives.index(life))

        # make boosters dissapear
        for boost in game.boost:
            boost.update()
            if boost.x < -850:
                game.boost.pop(game.boost.index(boost))


    def createObstacle(self, game):
        r = random.randrange(0, 6)
        l = random.randrange(0, 18)
        i = random.randrange(0, 20)
        if len(game.obstacles) == 0 or (
                game.obstacles[-1].num < 2 and game.obstacles[-1].x + game.obstacles[-1].width < 600) or (
                game.obstacles[-1].x + game.obstacles[-1].width < 480):
            if r == 0:
                game.obstacles.append(TriObs(810,405,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo.png')), 0))
                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(950,400))
                elif i == 0:
                    game.boost.append(Boost(950,400))

            elif r == 1:
                game.obstacles.append(TriObs(810,245,118,48,pygame.image.load(os.path.join('Imagens', 'Triangulos_inverso.png')),1))

                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(810,400))
                elif i == 0:
                    game.boost.append(Boost(810,400))

            elif r == 2 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(RectObs(810,375,45,64,pygame.image.load(os.path.join('Imagens', 'Obstaculo2_1.png')),2))
                game.obstacles.append(RectObs(940,314,45,126,pygame.image.load(os.path.join('Imagens', 'Obstaculo2_2.png')),2))
                game.obstacles.append(RectObs(1070,243,45,197,pygame.image.load(os.path.join('Imagens', 'Obstaculo2_3.png')),2))
                game.obstacles.append(TriObs(858,409,82,33,pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),2))
                game.obstacles.append(TriObs(988,409,82,33,pygame.image.load(os.path.join('Imagens', 'Obstaculo2_4.png')),2))

                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(940,275))

                elif i == 0:
                    game.boost.append(Boost(940,275))

            elif r == 3:
                game.obstacles.append(RectObs(810,380,379,60,pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),3))
                game.obstacles.append(RectObs(1300,380,379,60,pygame.image.load(os.path.join('Imagens', 'Obstaculo3_1.png')),3))
                game.obstacles.append(TriObs(1197,409,99,29,pygame.image.load(os.path.join('Imagens', 'Obstaculo3_2.png')),3))
                game.obstacles.append(TriObs(990,347,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo.png')),3))
                game.obstacles.append(TriObs(1480,347,35,36,pygame.image.load(os.path.join('Imagens', 'Triangulo.png')),3))
                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(900,340))
                elif i == 0:
                    game.boost.append(Boost(900,340))

            elif r == 4 and (len(game.obstacles) == 0 or (game.obstacles[-1].num != 2 and game.obstacles[-1].num != 4)):
                game.obstacles.append(TriObs(810,408,303,33,pygame.image.load(os.path.join('Imagens', 'Obstaculo4_1.png')),4))
                game.obstacles.append(RectObs(810,380,51,13,pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),4))
                game.obstacles.append(RectObs(935,320,51,13,pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),4))
                game.obstacles.append(RectObs(1060,260,51,13,pygame.image.load(os.path.join('Imagens', 'Obstaculo4_2.png')),4))
                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(935,280))

                elif i == 0:
                    game.boost.append(Boost(935,280))

            elif r == 5:
                game.obstacles.append(RectObs(810,350,306,38,pygame.image.load(os.path.join('Imagens', 'Plataforma.png')),5))
                game.obstacles.append(TriObs(810,408,306,33,pygame.image.load(os.path.join('Imagens', 'Espinhos_Plat.png')),5))
                if l == 0 and game.numLives < 5:
                    game.lives.append(Life(900,310))
                elif i == 0:
                    game.boost.append(Boost(900,310))



    def draw(self, game):
        self.basicZoneDraw(game)

        # draw lives
        for life in game.lives:
            life.draw(self.screen)

        # draw boosters
        for boost in game.boost:
            boost.draw(self.screen)

        # after drawing everything, flip the display
        pygame.display.flip()
