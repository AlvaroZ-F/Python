import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Point:({},{})".format(self.x, self.y)

    def add(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def substract(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def distance(self, p):
        return (math.sqrt((p.x-self.x)**2+(p.y-self.y)**2))
