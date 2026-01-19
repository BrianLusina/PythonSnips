import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.two_sum_less_k import two_sum_less_than_k

TWO_SUM_LESS_K_TEST_CASES = [
    ([4, 2, 11, 2, 5, 3, 5, 8], 7, 6),
    ([10, 20, 30], 15, -1),
    ([34, 23, 1, 24, 75, 33, 54, 8], 60, 58),
    ([5, 5, 5, 5, 5, 5], 15, 10),
    ([1, 2, 3, 4, 5], 3, -1),
]


class TwoSumLessKTestCase(unittest.TestCase):
    @parameterized.expand(TWO_SUM_LESS_K_TEST_CASES)
    def test_two_sum_less_k(self, numbers: List[int], target: int, expected: int):
        actual = two_sum_less_than_k(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
