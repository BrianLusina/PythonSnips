import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.insert_interval import insert_interval


class InsertIntervalTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([[1, 2], [3, 4], [5, 8], [9, 15]], [2, 5], [[1, 8], [9, 15]]),
            (
                [[1, 6], [8, 9], [10, 15], [16, 18]],
                [9, 10],
                [[1, 6], [8, 15], [16, 18]],
            ),
            (
                [[1, 2], [3, 4], [5, 8], [9, 15]],
                [16, 17],
                [[1, 2], [3, 4], [5, 8], [9, 15], [16, 17]],
            ),
            ([[1, 4], [5, 6], [7, 8], [9, 10]], [1, 5], [[1, 6], [7, 8], [9, 10]]),
            ([[1, 3], [4, 6], [7, 8], [9, 10]], [1, 10], [[1, 10]]),
            ([[1, 3], [5, 7], [8, 9], [10, 13]], [2, 6], [[1, 7], [8, 9], [10, 13]]),
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ]
    )
    def test_insert_interval(
        self,
        existing_intervals: List[List[int]],
        new_interval: List[int],
        expected: List[List[int]],
    ):
        actual = insert_interval(existing_intervals, new_interval)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
