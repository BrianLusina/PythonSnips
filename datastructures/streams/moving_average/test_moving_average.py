import unittest
from typing import List, Tuple
from parameterized import parameterized
from datastructures.streams.moving_average import MovingAverage
from datastructures.streams.moving_average.moving_average_with_buffer import (
    MovingAverageWithBuffer,
)


TEST_CASES = [
    (3, [(1, 1.00000), (10, 5.50000), (3, 4.66667), (5, 6.00000)]),
    (2, [(7, 7.00000), (14, 10.50000), (21, 17.50000), (28, 24.50000), (35, 31.50000)]),
    (3, [(5, 5.00000), (10, 7.50000), (15, 10.00000), (20, 15.00000)]),
    (10, [(1, 1.00000), (2, 1.50000)]),
    (100, [(-100, -100.00000)]),
]


class MyTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_moving_average(self, size: int, data_to_expected: List[Tuple[int, float]]):
        moving_average = MovingAverage(size)
        for data, expected in data_to_expected:
            actual = moving_average.next(data)
            round(actual, 5)
            self.assertEqual(expected, round(actual, 5))

    @parameterized.expand(TEST_CASES)
    def test_moving_average_with_buffer(
        self, size: int, data_to_expected: List[Tuple[int, float]]
    ):
        moving_average = MovingAverageWithBuffer(size)
        for data, expected in data_to_expected:
            actual = moving_average.next(data)
            round(actual, 5)
            self.assertEqual(expected, round(actual, 5))


if __name__ == "__main__":
    unittest.main()
