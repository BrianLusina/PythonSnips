import unittest
from parameterized import parameterized
from pymath.rectangle_area import compute_area


class RectangleAreaTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (0, 0, 1, 1, 2, 2, 3, 3, 2),
            (0, 0, 2, 2, 1, 1, 3, 3, 7),
            (-1, -1, 2, 2, 0, 0, 1, 1, 9),
            (0, 0, 0, 0, 1, 1, 2, 2, 1),
            (-8918, -419, -7715, 577, -8918, -419, -7715, 577, 1198188),
        ]
    )
    def test_compute_area(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
        expected,
    ):
        actual = compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
