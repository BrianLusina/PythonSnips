import unittest

from . import find_missing_element


class FindMissingElementTestCases(unittest.TestCase):
    def test_1(self):
        """should return 1 in [2,3,4,5]"""
        numbers = [2, 3, 4, 5]
        expected = 1
        actual = find_missing_element(numbers)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 4 in [1,2,3,5,6,7]"""
        numbers = [1, 2, 3, 5, 6, 7]
        expected = 4
        actual = find_missing_element(numbers)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 8 in [1,2,3,4,5,6,7]"""
        numbers = [1, 2, 3, 4, 5, 6, 7]
        expected = 8
        actual = find_missing_element(numbers)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
