import unittest
from typing import List
from parameterized import parameterized
from datastructures.trees.binary.node import BinaryTreeNode
from algorithms.two_pointers.two_sum import (
    two_sum,
    two_sum_with_pointers,
    two_sum_find_target,
)

TWO_SUM_TEST_CASES = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
]

TWO_SUM_TWO_POINTERS_TEST_CASES = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 3, 4], 6, [0, 2]),
    ([-1, 0], -1, [0, 1]),
]

TWO_SUM_INPUT_BST_TEST_CASES = [
    ([7, 3, 13, 2, 5, None, 19], 18, True),
    ([8, 4, None, 0, None, -11], 4, True),
    ([1, None, 2, None, 3, None, 4], 5, True),
    ([900], 900, False),
    ([0, -200, 500, -300, -100, 400, 600], 500, True),
]


class TwoSumTestCase(unittest.TestCase):
    @parameterized.expand(TWO_SUM_TEST_CASES)
    def test_two_sum(self, numbers: List[int], target: int, expected: List[int]):
        actual = two_sum(numbers, target)
        self.assertEqual(expected, actual)

    @parameterized.expand(TWO_SUM_TWO_POINTERS_TEST_CASES)
    def test_two_sum_with_two_pointers(
        self, numbers: List[int], target: int, expected: List[int]
    ):
        actual = two_sum_with_pointers(numbers, target)
        self.assertEqual(expected, actual)

    @parameterized.expand(TWO_SUM_INPUT_BST_TEST_CASES)
    def test_two_sum_input_bst(self, numbers: List[int], target: int, expected: bool):
        root = BinaryTreeNode(numbers[0])
        for data in numbers[1:]:
            if data is not None:
                root.insert_node(data)

        actual = two_sum_find_target(root, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
