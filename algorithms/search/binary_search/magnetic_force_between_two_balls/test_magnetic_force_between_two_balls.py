import unittest
from typing import List
from parameterized import parameterized
from algorithms.search.binary_search.magnetic_force_between_two_balls import (
    max_distance,
)

MAGNETIC_FORCE_BETWEEN_TWO_BALLS_TEST_CASES = [
    ([1, 2, 3, 4, 7], 3, 3),
    ([5, 4, 3, 2, 1, 1000000000], 2, 999999999),
    ([1, 2, 3, 7, 11], 2, 10),
    ([9, 8, 7, 3], 3, 2),
    ([1, 3, 7, 9, 14], 5, 2),
    ([1000, 1], 2, 999),
    ([5, 10, 15, 20, 25, 30], 4, 5),
]


class MagneticForceBetweenTwoBallsTestCase(unittest.TestCase):
    @parameterized.expand(MAGNETIC_FORCE_BETWEEN_TWO_BALLS_TEST_CASES)
    def test_max_distance(self, position: List[int], m: int, expected: int):
        actual = max_distance(position, m)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
