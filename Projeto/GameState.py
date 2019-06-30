class GameState():

    def invincible(self, game):
        if int(game.invincible) is not 0:
            return True
        return False

    def haveExtraLives(self, game):
        if game.numLives is not 0:
            return True
        return False
