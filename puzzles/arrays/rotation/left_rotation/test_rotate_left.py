import unittest
from . import rotate_left


class LeftRotationTestCase(unittest.TestCase):
    def test_rotate_by_2(self):
        """should rotate array [1,2,3,4,5] by 2 steps to the left to [3,4,5,1,2]"""
        d = 2
        arr = [1, 2, 3, 4, 5]
        expected = [3, 4, 5, 1, 2]
        actual = rotate_left(d, arr)

        self.assertEqual(expected, actual, msg=f"Rotate {arr} by {d}")

    def test_rotate_by_4(self):
        """should rotate array [1,2,3,4,5] by 4 steps to the left to [5,1,2,3,4]"""
        d = 4
        arr = [1, 2, 3, 4, 5]
        expected = [5, 1, 2, 3, 4]
        actual = rotate_left(d, arr)

        self.assertEqual(expected, actual, msg=f"Rotate {arr} by {d}")


if __name__ == '__main__':
    unittest.main()
