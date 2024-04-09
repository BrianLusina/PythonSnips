import unittest

from . import selection_sort


class SelectionSortTestCase(unittest.TestCase):
    def test_1(self):
        """Should sort [4,2,7,1,3] to [1,2,3,4,7]"""
        nums = [4, 2, 7, 1, 3]
        expected = [1, 2, 3, 4, 7]
        actual = selection_sort(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """Should sort [5,4,3,2,1] to [1,2,3,4,5]"""
        nums = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        actual = selection_sort(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
