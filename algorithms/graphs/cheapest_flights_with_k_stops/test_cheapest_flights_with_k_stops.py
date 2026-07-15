import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.cheapest_flights_with_k_stops import find_cheapest_price

CHEAPEST_FLIGHTS_WITH_K_STOPS_TEST_CASES = [
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    (3, [[0, 1, 100], [1, 2, 400], [0, 2, 350]], 0, 2, 0, 350),
    (4, [[0, 1, 100], [1, 2, 100], [2, 3, 100]], 0, 3, 1, -1),
    (
        4,
        [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0,
        3,
        1,
        700,
    ),
    (
        5,
        [
            [0, 1, 100],
            [1, 2, 100],
            [2, 3, 100],
            [3, 4, 100],
            [0, 4, 1000],
            [0, 2, 500],
            [1, 3, 250],
            [2, 4, 200],
        ],
        0,
        4,
        2,
        400,
    ),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
]


class CheapestFlightsWithKStopsTestCase(unittest.TestCase):
    @parameterized.expand(CHEAPEST_FLIGHTS_WITH_K_STOPS_TEST_CASES)
    def test_cheapest_flights_with_k_stops(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
        expected: int,
    ):
        actual = find_cheapest_price(n, flights, src, dst, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
