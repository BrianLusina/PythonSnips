import unittest
from . import pascals_triangle, pascal_nth_row


class PascalsTriangleTestCase(unittest.TestCase):
    def test_1(self):
        """k=3 should return [1, 3, 3, 1]"""
        k = 3
        expected = [1, 3, 3, 1]
        actual = pascal_nth_row(k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
