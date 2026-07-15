class Point:
    """
    Defines the blueprint of a specific point on the word grid. This point will be used to mark the position of
    a word on the cartesian plane.
    """

    def __init__(self, x, y):
        """
        Creates a new cartesian point object
        :param x: point on x-axis
        :param y: point on y-axis
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}:{})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)
