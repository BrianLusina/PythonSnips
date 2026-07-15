import unittest
from . import peak_of_mountain


class PeakOfMountainTestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 from 0 1 2 3 2 1 0"""
        nums = [0, 1, 2, 3, 2, 1, 0]
        expected = 3
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 from 0 10 3 2 1 0"""
        nums = [0, 10, 3, 2, 1, 0]
        expected = 1
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 1 from 0 10 0"""
        nums = [0, 10, 0]
        expected = 1
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 16 from 0 1 2 12 22 32 42 52 62 72 82 92 102 112 122 132 133 132 111 0"""
        nums = [
            0,
            1,
            2,
            12,
            22,
            32,
            42,
            52,
            62,
            72,
            82,
            92,
            102,
            112,
            122,
            132,
            133,
            132,
            111,
            0,
        ]
        expected = 16
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 1 from 0, 10, 5, 2"""
        nums = [0, 10, 5, 2]
        expected = 1
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 1 from 0, 2, 1, 0"""
        nums = [0, 2, 1, 0]
        expected = 1
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return 1 from 0, 1, 0"""
        nums = [0, 1, 0]
        expected = 1
        actual = peak_of_mountain(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
