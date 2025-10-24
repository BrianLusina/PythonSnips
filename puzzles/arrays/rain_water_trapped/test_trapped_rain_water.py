import unittest
from . import trapped_rain_water


class TrappedRainWaterTestCase(unittest.TestCase):
    def test_1(self):
        """Should return 6 for input of [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]"""
        a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        actual = trapped_rain_water(a)
        self.assertEqual(expected, actual)

    def test_2(self):
        """Should return 0 for input of [1, 2]"""
        a = [1, 2]
        expected = 0
        actual = trapped_rain_water(a)
        self.assertEqual(expected, actual)

    def test_3(self):
        """Should return 9 for input of [4,2,0,3,2,5]"""
        a = [4, 2, 0, 3, 2, 5]
        expected = 9
        actual = trapped_rain_water(a)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
