import unittest
from . import combination_sum_2


class CombinationSumTestCase(unittest.TestCase):
    def test_1(self):
        """should return [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ] for candidates = [10,1,2,7,6,1,5], target = 8"""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        actual = combination_sum_2(candidates, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [[1,2,2],[5]] for candidates = [2,5,2,1,2], target = 5"""
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        actual = combination_sum_2(candidates, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
