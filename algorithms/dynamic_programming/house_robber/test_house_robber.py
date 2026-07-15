import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.house_robber import (
    rob,
    rob_iii_recursion,
    rob_iii_dynamic_programming_top_down,
    rob_iii_dynamic_programming_bottom_up,
)
from datastructures.trees.binary.node import BinaryTreeNode

ROB_TEST_CASES = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([], 0),
    ([3], 3),
    ([3, 5], 5),
]

ROB_III_TEST_CASES = [
    (
        BinaryTreeNode(
            data=3,
            left=BinaryTreeNode(data=2, right=BinaryTreeNode(data=3)),
            right=BinaryTreeNode(data=3, right=BinaryTreeNode(data=1)),
        ),
        7,
    ),
    (
        BinaryTreeNode(
            data=3,
            left=BinaryTreeNode(
                data=4, left=BinaryTreeNode(data=1), right=BinaryTreeNode(data=3)
            ),
            right=BinaryTreeNode(data=5, right=BinaryTreeNode(data=1)),
        ),
        9,
    ),
    (
        BinaryTreeNode(
            data=1,
            left=BinaryTreeNode(
                data=4,
                left=BinaryTreeNode(data=2, left=BinaryTreeNode(data=3)),
                right=BinaryTreeNode(data=3),
            ),
        ),
        7,
    ),
    (
        BinaryTreeNode(
            data=1,
            right=BinaryTreeNode(
                data=2,
                left=BinaryTreeNode(
                    data=3, left=BinaryTreeNode(data=4), right=BinaryTreeNode(data=2)
                ),
                right=BinaryTreeNode(data=5),
            ),
        ),
        12,
    ),
    (
        BinaryTreeNode(
            data=3,
            left=BinaryTreeNode(data=2, left=BinaryTreeNode(data=3)),
            right=BinaryTreeNode(data=3, right=BinaryTreeNode(data=1)),
        ),
        7,
    ),
    (
        BinaryTreeNode(
            data=3,
            left=BinaryTreeNode(
                data=5, left=BinaryTreeNode(data=10), right=BinaryTreeNode(data=12)
            ),
            right=BinaryTreeNode(
                data=25, left=BinaryTreeNode(data=3), right=BinaryTreeNode(data=1)
            ),
        ),
        47,
    ),
    (
        BinaryTreeNode(
            data=9,
            left=BinaryTreeNode(
                data=7, left=BinaryTreeNode(data=1), right=BinaryTreeNode(data=8)
            ),
            right=BinaryTreeNode(
                data=11, left=BinaryTreeNode(data=10), right=BinaryTreeNode(data=12)
            ),
        ),
        40,
    ),
    (
        BinaryTreeNode(
            data=3,
        ),
        3,
    ),
    (
        BinaryTreeNode(
            data=8,
            left=BinaryTreeNode(data=7),
            right=BinaryTreeNode(data=10),
        ),
        17,
    ),
    (
        BinaryTreeNode(
            data=15,
            left=BinaryTreeNode(
                data=10,
                left=BinaryTreeNode(
                    data=5, left=BinaryTreeNode(data=3), right=BinaryTreeNode(data=7)
                ),
                right=BinaryTreeNode(
                    data=12, left=BinaryTreeNode(data=11), right=BinaryTreeNode(data=13)
                ),
            ),
            right=BinaryTreeNode(
                data=25, left=BinaryTreeNode(data=20), right=BinaryTreeNode(data=30)
            ),
        ),
        99,
    ),
]


class RobTestCase(unittest.TestCase):
    @parameterized.expand(ROB_TEST_CASES)
    def test_rob(self, nums: List[int], expected: int):
        actual = rob(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(ROB_III_TEST_CASES)
    def test_rob_iii_recursion(self, root: BinaryTreeNode, expected: int):
        actual = rob_iii_recursion(root)
        self.assertEqual(expected, actual)

    @parameterized.expand(ROB_III_TEST_CASES)
    def test_rob_iii_dynamic_programming_top_down(
        self, root: BinaryTreeNode, expected: int
    ):
        actual = rob_iii_dynamic_programming_top_down(root)
        self.assertEqual(expected, actual)

    @parameterized.expand(ROB_III_TEST_CASES)
    def test_rob_iii_dynamic_programming_bottom_up(
        self, root: BinaryTreeNode, expected: int
    ):
        actual = rob_iii_dynamic_programming_bottom_up(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
