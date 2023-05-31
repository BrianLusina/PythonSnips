import unittest

from . import quicksort


class QuicksortTestCases(unittest.TestCase):

    def test_one(self):
        """should sort numbers=[0,8,1,2,7,9,3,4]"""
        numbers = [0, 8, 1, 2, 7, 9, 3, 4]
        expected = [0, 1, 2, 3, 4, 7, 8, 9]
        actual = quicksort(numbers)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should sort numbers=[0,5,2,1,6,3]"""
        numbers = [0, 5, 2, 1, 6, 3]
        expected = [0, 1, 2, 3, 5, 6]
        actual = quicksort(numbers)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should sort numbers=[7,6,5,3,2,1]"""
        numbers = [7, 6, 5, 3, 2, 1]
        expected = [1, 2, 3, 5, 6, 7]
        actual = quicksort(numbers)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
