import unittest

from datastructures.lists.is_sorted_how import is_sorted_and_how


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('yes, ascending', is_sorted_and_how([1, 2]))

    def test_2(self):
        self.assertEqual('yes, descending', is_sorted_and_how([15, 7, 3, -8]))

    def test_3(self):
        self.assertEqual('no', is_sorted_and_how([4, 2, 30]))


if __name__ == '__main__':
    unittest.main()
