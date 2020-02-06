import math
from dotClass import Point

class Line:
    def __init__(self, points=[Point()]):
        self.points = points

    def __str__(self):
        output = 'Array of Stored Points: ['
        for i in self.points:
            output += str((i.x, i.y)) + ','
        output += ']'
        return output

    def __dir__(self):
        methods = ["add_point(self,p)", "total_distance(self)", "quadrant(self)", "subclass: Line_plain"]
        return methods
            
    def add_point(self,p):
        self.points.append(p)

    def total_distance(self):
        count = Point()
        output = 0
        for p in self.points:
            output += count.distance(p)
            count = p
        return output
    
    def quadrant(self):
        output = {}
        for point in self.points:
            if point.x > 0 and point.y > 0:
                output[str(point)] = "Belongs to the first quadrant"
            elif point.x < 0 and point.y > 0:
                output[str(point)] = "Belongs to the second quadrant"
            elif point.x < 0 and point.y < 0:
                output[str(point)] = "Belongs to the third quadrant"
            elif point.x > 0 and point.y < 0:
                output[str(point)] = "Belongs to the fourth quadrant"
            elif point.x != 0 and point.y == 0:
                output[str(point)] = "It's situated over the X axis"
            elif point.x == 0 and point.y != 0:
                output[str(point)] = "It's situated over the Y axis"
            else:
                output[str(point)] = "It's situated over the origin"
        return output

class Line_plain(Line):
    def __init__(self, points):
        Line.__init__(self, points)
        self.linex = []
        for point in self.points:
            self.linex.append(point.x)

    def __str__(self):
        output = 'List of axis X points: ['
        for i in self.linex:
            output += str((i)) + ','
        output += ']'
        return output

line_object = Line()
point_1 = Point(3,4)
point_2 = Point(5,1)
point_3 = Point(15,2)

print(line_object)
line_object.add_point(point_1)
line_object.add_point(point_2)
line_object.add_point(point_3)
print(line_object)
print(line_object.total_distance())
for i in line_object.quadrant():
    print (i)

print(dir(line_object))

line_x_object = Line_plain(line_object.points)
print(line_x_object)
