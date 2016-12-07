from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * pi * 2

aCircle = Circle(2)
print(aCircle.area())

