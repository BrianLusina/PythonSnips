import unittest
from . import can_place_flowers


class CanPlaceFlowersTestCase(unittest.TestCase):
    def test_1(self):
        """should return true for flowerbed=[1,0,0,0,1] and n = 1"""
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        actual = can_place_flowers(flowerbed, n)
        self.assertTrue(actual)

    def test_2(self):
        """should return true for flowerbed=[1,0,0,0,1] and n = 2"""
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        actual = can_place_flowers(flowerbed, n)
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
