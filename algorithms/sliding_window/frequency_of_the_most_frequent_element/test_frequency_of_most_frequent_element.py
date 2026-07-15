import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.sliding_window.frequency_of_the_most_frequent_element import (
    max_frequency,
)

MAX_FREQUENCY_TEST_CASES = [
    ([1, 2, 4], 5, 3),
    ([1, 4, 8, 13], 5, 2),
    ([3, 9, 6], 2, 1),
    ([1, 1, 2], 2, 3),
    ([4, 2, 10, 6], 2, 2),
    ([2, 3, 5], 3, 2),
    ([4, 6, 8, 10], 1, 1),
    ([1, 2, 3, 4], 5, 3),
]


class FrequencyOfMostFrequentElementTestCase(unittest.TestCase):
    @parameterized.expand(MAX_FREQUENCY_TEST_CASES, name_func=custom_test_name_func)
    def test_max_frequency(self, nums: List[int], k: int, expected: int) -> None:
        actual = max_frequency(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
