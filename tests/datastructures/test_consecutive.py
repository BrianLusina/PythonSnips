import unittest

from datastructures.lists.consecutive import consecutive


class ConsecutiveTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(consecutive([4, 8, 6]), 2)

    def test_2(self):
        self.assertEqual(consecutive([1, 2, 3, 4]), 0)

    def test_3(self):
        self.assertEqual(consecutive([]), 0)

    def test_4(self):
        self.assertEqual(consecutive([1]), 0)

    def test_5(self):
        self.assertEqual(consecutive([-10]), 0)


if __name__ == '__main__':
    unittest.main()
