import unittest
from . import find_first_in_duplicates_linear, find_first_in_duplicates


class FindFirstEntryInDuplicateListLinearTestCases(unittest.TestCase):
    def test_1(self):
        """should return 3 for numbers=[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401] and target=108"""
        numbers = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        target = 108
        expected = 3
        actual = find_first_in_duplicates_linear(numbers, target)
        self.assertEqual(expected, actual)


class FindFirstEntryInDuplicateListTestCases(unittest.TestCase):
    def test_1(self):
        """should return 3 for numbers=[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401] and target=108"""
        numbers = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        target = 108
        expected = 3
        actual = find_first_in_duplicates(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
