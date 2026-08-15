import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.heap.trapping_rain_water_ii import trap_rain_water, trap_rain_water_2

TRAPPING_RAIN_WATER_II_TEST_CASES = [
    ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
    (
        [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ],
        10,
    ),
]


class TrappingRainWaterIITestCase(unittest.TestCase):
    @parameterized.expand(
        TRAPPING_RAIN_WATER_II_TEST_CASES, name_func=custom_test_name_func
    )
    def test_trapping_rain_water_ii(self, height_map: List[List[int]], expected: int):
        actual = trap_rain_water(height_map)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        TRAPPING_RAIN_WATER_II_TEST_CASES, name_func=custom_test_name_func
    )
    def test_trapping_rain_water_ii_2(self, height_map: List[List[int]], expected: int):
        actual = trap_rain_water_2(height_map)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
