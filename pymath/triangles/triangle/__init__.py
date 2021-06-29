from collections import Counter
from math import sqrt, pow


class Triangle(object):
    """
    A triangle class that returns the kinds of triangles
    :cvar TYPES: The types of triangles to evaluate. it is a dictionary, therefore the key is the first letter
    of the type of triangle
        e stands for equilateral
        i stands for isosceles triangle
        s stands for scalene triangle
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

        # alternatively
        triangle=lambda a,b,c:all([a+b>c,a+c>b,b+c>a])
        triangle=lambda a,b,c:(a+b>c)&(a+c>b)&(b+c>a)
        triangle=lambda *x:sum(x)-max(x)>max(x)
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

    def area(self):
        """
        Gets the area of the triangle from the given sides
        Area of a triangle is calculated as a = 1/2 * b *h

        Equilateral triangle area is calculated as:
            1/2 * b * h, where the base, b, is any of the sides
            height, h, is the height which is calculated as h = (sqrt(3) * s) / 2
            This equates to (sqrt(3) * s^2) / 4

        Isosceles triangle area is calculated as:
        1/2 a^2 * sqrt( (b^2) / (a^2) - 1/4), where the b is a side with an equal length in another side,
        while a is the base of the triangle, or the side that does not have an equal length.

        First start by finding the 2 sides that are similar in length, will be stored as b
        The remaining side will be a(which will be used as the base), which we can then use to calculate the height
        h = sqrt(b ^ 2 - (1/4 * (a^2)))

        Scalene Triangle area is calculated as:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        Since all the sides are unequal

        :return: The area of the triangle as an integer
        :rtype: int
        """
        s1, s2, s3 = self.sides
        # if it is an equilateral triangle
        if self.kind() == self.TYPES["e"]:
            return (sqrt(3) * pow(s1, 2)) / 4

        # if the triangle is an isosceles triangle
        if self.kind() == self.TYPES["i"]:
            side_count = Counter(self.sides).most_common()
            highest_count = max(x[1] for x in side_count)
            lowest_count = min(x[1] for x in side_count)

            b, a = 0, 0

            for y in side_count:
                if y[1] == highest_count:
                    b = y[0]
                if y[1] == lowest_count:
                    a = y[0]

            return (0.5 * pow(a, 2)) * sqrt((pow(b, 2) / pow(a, 2)) - (1 / 4))

        # if the triangle is a scalene triangle
        if self.kind() == self.TYPES["s"]:
            s = sum(self.sides) / 2
            return sqrt(s * (s - s1) * (s - s2) * (s - s3))

    def perimeter(self):
        """
        Gets the perimeter of a triangle, perimeter is the sum of all 3 sides of a triangle
        :return: perimeter of a triangle as an int
        :rtype: int
        """
        return sum(self.sides)


class TriangleError(Exception):
    pass
