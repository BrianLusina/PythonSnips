import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.unique_paths import (
    unique_paths_top_down,
    unique_paths_math,
    unique_paths_bottom_up,
)

UNIQUE_PATHS_TEST_CASES = [
    (3, 7, 28),
    (3, 2, 3),
    (2, 2, 2),
    (3, 3, 6),
    (1, 1, 1),
    (10, 10, 48620),
    (20, 20, 35345263800),
]


class UniquePathsTestCase(unittest.TestCase):
    @parameterized.expand(UNIQUE_PATHS_TEST_CASES)
    def test_unique_paths_top_down(self, m: int, n: int, expected: int):
        actual = unique_paths_top_down(m, n)
        self.assertEqual(expected, actual)

    @parameterized.expand(UNIQUE_PATHS_TEST_CASES)
    def test_unique_paths_bottom_up(self, m: int, n: int, expected: int):
        actual = unique_paths_bottom_up(m, n)
        self.assertEqual(expected, actual)

    @parameterized.expand(UNIQUE_PATHS_TEST_CASES)
    def test_unique_paths_math(self, m: int, n: int, expected: int):
        actual = unique_paths_math(m, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
