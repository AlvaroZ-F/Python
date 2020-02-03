

class minimum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<{}>'.format(self.x)

something = minimum(0,0)
print(something.x)
