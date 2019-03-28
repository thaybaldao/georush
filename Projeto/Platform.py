class Platform():
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.x = obj1.x
        self.width = 306

    def draw(self, win):
        self.obj1.draw(win)
        self.obj2.draw(win)
        for obj in (self.obj1, self.obj2):
            if obj.x >= -850:
                obj.x -= 1.4
        self.x = self.obj1.x

    def collisionStatus(self, rect):
        if self.hitbox.colliderect(rect):
            if self.type == 'triangle':
                return 'death'
            else:
                x = self.hitbox.centerx - rect.centerx
                y = rect.centerx - self.hitbox.centerx
                collisionAngle = atan2(y, x)
                maxLateralCollisionAngle = atan2(self.hitbox.height + rect.height,
                                                 self.hitbox.width + rect.width)

                if collisionAngle > maxLateralCollisionAngle and collisionAngle < pi - maxLateralCollisionAngle:
                    return 'continue'

                return 'death'