import unittest

from datastructures.lists.min_max import min_max


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min_max([1, 2, 3, 4, 5]), [1, 5])

    def test_2(self):
        self.assertListEqual(min_max([2334454, 5]), [5, 2334454])

    def test_3(self):
        self.assertListEqual(min_max([1]), [1, 1])


if __name__ == '__main__':
    unittest.main()
