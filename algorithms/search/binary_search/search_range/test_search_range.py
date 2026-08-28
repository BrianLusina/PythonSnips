import unittest
from typing import List, Callable
import pytest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.search.binary_search.search_range import (
    search_range,
    search_range_v3,
    search_range_v2,
    search_range_v4,
)

# Test implementations under benchmark
IMPLEMENTATIONS: List[Callable] = [
    search_range,
    search_range_v2,
    search_range_v3,
    search_range_v4,
]

SEARCH_RANGE_TEST_CASES = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([1, 3], 1, [0, 0]),
    ([1, 4], 4, [1, 1]),
    ([1, 2, 3], 2, [1, 1]),
    ([3, 3, 3], 3, [0, 2]),
]

# Generate datasets for benchmarking
SMALL_DATASET = ([5, 7, 7, 8, 8, 10], 8)
LARGE_DATASET = (sorted([i // 2 for i in range(100_000)]), 25_000)
NOT_FOUND_DATASET = (list(range(0, 100_000, 2)), 50_001)


class SearchRangeTestCases(unittest.TestCase):
    @parameterized.expand(SEARCH_RANGE_TEST_CASES, name_func=custom_test_name_func)
    def test_search_range(self, nums: List[int], target: int, expected: List[int]):
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    @parameterized.expand(SEARCH_RANGE_TEST_CASES, name_func=custom_test_name_func)
    def test_search_range_v2(self, nums: List[int], target: int, expected: List[int]):
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    @parameterized.expand(SEARCH_RANGE_TEST_CASES, name_func=custom_test_name_func)
    def test_search_range_v3(self, nums: List[int], target: int, expected: List[int]):
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    @parameterized.expand(SEARCH_RANGE_TEST_CASES, name_func=custom_test_name_func)
    def test_search_range_v4(self, nums: List[int], target: int, expected: List[int]):
        actual = search_range_v4(nums=nums, target=target)
        self.assertEqual(expected, actual)


@pytest.mark.benchmark(group="search-range-small")
@pytest.mark.parametrize("func", IMPLEMENTATIONS, ids=lambda f: f.__name__)
def test_benchmark_search_range_small(benchmark, func):
    nums, target = SMALL_DATASET
    result = benchmark(func, nums=nums, target=target)
    assert result == [3, 4]


@pytest.mark.benchmark(group="search-range-large")
@pytest.mark.parametrize("func", IMPLEMENTATIONS, ids=lambda f: f.__name__)
def test_benchmark_search_range_large(benchmark, func):
    nums, target = LARGE_DATASET
    result = benchmark(func, nums=nums, target=target)
    assert result == [50_000, 50_001]


@pytest.mark.benchmark(group="search-range-not-found")
@pytest.mark.parametrize("func", IMPLEMENTATIONS, ids=lambda f: f.__name__)
def test_benchmark_search_range_not_found(benchmark, func):
    nums, target = NOT_FOUND_DATASET
    result = benchmark(func, nums=nums, target=target)
    assert result == [-1, -1]


if __name__ == "__main__":
    unittest.main()
