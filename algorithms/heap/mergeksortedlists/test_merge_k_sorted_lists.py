import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.mergeksortedlists import merge_k_lists

MERGE_K_LISTS_TEST_CASES = [
    ([[3, 4, 6], [2, 3, 5], [-1, 6]], [-1, 2, 3, 3, 4, 5, 6, 6]),
    ([[2, 4, 6], [1, 3, 5]], [1, 2, 3, 4, 5, 6]),
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
    ([[1, 2, 3]], [1, 2, 3]),
]


class MegeKListsTestCase(unittest.TestCase):
    @parameterized.expand(MERGE_K_LISTS_TEST_CASES)
    def test_merge_k_lists(self, lists: List[List[int]], expected: List[int]):
        actual = merge_k_lists(lists)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
