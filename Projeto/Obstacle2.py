class Obstacle2():
    def __init__(self, obj1, obj2, obj3, obj4, obj5):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.obj5 = obj5
        self.x = obj2.x
        self.width = 200

    def draw(self, win):
        self.obj1.draw(win)
        self.obj2.draw(win)
        self.obj3.draw(win)
        self.obj4.draw(win)
        self.obj5.draw(win)
        for obj in (self.obj1, self.obj2, self.obj3, self.obj4, self.obj5):
            if obj.x >= -850:
                obj.x -= 1.4
        self.x = self.obj2.x
