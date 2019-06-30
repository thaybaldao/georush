class GameState():
    def __init__(self, game):
        self.game = game

    def invincible(self):
        if int(self.game.invincible) is not 0:
            return True
        return False

    def haveExtraLifes(self):
        if self.game.numLives is not 0:
            return True
        return False
