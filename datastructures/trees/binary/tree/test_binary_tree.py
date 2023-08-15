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


class BinaryTreeIsBalancedTestCases(unittest.TestCase):
    def test_returns_true_for_no_root(self):
        """should return True if the binary tree has no root"""
        tree = BinaryTree()
        actual = tree.is_balanced()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_no_left_nor_right(self):
        """should return true for tree with root only"""
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)
        actual = tree.is_balanced()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right(self):
        """should return true for tree with root and 2 children"""
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        root.left = left
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_balanced()

        self.assertTrue(actual)

    def test_returns_true_for_tree_with_0_left_and_1_right(self):
        """should return true for tree with root with 2 children"""
        left_left = BinaryTreeNode(4)
        left_right = BinaryTreeNode(5)

        left = BinaryTreeNode(2, left=left_left, right=left_right)
        right = BinaryTreeNode(3)

        root = BinaryTreeNode(1, left, right)

        tree = BinaryTree(root=root)
        actual = tree.is_balanced()

        self.assertTrue(actual)


class BinaryTreeHeight(unittest.TestCase):

    def test_returns_0_for_no_root(self):
        """should return 0 if the binary tree has no root"""
        tree = BinaryTree()
        actual = tree.height()

        self.assertEquals(0, actual)

    def test_returns_1_for_root_but_no_children(self):
        """should return 1 if the binary tree has a root, but no left nor right subtrees"""
        root = BinaryTreeNode(data=1)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEquals(1, actual)

    def test_returns_3_for_tree_3_9_20_null_null_15_7(self):
        """should return 3 if the binary tree [3,9,20,null,null,15,7]"""
        left = BinaryTreeNode(data=9)
        right_left = BinaryTreeNode(data=15)
        right_right = BinaryTreeNode(data=7)
        right = BinaryTreeNode(data=20, left=right_left, right=right_right)

        root = BinaryTreeNode(data=3, left=left, right=right)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEquals(3, actual)

    def test_returns_2_for_tree_1_null_20(self):
        """should return 2 if the binary tree [1,null,20]"""
        right = BinaryTreeNode(data=2)

        root = BinaryTreeNode(data=1, right=right)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEquals(2, actual)


class BinaryTreeLeafSimilarTest(unittest.TestCase):

    def test_1(self):
        """should return true for tree1=3,5,1,6,2,9,8,null,null,7,4 and tree2=3,5,1,6,7,4,2,null,null,null,null,null,null,9,8"""
        left1 = BinaryTreeNode(5, left=BinaryTreeNode(6),
                               right=BinaryTreeNode(2, left=BinaryTreeNode(7), right=BinaryTreeNode(4)))
        right1 = BinaryTreeNode(1, left=BinaryTreeNode(9), right=BinaryTreeNode(8))

        root1 = BinaryTreeNode(3, left=left1, right=right1)
        tree1 = BinaryTree(root1)

        left2 = BinaryTreeNode(5, left=BinaryTreeNode(6), right=BinaryTreeNode(7))
        right2 = BinaryTreeNode(1, left=BinaryTreeNode(4),
                                right=BinaryTreeNode(2, left=BinaryTreeNode(9), right=BinaryTreeNode(8)))

        root2 = BinaryTreeNode(3, left=left2, right=right2)
        tree2 = BinaryTree(root2)

        actual = tree1.leaf_similar(tree2)

        self.assertTrue(actual)

    def test_2(self):
        """should return false for tree1= and tree2= """
        root1 = BinaryTreeNode(data=1, left=BinaryTreeNode(2), right=BinaryTreeNode(3))
        tree1 = BinaryTree(root=root1)

        root2 = BinaryTreeNode(data=1, left=BinaryTreeNode(3), right=BinaryTreeNode(2))
        tree2 = BinaryTree(root=root2)

        actual = tree1.leaf_similar(tree2)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
