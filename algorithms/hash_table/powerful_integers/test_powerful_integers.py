import unittest
from typing import List
from parameterized import parameterized
from algorithms.hash_table.powerful_integers import (
    powerful_integers,
    powerful_integers_logarithmic_bounds,
)

POWERFUL_INTEGERS_TEST_CASE = [
    (2, 2, 20, [2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20]),
    (1, 1, 5, [2]),
    (5, 3, 50, [2, 4, 6, 8, 10, 14, 26, 28, 32, 34]),
    (100, 100, 1000000, [2, 101, 200, 10001, 10100, 20000]),
    (2, 5, 0, []),
    (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
    (3, 5, 15, [2, 4, 6, 8, 10, 14]),
]


class PowerfulIntegersTestCase(unittest.TestCase):
    @parameterized.expand(POWERFUL_INTEGERS_TEST_CASE)
    def test_powerful_integers(self, x: int, y: int, bound: int, expected: List[int]):
        actual = powerful_integers(x, y, bound)
        actual.sort()
        self.assertEqual(expected, actual)

    @parameterized.expand(POWERFUL_INTEGERS_TEST_CASE)
    def test_powerful_integers_logarithmic_bounds(
        self, x: int, y: int, bound: int, expected: List[int]
    ):
        actual = powerful_integers_logarithmic_bounds(x, y, bound)
        actual.sort()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
