import unittest
from . import combination_sum_3


class CombinationSumTestCase(unittest.TestCase):
    def test_1(self):
        """should return [[1,2,4]] for k=3 & n=7"""
        k = 3
        n = 7
        expected = [[1, 2, 4]]
        actual = combination_sum_3(k, n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [[1,2,4]] for k=3 & n=9"""
        k = 3
        n = 9
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        actual = combination_sum_3(k, n)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [] for k=4 & n=1"""
        k = 4
        n = 1
        expected = []
        actual = combination_sum_3(k, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
