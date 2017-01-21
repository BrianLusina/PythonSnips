class Triangle(object):
    """
    A triangle class that returns the kinds of triangles
    """
    # the types of triangles
    TYPES = {
        "e": "equilateral",
        "s": "scalene",
        "i": "isosceles"
    }

    def __init__(self, s1, s2, s3):
        """
        initializes a Triangle object with the lengths of the triangle as parameters
        :param s1: side 1
        :param s2: side 2
        :param s3: side 3
        :raises: TriangleError
        """
        self.sides = (s1, s2, s3)

        # if the triangle sides are violated, raise an error early
        if self._invalid_lengths() or self._violates_inequality():
            raise TriangleError

    def _invalid_lengths(self):
        """
        Checks if any of the sides of the triangle have invalid lengths, an invalid length could be
        a side that is less than 0
        :return: True/False
        :rtype: bool
        """
        return any(side <= 0 for side in self.sides)

    def _violates_inequality(self):
        """
        Checks If any 2 sides sum of the triangle violate the triangle inequality.
        The inequality x + y >= z
        where x,y, and z are the lengths of the sides of a triangle. In other words, the
        sum of the lengths of any two sides of a triangle always exceeds or is equal to
        the length of the third side.
        :return: True/False in regards to any violation
        :rtype: bool
        """
        x, y, z = self.sides
        return any([
            x + y <= z,
            x + z <= y,
            y + z <= x
            ]
        )

    def kind(self):
        """
        The kind of triangle this object is
        :return: The kind of triangle this is
        :rtype: str
        """

        # get the distinct sides of the triangle
        distinct = len(set(self.sides))

        # equilateral if all three sides are equal
        if distinct == 1:
            return self.TYPES["e"]
        # if 2 sides are equal
        elif distinct == 2:
            return self.TYPES["i"]
        # no sides are equal
        else:
            return self.TYPES["s"]


class TriangleError(Exception):
    pass
