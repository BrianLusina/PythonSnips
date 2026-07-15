import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.combination import combination_sum_3

COMBINATION_SUM_3_TEST_CASES = [
    (3, 7, [[1, 2, 4]]),
    (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    (4, 1, []),
    (1, 1, [[1]]),
]


class CombinationSumTestCase(unittest.TestCase):
    @parameterized.expand(COMBINATION_SUM_3_TEST_CASES)
    def test_combination_sum_3(self, k: int, n: int, expected: List[List[int]]):
        actual = combination_sum_3(k, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
