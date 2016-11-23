class Tank:
    def __init__(self, name, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.name = name

    def updatePosition(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction

    def getPosition(self):
        return self.x, self.y, self.direction