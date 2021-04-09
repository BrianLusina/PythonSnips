import unittest

from datastructures.lists.repeat_sum import repeat_sum


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]), 10)

    def test2(self):
        self.assertEqual(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]), 0)

    def test3(self):
        self.assertEqual(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]), 9)

    def test4(self):
        self.assertEqual(repeat_sum([[1]]), 0)
