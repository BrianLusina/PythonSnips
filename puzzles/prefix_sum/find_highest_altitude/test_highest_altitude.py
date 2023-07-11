import unittest

from . import largest_altitude


class LargestAltitudeTestCase(unittest.TestCase):
    def test_one(self):
        """should return 1 from gain=[-5,1,5,0,-7]"""
        gain = [-5, 1, 5, 0, -7]
        expected = 1
        actual = largest_altitude(gain)

        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 0 from gain=[-4,-3,-2,-1,4,3,2]"""
        gain = [-4, -3, -2, -1, 4, 3, 2]
        expected = 0
        actual = largest_altitude(gain)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
