import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.min_cost_hire_k_workers import min_cost_to_hire_workers, min_cost_to_hire_workers_2

MIN_COST_TO_HIRE_K_WORKERS_TEST_CASES = [
    ([10, 20, 5], [70, 50, 30], 2, 105.00000),
    ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.66667),
    ([10, 10, 10], [50, 60, 70], 2, 120.00000),
    ([2, 3, 1], [5, 6, 2], 2, 7.50000),
    ([5, 9, 4], [50, 45, 30], 3, 180.00000),
    ([7, 8, 6, 10], [70, 90, 80, 100], 2, 168.75000),
]


class MinCostToHireWorkersTestCase(unittest.TestCase):
    @parameterized.expand(MIN_COST_TO_HIRE_K_WORKERS_TEST_CASES)
    def test_min_cost_to_hire_k_workers(
        self, quality: List[int], wage: List[int], k: int, expected: float
    ):
        actual = min_cost_to_hire_workers(quality, wage, k)
        self.assertEqual(expected, round(actual, 5))

    @parameterized.expand(MIN_COST_TO_HIRE_K_WORKERS_TEST_CASES)
    def test_min_cost_to_hire_k_workers_2(
        self, quality: List[int], wage: List[int], k: int, expected: float
    ):
        actual = min_cost_to_hire_workers_2(quality, wage, k)
        self.assertEqual(expected, round(actual, 5))


if __name__ == "__main__":
    unittest.main()
