import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.two_city_scheduling import two_city_scheduling

TWO_CITY_SCHEDULING_TEST_CASES = [
    ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
    ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
    (
        [
            [515, 563],
            [451, 713],
            [537, 709],
            [343, 819],
            [855, 779],
            [457, 60],
            [650, 359],
            [631, 42],
        ],
        3086,
    ),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 18),
    ([[1, 2], [1, 2], [1, 2], [1, 2]], 6),
    ([[100, 10], [1000, 10], [500, 50], [100, 1]], 260),
    ([[100, 10], [1000, 10], [500, 50], [100, 1], [50, 1], [2000, 40]], 350),
]


class TwoCitySchedulingTestCase(unittest.TestCase):
    @parameterized.expand(TWO_CITY_SCHEDULING_TEST_CASES)
    def test_two_city_scheduling(self, costs: List[List[int]], expected: int):
        actual = two_city_scheduling(costs)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
