import unittest
from typing import List

from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.hash_table.number_of_black_blocks import (
    count_black_blocks,
    count_black_blocks_2,
)

NUMBER_OF_BLACK_BLOCKS_TEST_CASES = [
    (3, 3, [[0, 0]], [3, 1, 0, 0, 0]),
    (3, 3, [[0, 0], [1, 1], [0, 2]], [0, 2, 2, 0, 0]),
    (8, 9, [], [56, 0, 0, 0, 0]),
    (2, 2, [[0, 0], [0, 1], [1, 0]], [0, 0, 0, 1, 0]),
    (5, 6, [[2, 3]], [16, 4, 0, 0, 0]),
    (4, 4, [[0, 0]], [8, 1, 0, 0, 0]),
    (3, 5, [[1, 2], [1, 3]], [2, 4, 2, 0, 0]),
]


class NumberOfBlackBlocksTestCase(unittest.TestCase):
    @parameterized.expand(
        NUMBER_OF_BLACK_BLOCKS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_count_black_blocks(
        self, m: int, n: int, black_positions: List[List[int]], expected: List[int]
    ):
        actual = count_black_blocks(m, n, black_positions)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        NUMBER_OF_BLACK_BLOCKS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_count_black_blocks_2(
        self, m: int, n: int, black_positions: List[List[int]], expected: List[int]
    ):
        actual = count_black_blocks_2(m, n, black_positions)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
