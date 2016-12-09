import unittest
from pprint import pprint


class TwoDimensions(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dimensions(self):
        row, col = self.x, self.y
        mult = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                mult[r][c] = r * c
        return mult


class Test(unittest.TestCase):
    def test_4_5(self):
        d_Arr = TwoDimensions(4, 5)
        self.assertEqual([[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]], d_Arr.dimensions())

    def test_3_5(self):
        d_Arr = TwoDimensions(3, 5)
        self.assertEqual([[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]], d_Arr.dimensions())
