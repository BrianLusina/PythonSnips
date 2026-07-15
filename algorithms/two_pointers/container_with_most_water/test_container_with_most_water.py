import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.container_with_most_water import max_area, max_area_2

CONTAINER_WITH_MOST_WATER_TEST_CASES = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1, 5, 4, 3], 6),
]


class ContainerWithMostWaterTestCases(unittest.TestCase):
    @parameterized.expand(CONTAINER_WITH_MOST_WATER_TEST_CASES)
    def test_max_area(self, heights: List[int], expected: int):
        actual = max_area(heights)
        self.assertEqual(expected, actual)

    @parameterized.expand(CONTAINER_WITH_MOST_WATER_TEST_CASES)
    def test_max_area_2(self, heights: List[int], expected: int):
        actual = max_area_2(heights)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
