import math
from dotClass import Point

class Line:
    def __init__(self, points=[Point()]):
        self.points = points

    def __str__(self):
        output = 'Array of Stored Points: ['
        for i in self.points:
            output += str((i.x,i.y))+','
        output +=']'
        return output
            
    def add_point(self,p):
        self.points.append(p)

    def total_distance(self):
        count = Point()
        output = 0
        for p in self.points:
            output += count.distance(p)
            count = p
        return output

line_object = Line()
point_1 = Point(3,4)
point_2 = Point(5,1)

print(line_object)
line_object.add_point(point_1)
line_object.add_point(point_2)
print(line_object)
print(line_object.total_distance())
