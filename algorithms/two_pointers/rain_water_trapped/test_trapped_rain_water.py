import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.rain_water_trapped import trapped_rain_water

TRAPPING_RAIN_WATER = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([1, 2], 0),
    ([4, 2, 0, 3, 2, 5], 9),
    ([3, 4, 1, 2, 2, 5, 1, 0, 2], 10),
]


class TrappedRainWaterTestCase(unittest.TestCase):
    @parameterized.expand(TRAPPING_RAIN_WATER)
    def test_trapping_rain_water(self, heights: List[int], expected: int):
        actual = trapped_rain_water(heights)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
