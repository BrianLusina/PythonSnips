"""
Used to demonstrate decorators in classes
"""
from math import pi


class Circle(object):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """
        This sets the radius as a mutable property
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Allows us to set the radius of an instance of a Circle.
        is useful for performing sanity checks, ensuring that reasonable values are set
        """
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError(f"Radius can not be negative")

    @property
    def area(self):
        """
        immutable property: properties without .setter() methods can’t be changed. 
        Even though it is defined as a method, it can be retrieved as an attribute without parentheses.
        """
        return self.pi() * self.radius ** 2

    def cylinder_volume(self, height):
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """
        Factory method creating a unit circle of 1
        A class method not bound to one particular instance of Circle. 
        Class methods are often used as factory methods that can create specific instances of the class
        """
        return cls(1)

    @staticmethod
    def pi():
        """
        Represents a static method that belongs to the namespace of a class.
        Can be called on the class or on the instance of the class
        """
        return pi
