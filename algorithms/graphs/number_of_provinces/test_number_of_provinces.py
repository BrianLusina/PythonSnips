import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.graphs.number_of_provinces import (
    number_of_provinces,
    number_of_provinces_dfs,
)

NUMBER_OF_PROVINCES_TEST_CASES = [
    ([], 0),
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
]


class NumberOfProvincesTestCase(unittest.TestCase):
    @parameterized.expand(
        NUMBER_OF_PROVINCES_TEST_CASES, name_func=custom_test_name_func
    )
    def test_number_of_provinces_union_find(
        self, is_connected: List[List[int]], expected: int
    ):
        actual = number_of_provinces(is_connected)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        NUMBER_OF_PROVINCES_TEST_CASES, name_func=custom_test_name_func
    )
    def test_number_of_provinces_dfs(
        self, is_connected: List[List[int]], expected: int
    ):
        actual = number_of_provinces_dfs(is_connected)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
