import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.network_delay_time import (
    network_delay_time,
    network_delay_time_2,
)


NETWORK_DELAY_TIME_TEST_CASES = [
    (
        "times=[[1,2,5],[1,3,10],[1,4,15]], n=4, k=1",
        [[1, 2, 5], [1, 3, 10], [1, 4, 15]],
        4,
        1,
        15,
    ),
    (
        "times=[[1,2,1],[2,3,1],[3,4,1]], n=4, k=1",
        [[1, 2, 1], [2, 3, 1], [3, 4, 1]],
        4,
        1,
        3,
    ),
    (
        "times=[[1,2,5],[2,3,10],[2,4,15]], n=4, k=1",
        [[1, 2, 5], [2, 3, 10], [2, 4, 15]],
        4,
        1,
        20,
    ),
    (
        "times=[[1,2,5],[1,3,5],[1,4,5],[2,4,5],[3,4,5]], n=4, k=1",
        [[1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5]],
        4,
        1,
        5,
    ),
    (
        "times=[[1,2,1],[2,3,2],[3,4,3],[4,1,4]], n=4, k=2",
        [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 1, 4]],
        4,
        2,
        9,
    ),
    (
        "times=[[2,1,1],[3,2,1],[3,4,2]], n=4, k=3",
        [[2, 1, 1], [3, 2, 1], [3, 4, 2]],
        4,
        3,
        2,
    ),
    (
        "times=[[1,2,1],[2,3,1],[3,5,2]], n=5, k=1",
        [[1, 2, 1], [2, 3, 1], [3, 5, 2]],
        5,
        1,
        -1,
    ),
    ("times=[[1,2,2]], n=2, k=2", [[1, 2, 2]], 2, 2, -1),
    (
        "times=[[1,2,3], [1,3,5], [2,3,1]], n=3, k=1",
        [[1, 2, 3], [1, 3, 5], [2, 3, 1]],
        3,
        1,
        4,
    ),
    ("times=[[1,2,2], [3,2,1]], n=3, k=1", [[1, 2, 2], [3, 2, 1]], 3, 1, -1),
]


class NetworkDelayTimeTestCase(unittest.TestCase):
    @parameterized.expand(NETWORK_DELAY_TIME_TEST_CASES)
    def test_network_delay_time(
        self, _, times: List[List[int]], n: int, k: int, expected: int
    ):
        actual = network_delay_time(times, n, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(NETWORK_DELAY_TIME_TEST_CASES)
    def test_network_delay_time_2(
        self, _, times: List[List[int]], n: int, k: int, expected: int
    ):
        actual = network_delay_time_2(times, n, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
