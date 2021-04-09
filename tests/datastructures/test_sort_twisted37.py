import unittest

from datastructures.lists.sort_twisted37 import sort_twisted37


# todo: fix sorted twisted function
class SortTwisted32Tests(unittest.TestCase):
    def shortDescription(self):
        return "Sort Twisted 37 tests"

    @unittest.skip
    def test_1(self):
        self.assertEqual(sort_twisted37([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 7, 4, 5, 6, 3, 8, 9])

    @unittest.skip
    def test2(self):
        self.assertEqual(sort_twisted37([12, 13, 14]), [12, 14, 13])

    @unittest.skip
    def test_3(self):
        self.assertEqual(sort_twisted37([9, 2, 4, 7, 3]), [2, 7, 4, 3, 9])


if __name__ == "__main__":
    unittest.main()
