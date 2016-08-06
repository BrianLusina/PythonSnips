# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Solution:
import unittest


class InputOutString(object):
    @staticmethod
    def get_string():
        user = input("Input a string: ")
        return user.upper()

    @staticmethod
    def print_string():
        return InputOutString.get_string()

cl = InputOutString()
print(cl.print_string())


class Tests(unittest.TestCase):
    def test1(self):
        user = cl.print_string()
        self.assertEqual(user.upper(), user)
