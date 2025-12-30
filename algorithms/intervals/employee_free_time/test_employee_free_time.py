import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.employee_free_time.interval import Interval
from algorithms.intervals.employee_free_time import (
    employee_free_time,
    employee_free_time_heap,
)

EMPLOYEE_FREE_TIME_TEST_CASES = [
    (
        [
            [Interval(start=1, end=2), Interval(start=5, end=6)],
            [Interval(start=1, end=3)],
            [Interval(start=4, end=10)],
        ],
        [Interval(start=3, end=4)],
    ),
    (
        [
            [Interval(start=1, end=3), Interval(start=6, end=7)],
            [Interval(start=2, end=4)],
            [Interval(start=2, end=5), Interval(start=9, end=12)],
        ],
        [Interval(start=5, end=6), Interval(start=7, end=9)],
    ),
    (
        [
            [Interval(start=2, end=3), Interval(start=7, end=9)],
            [Interval(start=1, end=4), Interval(start=6, end=7)],
        ],
        [Interval(start=4, end=6)],
    ),
    (
        [
            [Interval(start=3, end=5), Interval(start=8, end=10)],
            [Interval(start=4, end=6), Interval(start=9, end=12)],
            [Interval(start=5, end=6), Interval(start=8, end=10)],
        ],
        [Interval(start=6, end=8)],
    ),
    (
        [
            [
                Interval(start=1, end=2),
                Interval(start=3, end=4),
                Interval(start=5, end=6),
                Interval(start=7, end=8),
                Interval(start=9, end=10),
                Interval(start=11, end=12),
            ],
            [
                Interval(start=1, end=2),
                Interval(start=3, end=4),
                Interval(start=5, end=6),
                Interval(start=7, end=8),
                Interval(start=9, end=10),
                Interval(start=11, end=12),
            ],
            [
                Interval(start=1, end=2),
                Interval(start=3, end=4),
                Interval(start=5, end=6),
                Interval(start=7, end=8),
                Interval(start=9, end=10),
                Interval(start=11, end=12),
            ],
            [
                Interval(start=1, end=2),
                Interval(start=3, end=4),
                Interval(start=5, end=6),
                Interval(start=7, end=8),
                Interval(start=9, end=10),
                Interval(start=11, end=12),
            ],
        ],
        [
            Interval(start=2, end=3),
            Interval(start=4, end=5),
            Interval(start=6, end=7),
            Interval(start=8, end=9),
            Interval(start=10, end=11),
        ],
    ),
]


class EmployeeFreeTimeTestCase(unittest.TestCase):
    @parameterized.expand(EMPLOYEE_FREE_TIME_TEST_CASES)
    def test_employee_free_time(
        self, schedule: List[List[Interval]], expected: List[Interval]
    ):
        actual = employee_free_time(schedule)
        self.assertListEqual(expected, actual)

    @parameterized.expand(EMPLOYEE_FREE_TIME_TEST_CASES)
    def test_employee_free_time_heap(
        self, schedule: List[List[Interval]], expected: List[Interval]
    ):
        actual = employee_free_time_heap(schedule)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
