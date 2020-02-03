import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point:({},{})".format(self.x, self.y)

    def distance(self, p):
        return (math.sqrt((p.x-self.x)**2+(p.y-self.y)**2))

point_1 = Point(3,5)
point_2 = Point(2,9)

print(point_1.distance(point_2))
