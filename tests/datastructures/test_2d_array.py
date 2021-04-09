import unittest

from datastructures.lists.twod_array import TwoDimensions


class Test(unittest.TestCase):
    def test_4_5(self):
        d_Arr = TwoDimensions(4, 5)
        self.assertEqual([[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]], d_Arr.dimensions())

    def test_3_5(self):
        d_Arr = TwoDimensions(3, 5)
        self.assertEqual([[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]], d_Arr.dimensions())
