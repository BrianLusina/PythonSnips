import unittest
from typing import List
from parameterized import parameterized
from algorithms.search.binary_search.divide_chocolate import maximize_sweetness, maximize_sweetness_2

TEST_CASES = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6),
    ([5], 0, 5),
    ([1, 2, 2, 1, 2, 2, 1], 3, 2),
    ([1, 1, 1, 1, 1, 1, 1], 6, 1),
    ([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 20, 7),
]


class MaximizeSweetnessTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_maximize_sweetness(self, sweetness: List[int], k: int, expected: int):
        actual = maximize_sweetness(sweetness, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(TEST_CASES)
    def test_maximize_sweetness_2(self, sweetness: List[int], k: int, expected: int):
        actual = maximize_sweetness_2(sweetness, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
