import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.max_profit_in_job_scheduling import job_scheduling

JOB_SCHEDULING_TEST_CASES = [
    (
        "startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]",
        [1, 2, 3, 3],
        [3, 4, 5, 6],
        [50, 10, 40, 70],
        120,
    ),
    (
        "startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]",
        [1, 2, 3, 4, 6],
        [3, 5, 10, 6, 9],
        [20, 20, 100, 70, 60],
        150,
    ),
    (
        "startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]",
        [1, 1, 1],
        [2, 3, 4],
        [5, 6, 4],
        6,
    ),
]


class MaxProfitInJobSchedulingTestCase(unittest.TestCase):
    @parameterized.expand(JOB_SCHEDULING_TEST_CASES)
    def test_job_scheduling(
        self,
        _,
        start_time: List[int],
        end_time: List[int],
        profit: List[int],
        expected: int,
    ):
        actual = job_scheduling(start_time, end_time, profit)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
