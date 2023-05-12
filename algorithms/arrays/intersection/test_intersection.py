import unittest

from . import intersection


class IntersectionTestCases(unittest.TestCase):

    def test_1(self):
        """should return [3,4] for a = [3,1,4,2], b = [4,5,3,6]"""
        a = [3, 1, 4, 2]
        b = [4, 5, 3, 6]
        expected = [3, 4]
        actual = intersection(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
