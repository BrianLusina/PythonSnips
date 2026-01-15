import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.topklargest import k_largest, kth_largest, kth_largest_sorting

K_LARGEST_ELEMENTS_TEST_CASES = [
    ([9, 3, 7, 1, -2, 6, 8], 3, [8, 7, 9]),
    ([5, 3, 2, 1, 4], 2, [5, 4]),
]


class TopKLargestElementsTestCase(unittest.TestCase):
    @parameterized.expand(K_LARGEST_ELEMENTS_TEST_CASES)
    def test_top_k_largest_elements(self, nums: List[int], k: int, expected: List[int]):
        actual = k_largest(nums, k)
        self.assertListEqual(sorted(expected), sorted(actual))


KTH_LARGEST_ELEMENTS_TEST_CASES = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1], 1, 1),
    ([7, 10, 4, 3, 20, 15], 3, 10),
    ([7, 10, 4, 3, 20, 15], 4, 7),
    ([7, 10, 4, 3, 20, 15], 5, 4),
    ([5, 3, 2, 1, 4], 2, 4),
]


class TopKthLargestElementsTestCase(unittest.TestCase):
    @parameterized.expand(KTH_LARGEST_ELEMENTS_TEST_CASES)
    def test_top_kth_largest_element(self, nums: List[int], k: int, expected: int):
        actual = kth_largest(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(KTH_LARGEST_ELEMENTS_TEST_CASES)
    def test_top_kth_largest_element_sorting(
        self, nums: List[int], k: int, expected: int
    ):
        actual = kth_largest_sorting(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
