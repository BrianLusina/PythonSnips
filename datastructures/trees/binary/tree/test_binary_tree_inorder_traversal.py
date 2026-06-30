import unittest

from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.node import BinaryTreeNode


class BinaryTreeInOrderTraversal(unittest.TestCase):
    def test_1(self):
        """Should return [A, B, C, D, E, F, G, H, I]"""
        expected = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        right = BinaryTreeNode("G", right=BinaryTreeNode("I", left=BinaryTreeNode("H")))
        left = BinaryTreeNode(
            "B",
            left=BinaryTreeNode("A"),
            right=BinaryTreeNode(
                "D", left=BinaryTreeNode("C"), right=BinaryTreeNode("E")
            ),
        )
        root = BinaryTreeNode("F", left=left, right=right)

        tree = BinaryTree(root=root)
        actual = tree.inorder_traversal()
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
