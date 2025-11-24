import unittest
from parameterized import parameterized
from . import max_runtime, max_run_time_2


class MaxRunTimeTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([2, 3, 3, 4], 3, 4),
            ([1, 1, 4, 5], 2, 5),
            ([2, 2, 2, 2], 1, 8),
            ([7, 2, 5, 10, 8], 2, 16),
            ([1, 2, 3, 4, 5], 2, 7),
            ([3, 4, 3, 4, 5, 5, 8, 2], 4, 8),
            ([5, 2, 4], 2, 5),
            ([1, 6, 2, 6, 8], 5, 1),
        ]
    )
    def test_max_runtime_1(self, batteries, n, expected):
        actual = max_runtime(batteries, n)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([2, 3, 3, 4], 3, 4),
            ([1, 1, 4, 5], 2, 5),
            ([2, 2, 2, 2], 1, 8),
            ([7, 2, 5, 10, 8], 2, 16),
            ([1, 2, 3, 4, 5], 2, 7),
            ([3, 4, 3, 4, 5, 5, 8, 2], 4, 8),
            ([5, 2, 4], 2, 5),
            ([1, 6, 2, 6, 8], 5, 1),
        ]
    )
    def test_max_runtime_2(self, batteries, n, expected):
        actual = max_run_time_2(batteries, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
