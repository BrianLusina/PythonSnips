import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.climb_stairs import (
    climb_stairs,
    climb_stairs_dp_bottom_up,
    climb_stairs_dp_top_down,
)

CLIMB_STAIRS_TEST_CASES = [
    (2, 2),
    (3, 3),
    (4, 5),
    (4, 5),
    (5, 8),
]


class ClimbStairsTestCase(unittest.TestCase):
    @parameterized.expand(CLIMB_STAIRS_TEST_CASES)
    def test_climb_stairs(self, n: int, expected: int):
        actual = climb_stairs(n)
        self.assertEqual(expected, actual)

    @parameterized.expand(CLIMB_STAIRS_TEST_CASES)
    def test_climb_stairs_dp_bottom_up(self, n: int, expected: int):
        actual = climb_stairs_dp_bottom_up(n)
        self.assertEqual(expected, actual)

    @parameterized.expand(CLIMB_STAIRS_TEST_CASES)
    def test_climb_stairs_dp_top_down(self, n: int, expected: int):
        actual = climb_stairs_dp_top_down(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
