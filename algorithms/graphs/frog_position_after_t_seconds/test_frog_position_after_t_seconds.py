import unittest
from parameterized import parameterized
from . import frog_position, frog_position_2


class FrogPositionAfterTSecondsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (1, [], 5, 1, 1.00000),
            (4, [[1, 2], [2, 3], [3, 4]], 4, 4, 1.00000),
            (4, [[1, 2], [1, 3], [2, 4]], 2, 2, 0.00000),
            (5, [[1, 2], [1, 3], [3, 4], [4, 5]], 2, 5, 0.00000),
            (6, [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]], 2, 6, 0.16667),
            (1, [], 1, 1, 1.00000),
            (3, [[1, 2], [2, 3]], 2, 3, 1.00000),
            (3, [[1, 2], [1, 3]], 1, 2, 0.50000),
            (6, [[1, 2], [1, 3], [3, 4], [4, 5], [5, 6]], 2, 6, 0.00000),
            (6, [[2, 1], [3, 1], [4, 3], [5, 1], [6, 2]], 2, 6, 0.33333),
        ]
    )
    def test_frog_position(self, n, edges, t, target, expected):
        actual = frog_position(n, edges, t, target)
        actual_rounded = round(actual, 5)
        self.assertEqual(expected, actual_rounded)

    @parameterized.expand(
        [
            (1, [], 5, 1, 1.00000),
            (4, [[1, 2], [2, 3], [3, 4]], 4, 4, 1.00000),
            (4, [[1, 2], [1, 3], [2, 4]], 2, 2, 0.00000),
            (5, [[1, 2], [1, 3], [3, 4], [4, 5]], 2, 5, 0.00000),
            (6, [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]], 2, 6, 0.16667),
            (1, [], 1, 1, 1.00000),
            (3, [[1, 2], [2, 3]], 2, 3, 1.00000),
            (3, [[1, 2], [1, 3]], 1, 2, 0.50000),
            (6, [[1, 2], [1, 3], [3, 4], [4, 5], [5, 6]], 2, 6, 0.00000),
            (6, [[2, 1], [3, 1], [4, 3], [5, 1], [6, 2]], 2, 6, 0.33333),
        ]
    )
    def test_frog_position(self, n, edges, t, target, expected):
        actual = frog_position_2(n, edges, t, target)
        actual_rounded = round(actual, 5)
        self.assertEqual(expected, actual_rounded)


if __name__ == "__main__":
    unittest.main()
