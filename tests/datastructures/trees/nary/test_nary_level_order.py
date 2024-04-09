import unittest

from datastructures.trees import TreeNode
from datastructures.trees.nary import NAryTree


class NAryTreeLevelOrderTestCases(unittest.TestCase):
    def test_one(self):
        """input of        10
             /   /    \   \
            2  34    56   100
           / \        |   / | \
          77  88      1   7  8  9 should return [10, 2, 34, 56, 100, 77, 88, 1, 7, 8, 9]"""
        root = TreeNode(10)

        node2 = TreeNode(2)
        node77 = TreeNode(77)
        node88 = TreeNode(88)
        node2.children = [node77, node88]

        node34 = TreeNode(34)

        node56 = TreeNode(56)
        node1 = TreeNode(1)
        node56.children = [node1]

        node100 = TreeNode(100)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node9 = TreeNode(9)
        node100.children = [node7, node8, node9]

        root.children = [node2, node34, node56, node100]

        nary = NAryTree(root)
        actual = nary.level_order_traversal()
        expected = [10, 2, 34, 56, 100, 77, 88, 1, 7, 8, 9]
        self.assertEqual(expected, actual)

    def test_two(self):
        """input of        1
             /   /    \   \
            2  3      4    5
           / \        |  /  | \
          6   7       8 9  10  11 should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
        root = TreeNode(1)

        node2 = TreeNode(2)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node2.children = [node6, node7]

        node3 = TreeNode(3)

        node4 = TreeNode(4)
        node8 = TreeNode(8)
        node4.children = [node8]

        node5 = TreeNode(5)
        node9 = TreeNode(9)
        node10 = TreeNode(10)
        node11 = TreeNode(11)
        node5.children = [node9, node10, node11]

        root.children = [node2, node3, node4, node5]

        nary = NAryTree(root)
        actual = nary.level_order_traversal()
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
