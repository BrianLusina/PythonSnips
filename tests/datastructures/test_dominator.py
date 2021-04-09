import unittest

from datastructures.lists.dominator import dominator


class DominatorTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)

    def test2(self):
        self.assertEqual(dominator([1, 2, 3, 4, 5]), -1)

    def test3(self):
        self.assertEqual(dominator([1, 1, 1, 2, 2, 2]), -1)

    def test4(self):
        self.assertEqual(dominator([1, 1, 1, 2, 2, 2, 2]), 2)

    def test5(self):
        self.assertEqual(dominator([]), -1)

    def test6(self):
        self.assertEqual(dominator([7, 6, 9, 7, 7, 7, 7, 7, 3, 7, 2, 7, 10, 7, 7, 7, 2]), 7)
