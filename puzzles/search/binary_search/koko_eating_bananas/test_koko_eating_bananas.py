import unittest

from . import min_eating_speed


class MinEatingSpeedTestCase(unittest.TestCase):
    def test_1(self):
        """should return 4 for piles = [3, 6, 7, 11] h = 8"""
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        actual = min_eating_speed(piles, h)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 30 for piles = [30, 11, 23, 4, 20] h = 5"""
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        actual = min_eating_speed(piles, h)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 23 for piles = [30, 11, 23, 4, 20] h = 6"""
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        actual = min_eating_speed(piles, h)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 2 for piles = [2, 2] h = 2"""
        piles = [2,2]
        h = 2
        expected = 2
        actual = min_eating_speed(piles, h)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
