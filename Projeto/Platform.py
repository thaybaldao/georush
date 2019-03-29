from math import *

class Platform():
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.x = obj1.x
        self.width = 306
        self.objects = [obj1, obj2]
        self.num = '5'

    def draw(self, win):
        self.obj1.draw(win)
        self.obj2.draw(win)
        for obj in (self.obj1, self.obj2):
            if obj.x >= -850:
                obj.x -= 1.4
        self.x = self.obj1.x

    def collisionStatus(self, rect):
        for object in self.objects:
            if object.hitbox.colliderect(rect):
                if object.type == 'triangle':
                    return 'death'
                else:
                    x = object.hitbox.centerx - rect.centerx
                    y = rect.centerx - object.hitbox.centerx
                    collisionAngle = atan2(y, x)
                    maxLateralCollisionAngle = atan2(object.hitbox.height + rect.height,
                                                     object.hitbox.width + rect.width)

                    if collisionAngle > maxLateralCollisionAngle and collisionAngle < pi - maxLateralCollisionAngle:
                        return 'continue'

                    return 'death'