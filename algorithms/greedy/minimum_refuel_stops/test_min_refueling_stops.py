import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.minimum_refuel_stops import min_refuel_stops, min_refuel_stops_2

MIN_REFUELING_STOPS_TEST_CASES = [
    (3, 3, [], 0),
    (1, 1, [], 0),
    (100, 1, [[10, 100]], -1),
    (120, 10, [[10, 60], [20, 25], [30, 30], [60, 40]], 3),
    (15, 3, [[2, 5], [3, 1], [6, 3], [12, 6]], 4),
    (570, 140, [[140, 200], [160, 130], [310, 200], [330, 250]], 2),
    (1360, 380, [[310, 160], [380, 620], [700, 89], [850, 190], [990, 360]], 2),
    (59, 14, [[9, 12], [11, 7], [13, 16], [21, 18], [47, 6]], 3),
    (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
]


class MinRefuelStopsTestCase(unittest.TestCase):
    @parameterized.expand(MIN_REFUELING_STOPS_TEST_CASES)
    def test_min_refueling_stops(
        self, target: int, start_fuel: int, stations: List[List[int]], expected: int
    ):
        actual = min_refuel_stops(target, start_fuel, stations)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_REFUELING_STOPS_TEST_CASES)
    def test_min_refueling_stops_2(
        self, target: int, start_fuel: int, stations: List[List[int]], expected: int
    ):
        actual = min_refuel_stops_2(target, start_fuel, stations)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
