import unittest

from pystrings.name_that_number import name_that_number


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(name_that_number(0), 'zero')

    def test2(self):
        self.assertEqual(name_that_number(4), 'four')

    def test3(self):
        self.assertEqual(name_that_number(9), 'nine')

    def test4(self):
        self.assertEqual(name_that_number(23), 'twenty three')

    def test5(self):
        self.assertEqual(name_that_number(20), "twenty")
