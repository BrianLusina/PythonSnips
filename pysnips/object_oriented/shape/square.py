from object_oriented.shape import Shape


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length


aSquare = Square(3)
print(aSquare.area())
