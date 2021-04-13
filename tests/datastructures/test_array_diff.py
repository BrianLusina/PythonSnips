import unittest

from datastructures.arrays.array_diff import array_diff


class ArrayDiffTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")

    def test_2(self):
        self.assertEqual(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")

    def test_3(self):
        self.assertEqual(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")

    def test_4(self):
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")

    def test_5(self):
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
