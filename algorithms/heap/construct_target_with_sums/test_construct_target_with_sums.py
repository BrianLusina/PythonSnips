import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.construct_target_with_sums import is_possible, is_possible_2

CONSTRUCT_TARGET_WITH_SUMS_TEST_CASES = [
    ([9, 3, 5], True),
    ([1, 1, 1, 2], False),
    ([8, 5], True),
    ([3, 5, 1], True),
    ([1, 1, 10], False),
    ([1, 1, 10], False),
    ([1], True),
    ([1, 2], True),
]


class ConstructTargetWithSumsTestCase(unittest.TestCase):
    @parameterized.expand(CONSTRUCT_TARGET_WITH_SUMS_TEST_CASES)
    def test_is_possible(self, target: List[int], expected: bool):
        actual = is_possible(target)
        self.assertEqual(expected, actual)

    @parameterized.expand(CONSTRUCT_TARGET_WITH_SUMS_TEST_CASES)
    def test_is_possible_2(self, target: List[int], expected: bool):
        actual = is_possible_2(target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
