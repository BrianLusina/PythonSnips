import unittest

from . import BinaryTree, BinaryTreeNode


class BinaryTreeIsCompleteTestCases(unittest.TestCase):
    def test_returns_true_for_no_root(self):
        """Tree with no root should return true"""
        tree = BinaryTree()
        actual = tree.is_complete()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_no_left_nor_right(self):
        """Should return true for tree with root, but no left nor right nodes"""
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)
        actual = tree.is_complete()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right(self):
        """Should return true for root with 2 children, 1 left and 1 right"""
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        root.left = left
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right_and_3_grandchildren(self):
        """Should return true for root with 2 children, 1 left and 1 right, 2 on left and 1 on the right"""
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)

        root.left = left
        root.right = right

        left.left = BinaryTreeNode(4)
        left.right = BinaryTreeNode(5)
        right.left = BinaryTreeNode(6)

        tree = BinaryTree(root=root)
        actual = tree.is_complete()

        self.assertTrue(actual)


class BinaryTreeIsFullTestCases(unittest.TestCase):
    def test_returns_false_for_no_root(self):
        tree = BinaryTree()
        actual = tree.is_full()

        self.assertFalse(actual)

    def test_returns_true_for_root_with_no_left_nor_right(self):
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right(self):
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        root.left = left
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertTrue(actual)

    def test_returns_false_for_tree_with_0_left_and_1_right(self):
        root = BinaryTreeNode(1)
        right = BinaryTreeNode(3)
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertFalse(actual)


class BinaryTreeIsPerfectTestCases(unittest.TestCase):
    def test_returns_false_for_no_root(self):
        tree = BinaryTree()
        actual = tree.is_perfect()

        self.assertFalse(actual)

    def test_returns_true_for_root_with_no_left_nor_right(self):
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)
        actual = tree.is_perfect()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right(self):
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        root.left = left
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_perfect()

        self.assertTrue(actual)

    def test_returns_false_for_tree_with_0_left_and_1_right(self):
        root = BinaryTreeNode(1)
        right = BinaryTreeNode(3)
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_perfect()

        self.assertFalse(actual)

    def test_returns_true_for_tree_with_3_levels_all_filled(self):
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        left_left = BinaryTreeNode(4)
        left_right = BinaryTreeNode(5)
        right_left = BinaryTreeNode(6)
        right_right = BinaryTreeNode(7)

        root.right = right
        root.left = left
        left.left = left_left
        left.right = left_right
        right.left = right_left
        right.right = right_right

        tree = BinaryTree(root=root)
        actual = tree.is_perfect()

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
