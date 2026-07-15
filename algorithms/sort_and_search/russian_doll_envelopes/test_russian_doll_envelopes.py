import unittest
from typing import List
from parameterized import parameterized
from algorithms.sort_and_search.russian_doll_envelopes import (
    max_envelopes,
    max_envelopes_find_position,
)
from utils.test_utils import custom_test_name_func

RUSSIAN_DOLL_ENVELOPES_TEST_CASES = [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ([[1, 1], [1, 1], [1, 1]], 1),
    ([[1, 3], [4, 9], [3, 5], [6, 10], [2, 11]], 4),
    ([[3, 2], [1, 4], [7, 7], [8, 3]], 2),
]


class RussianDollEnvelopesTestCase(unittest.TestCase):
    @parameterized.expand(
        RUSSIAN_DOLL_ENVELOPES_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_envelopes(self, envelopes: List[List[int]], expected: int):
        actual = max_envelopes(envelopes)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        RUSSIAN_DOLL_ENVELOPES_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_envelopes_find_position(
        self, envelopes: List[List[int]], expected: int
    ):
        actual = max_envelopes_find_position(envelopes)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
