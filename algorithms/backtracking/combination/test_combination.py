import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.combination import combine, combine_2

COMBINATION_TEST_CASES = [
    (1, 1, [[1]]),
    (2, 2, [[1, 2]]),
    (3, 3, [[1, 2, 3]]),
    (3, 1, [[1], [2], [3]]),
    (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    (
        5,
        3,
        [
            [1, 2, 3],
            [1, 2, 4],
            [1, 2, 5],
            [1, 3, 4],
            [1, 3, 5],
            [1, 4, 5],
            [2, 3, 4],
            [2, 3, 5],
            [2, 4, 5],
            [3, 4, 5],
        ],
    ),
]


class CombinationSumTestCase(unittest.TestCase):
    @parameterized.expand(COMBINATION_TEST_CASES)
    def test_combination(self, n: int, k: int, expected: List[List[int]]):
        actual = combine(n, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(COMBINATION_TEST_CASES)
    def test_combination_2(self, n: int, k: int, expected: List[List[int]]):
        actual = combine_2(n, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
