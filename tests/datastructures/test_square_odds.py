import unittest

from datastructures.lists.square_odds import square_odds


class SquareOddTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1,9,25,49,81", square_odds("1,2,3,4,5,6,7,8,9"))
