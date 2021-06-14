from math import pi

from . import Shape


class Circle(Shape):
    def __init__(self, radius):
        # noinspection PyCompatibility
        super().__init__()
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * pi * 2


aCircle = Circle(2)
print(aCircle.area())
