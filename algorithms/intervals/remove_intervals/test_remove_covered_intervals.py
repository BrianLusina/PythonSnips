import unittest
from typing import List
from copy import deepcopy
from parameterized import parameterized
from algorithms.intervals.remove_intervals import remove_covered_intervals

TEST_CASES = [
    ([[1, 5], [2, 5], [3, 5], [4, 5]], 1),
    ([[1, 3], [3, 6], [6, 9]], 3),
    ([[1, 3], [4, 6], [7, 9]], 3),
    ([[1, 10], [2, 9], [3, 8], [4, 7]], 1),
    ([[1, 4], [3, 6], [2, 8]], 2),
    ([[1, 2], [1, 4], [3, 4]], 1),
    ([[1, 5], [2, 3], [4, 6]], 2),
    (
        [
            [33, 40],
            [39, 48],
            [39, 53],
            [63, 68],
            [46, 53],
            [56, 62],
            [71, 79],
            [67, 73],
            [103, 114],
            [51, 58],
            [47, 54],
            [123, 130],
            [142, 157],
            [66, 71],
            [151, 164],
            [80, 85],
            [94, 105],
            [100, 107],
            [164, 172],
            [105, 119],
            [221, 226],
            [171, 176],
            [98, 105],
            [129, 137],
            [272, 281],
            [66, 76],
            [38, 53],
            [176, 185],
            [264, 269],
            [243, 255],
            [100, 105],
            [343, 357],
            [192, 207],
            [314, 325],
            [77, 84],
            [208, 222],
            [54, 59],
            [48, 59],
            [138, 150],
            [78, 88],
            [33, 46],
            [70, 84],
            [35, 44],
            [282, 295],
            [128, 136],
            [472, 485],
            [177, 189],
            [190, 196],
            [398, 413],
            [108, 121],
            [375, 385],
            [376, 388],
            [422, 429],
            [519, 527],
            [46, 51],
            [530, 543],
            [345, 360],
            [570, 575],
            [374, 388],
            [527, 534],
            [271, 282],
            [430, 436],
            [81, 91],
            [136, 149],
            [494, 500],
            [52, 60],
        ],
        48,
    ),
]


class RemoveCoveredIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_remove_closed_intervals(self, intervals: List[List[int]], expected: int):
        input_intervals = deepcopy(intervals)
        actual = remove_covered_intervals(input_intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
