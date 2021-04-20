import unittest

from pymath.evil_or_odious import evil


class EvilOrOdiousTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(evil(1), "It's Odious!")

    def test_2(self):
        self.assertEqual(evil(2), "It's Odious!")

    def test_3(self):
        self.assertEqual(evil(3), "It's Evil!")
