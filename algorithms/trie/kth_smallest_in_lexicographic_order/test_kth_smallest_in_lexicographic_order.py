import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.trie.kth_smallest_in_lexicographic_order import (
    find_kth_number,
    find_kth_number_2,
    find_kth_number_3,
)

KTH_SMALLEST_IN_LEXICOGRAPHIC_ORDER_TEST_CASES = [
    (13, 2, 10),
    (1, 1, 1),
]


class KthSmallestInLexicographicOrderTestCase(unittest.TestCase):
    @parameterized.expand(
        KTH_SMALLEST_IN_LEXICOGRAPHIC_ORDER_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_kth_number(self, n: int, k: int, expected: int):
        actual = find_kth_number(n, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        KTH_SMALLEST_IN_LEXICOGRAPHIC_ORDER_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_kth_number_2(self, n: int, k: int, expected: int):
        actual = find_kth_number_2(n, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        KTH_SMALLEST_IN_LEXICOGRAPHIC_ORDER_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_kth_number_3(self, n: int, k: int, expected: int):
        actual = find_kth_number_3(n, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
