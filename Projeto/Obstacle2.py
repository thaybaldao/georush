from math import *

class Obstacle2():
    def __init__(self, obj1, obj2, obj3, obj4, obj5):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.obj5 = obj5
        self.x = (obj1.x + obj2.x + obj3.x + obj4.x + obj5.x)/5
        self.objects = [obj1, obj2, obj3, obj4, obj5]


    def draw(self, win):
        self.obj1.draw(win)
        self.obj2.draw(win)
        self.obj3.draw(win)
        self.obj4.draw(win)
        self.obj5.draw(win)
        for object in self.objects:
            if object.x >= -850:
                object.x -= 1.4

        self.x = (self.obj1.x + self.obj2.x + self.obj3.x + self.obj4.x + self.obj5.x) / 5

    def collisionStatus(self, rect):
        for object in self.objects:
            if object.hitbox.colliderect(rect):
                if object.type == 'triangle':
                    return 'death'
                else:
                    x = object.hitbox.centerx - rect.centerx
                    y = rect.centerx - object.hitbox.centerx
                    collisionAngle = atan2(y, x)
                    maxLateralCollisionAngle = atan2(object.hitbox.height + rect.height, object.hitbox.width + rect.width)

                    if collisionAngle > maxLateralCollisionAngle and collisionAngle < pi - maxLateralCollisionAngle:
                        return 'continue'

                    return 'death'

