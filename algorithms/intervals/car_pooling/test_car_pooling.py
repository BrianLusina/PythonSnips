import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.car_pooling import car_pooling, car_pooling_bucket

CAR_POOLING_TEST_CASES = [
    ([[3, 2, 6], [1, 4, 7], [2, 5, 8]], 5, False),
    ([[2, 0, 4], [3, 2, 6], [1, 5, 8]], 4, False),
    ([[1, 0, 3], [2, 2, 5], [3, 4, 6]], 6, True),
    ([[2, 1, 5], [3, 3, 7]], 4, False),
    ([[2, 1, 5], [3, 3, 7]], 5, True),
    ([[3, 2, 6], [1, 4, 7], [2, 5, 8]], 5, False),
    ([[1, 0, 4], [2, 2, 6], [3, 5, 8]], 6, True),
    ([[50, 0, 50], [51, 1, 51]], 100, False),
    ([[25, 0, 4], [25, 2, 6], [25, 5, 8]], 50, True),
]


class CarPoolingTestCases(unittest.TestCase):
    @parameterized.expand(CAR_POOLING_TEST_CASES)
    def test_car_pooling(self, trips: List[List[int]], capacity: int, expected: bool):
        actual = car_pooling(trips, capacity)
        self.assertEqual(expected, actual)

    @parameterized.expand(CAR_POOLING_TEST_CASES)
    def test_car_pooling_bucket_sort(
        self, trips: List[List[int]], capacity: int, expected: bool
    ):
        actual = car_pooling_bucket(trips, capacity)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
