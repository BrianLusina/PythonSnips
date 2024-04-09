import unittest

from . import unique_occurrences


class UniqueOccurrencesTestCase(unittest.TestCase):
    def test_one(self):
        """should return true for arr = [1,2,2,1,1,3]"""
        arr = [1, 2, 2, 1, 1, 3]
        actual = unique_occurrences(arr)
        self.assertTrue(actual)

    def test_two(self):
        """should return false for arr = [1,2]"""
        arr = [1, 2]
        actual = unique_occurrences(arr)
        self.assertFalse(actual)

    def test_three(self):
        """should return true for arr = [-3,0,1,-3,1,1,1,-3,10,0]"""
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        actual = unique_occurrences(arr)
        self.assertTrue(actual)

    def test_four(self):
        """should return false for arr = [1,2,4,3,1,3,3,4]"""
        arr = [1, 2, 4, 3, 1, 3, 3, 4]
        actual = unique_occurrences(arr)
        self.assertFalse(actual)

    def test_five(self):
        """should return true for arr = [1,2,4,3,1,3,3,4,4,4]"""
        arr = [1, 2, 4, 3, 1, 3, 3, 4, 4, 4]
        actual = unique_occurrences(arr)
        self.assertTrue(actual)

    def test_six(self):
        """should return true for arr = [-1,-1,-1,-3,-1,-1]"""
        arr = [-1, -1, -1, -3, -1, -1]
        actual = unique_occurrences(arr)
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
