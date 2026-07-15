import unittest

from algorithms.backtracking.subsets.cascading_subsets import each_cons


class CascadingSubsetsTestCase(unittest.TestCase):
    def test_case1(self):
        """Should return cascading lists of 1 element"""
        lst = [3, 5, 8, 13]
        expected = [[3], [5], [8], [13]]
        actual = each_cons(lst, 1)
        self.assertEqual(expected, actual)

    def test_case2(self):
        """Should return cascading lists of 2 elements"""
        lst = [3, 5, 8, 13]
        expected = [[3, 5], [5, 8], [8, 13]]
        actual = each_cons(lst, 2)
        self.assertEqual(expected, actual)

    def test_case3(self):
        """Should return cascading lists of 3 elements"""
        lst = [3, 5, 8, 13]
        expected = [[3, 5, 8], [5, 8, 13]]
        actual = each_cons(lst, 3)
        self.assertEqual(expected, actual)

    def test_case4(self):
        """empty list should return an empty list"""
        lst = []
        expected = []
        actual = each_cons(lst, 3)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
