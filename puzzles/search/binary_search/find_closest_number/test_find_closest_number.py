import unittest
from . import find_closest_number


class FindClosestNumberTestCase(unittest.TestCase):
    def test_1(self):
        items = [1, 2, 4, 5, 6, 6, 8, 9]
        target = 11
        expected = 9
        actual = find_closest_number(items, target)

        self.assertEqual(expected, actual)

    def test_2(self):
        items = [2, 5, 6, 7, 8, 8, 9]
        target = 4
        expected = 5
        actual = find_closest_number(items, target)

        self.assertEqual(expected, actual)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
