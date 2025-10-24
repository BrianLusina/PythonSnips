import unittest

from . import candy


class CandyTestCase(unittest.TestCase):
    def test_1(self):
        ratings = [1, 0, 2]
        expected = 5
        actual = candy(ratings)
        self.assertEqual(expected, actual)

    def test_2(self):
        ratings = [1, 2, 2]
        expected = 4
        actual = candy(ratings)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
