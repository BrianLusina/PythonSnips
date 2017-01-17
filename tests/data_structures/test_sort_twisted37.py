import unittest
from pysnips.data_structures.lists.sort_twisted37 import sort_twisted37


class SortTwisted32Tests(unittest.TestCase):
    def shortDescription(self):
        return "Sort Twisted 37 tests"

    def test_1(self):
        self.assertEqual(sort_twisted37([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 7, 4, 5, 6, 3, 8, 9])

    def test2(self):
        self.assertEqual(sort_twisted37([12, 13, 14]), [12, 14, 13])

    def test_3(self):
        self.assertEqual(sort_twisted37([9, 2, 4, 7, 3]), [2, 7, 4, 3, 9])


if __name__ == "__main__":
    unittest.main()
