import unittest
from . import find_index_of_smallest_number


class FindIndexOfSmallestNumberTestCase(unittest.TestCase):
    def test_1(self):
        """should return 4 in input of [4, 5, 6, 7, 1, 2, 3]"""
        numbers = [4, 5, 6, 7, 1, 2, 3]
        expected = 4
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 in input of [6, 7, 1, 2, 3, 4, 5]"""
        numbers = [6, 7, 1, 2, 3, 4, 5]
        expected = 2
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 1 in input of [7, 1, 2, 3, 4, 5, 6]"""
        numbers = [7, 1, 2, 3, 4, 5, 6]
        expected = 1
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 0 in input of [1, 2, 3, 4, 5, 6, 7]"""
        numbers = [1, 2, 3, 4, 5, 6, 7]
        expected = 0
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 5 in input of [3, 4, 5, 6, 7, 1, 2]"""
        numbers = [3, 4, 5, 6, 7, 1, 2]
        expected = 5
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 6 in input of [2, 3, 4, 5, 6, 7, 1]"""
        numbers = [2, 3, 4, 5, 6, 7, 1]
        expected = 6
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return 3 in input of [5, 6, 7, 1, 2, 3, 5]"""
        numbers = [5, 6, 7, 1, 2, 3, 5]
        expected = 3
        actual = find_index_of_smallest_number(numbers)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
