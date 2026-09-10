import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.dynamic_programming.last_stone_weight import (
    last_stone_weight_2,
    last_stone_weight_2_2,
)

LAST_STONE_WEIGHT_TEST_CASES = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([31, 26, 33, 21, 40], 5),
    ([42], 42),
    ([37, 37], 0),
    ([6, 6, 6, 6, 6], 6),
    ([3, 5, 8, 10, 4], 0),
    ([100, 10, 10, 10], 70),
]


class LastStoneWeightTestCase(unittest.TestCase):
    @parameterized.expand(LAST_STONE_WEIGHT_TEST_CASES, name_func=custom_test_name_func)
    def test_last_stone_weight_2(self, stones: List[int], expected: int):
        actual = last_stone_weight_2(stones)
        self.assertEqual(expected, actual)

    @parameterized.expand(LAST_STONE_WEIGHT_TEST_CASES, name_func=custom_test_name_func)
    def test_last_stone_weight_2_2(self, stones: List[int], expected: int):
        actual = last_stone_weight_2_2(stones)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
