import unittest

from . import BinaryTree, BinaryTreeNode


class BinaryTreeCreateTreeTestCases(unittest.TestCase):
    def test_create_tree_1(self):
        """should create a tree from [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]"""
        elements = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
        tree = BinaryTree.create_tree(elements)

        self.assertEqual(1, tree.root.data)
        self.assertIsNone(tree.root.left)


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

        self.assertEqual(0, actual)

    def test_returns_1_for_root_but_no_children(self):
        """should return 1 if the binary tree has a root, but no left nor right subtrees"""
        root = BinaryTreeNode(data=1)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEqual(1, actual)

    def test_returns_3_for_tree_3_9_20_null_null_15_7(self):
        """should return 3 if the binary tree [3,9,20,null,null,15,7]"""
        left = BinaryTreeNode(data=9)
        right_left = BinaryTreeNode(data=15)
        right_right = BinaryTreeNode(data=7)
        right = BinaryTreeNode(data=20, left=right_left, right=right_right)

        root = BinaryTreeNode(data=3, left=left, right=right)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEqual(3, actual)

    def test_returns_2_for_tree_1_null_20(self):
        """should return 2 if the binary tree [1,null,20]"""
        right = BinaryTreeNode(data=2)

        root = BinaryTreeNode(data=1, right=right)
        tree = BinaryTree(root=root)

        actual = tree.height()
        self.assertEqual(2, actual)


class BinaryTreeLeafSimilarTest(unittest.TestCase):
    def test_1(self):
        """should return true for tree1=3,5,1,6,2,9,8,null,null,7,4 and tree2=3,5,1,6,7,4,2,null,null,null,null,null,null,9,8"""
        left1 = BinaryTreeNode(
            5,
            left=BinaryTreeNode(6),
            right=BinaryTreeNode(2, left=BinaryTreeNode(7), right=BinaryTreeNode(4)),
        )
        right1 = BinaryTreeNode(1, left=BinaryTreeNode(9), right=BinaryTreeNode(8))

        root1 = BinaryTreeNode(3, left=left1, right=right1)
        tree1 = BinaryTree(root1)

        left2 = BinaryTreeNode(5, left=BinaryTreeNode(6), right=BinaryTreeNode(7))
        right2 = BinaryTreeNode(
            1,
            left=BinaryTreeNode(4),
            right=BinaryTreeNode(2, left=BinaryTreeNode(9), right=BinaryTreeNode(8)),
        )

        root2 = BinaryTreeNode(3, left=left2, right=right2)
        tree2 = BinaryTree(root2)

        actual = tree1.leaf_similar(tree2)

        self.assertTrue(actual)

    def test_2(self):
        """should return false for tree1= and tree2="""
        root1 = BinaryTreeNode(data=1, left=BinaryTreeNode(2), right=BinaryTreeNode(3))
        tree1 = BinaryTree(root=root1)

        root2 = BinaryTreeNode(data=1, left=BinaryTreeNode(3), right=BinaryTreeNode(2))
        tree2 = BinaryTree(root=root2)

        actual = tree1.leaf_similar(tree2)
        self.assertFalse(actual)


class BinaryTreeGoodNodesTest(unittest.TestCase):
    def test_1(self):
        """should return 4 for tree=[3,1,4,3,null,1,5]"""
        root = BinaryTreeNode(
            3,
            left=BinaryTreeNode(1, left=BinaryTreeNode(3)),
            right=BinaryTreeNode(4, left=BinaryTreeNode(1), right=BinaryTreeNode(5)),
        )
        tree = BinaryTree(root)

        actual = tree.number_of_good_nodes()

        self.assertEqual(4, actual)

    def test_2(self):
        """should return 3 for tree=[3,3,null,4,2]"""
        root = BinaryTreeNode(
            data=3,
            left=BinaryTreeNode(3, right=BinaryTreeNode(2), left=BinaryTreeNode(4)),
        )
        tree = BinaryTree(root=root)

        actual = tree.number_of_good_nodes()
        self.assertEqual(3, actual)

    def test_3(self):
        """should return 1 for tree=[1]"""
        root = BinaryTreeNode(data=1)
        tree = BinaryTree(root=root)

        actual = tree.number_of_good_nodes()
        self.assertEqual(1, actual)


class BinaryTreePathSumTest(unittest.TestCase):
    def test_1(self):
        """should return 3 for tree=[10,5,-3,3,2,null,11,3,-2,null,1] and target=8"""
        root = BinaryTreeNode(
            10,
            left=BinaryTreeNode(
                data=5,
                left=BinaryTreeNode(
                    3, left=BinaryTreeNode(3), right=BinaryTreeNode(-2)
                ),
                right=BinaryTreeNode(2, right=BinaryTreeNode(1)),
            ),
            right=BinaryTreeNode(-3, right=BinaryTreeNode(11)),
        )
        tree = BinaryTree(root)
        target = 8
        actual = tree.path_sum(target=target)
        expected = 3

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for tree=[5,4,8,11,null,13,4,7,2,null,null,5,1] and target=22"""
        root = BinaryTreeNode(
            data=5,
            left=BinaryTreeNode(
                4,
                left=BinaryTreeNode(
                    11, left=BinaryTreeNode(7), right=BinaryTreeNode(2)
                ),
                right=BinaryTreeNode(
                    8,
                    left=BinaryTreeNode(
                        13, left=BinaryTreeNode(5), right=BinaryTreeNode(1)
                    ),
                    right=BinaryTreeNode(4),
                ),
            ),
        )
        tree = BinaryTree(root=root)
        target = 22
        actual = tree.path_sum(target=target)
        expected = 3
        self.assertEqual(expected, actual)


class BinaryTreeLongestZigZagTest(unittest.TestCase):
    def test_1(self):
        """should return 3 for tree=[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]"""
        right_right = BinaryTreeNode(
            1,
            left=BinaryTreeNode(1, right=BinaryTreeNode(1, right=BinaryTreeNode(1))),
            right=BinaryTreeNode(1),
        )

        right_left = BinaryTreeNode(1)

        right = BinaryTreeNode(1, left=right_left, right=right_right)

        root = BinaryTreeNode(1, right=right)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag()
        expected = 3

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 4 for tree=[1,1,1,null,1,null,null,1,1,null,1]"""

        left_right = BinaryTreeNode(
            1,
            right=BinaryTreeNode(1),
            left=(BinaryTreeNode(1, right=BinaryTreeNode(1))),
        )
        left = BinaryTreeNode(1, right=left_right)

        right = BinaryTreeNode(1)

        root = BinaryTreeNode(data=5, left=left, right=right)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag()
        expected = 4
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 for tree=[1]"""
        root = BinaryTreeNode(data=1)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag()
        expected = 0
        self.assertEqual(expected, actual)

    def test_1_with_stack(self):
        """should return 3 for tree=[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]"""
        right_right = BinaryTreeNode(
            1,
            left=BinaryTreeNode(1, right=BinaryTreeNode(1, right=BinaryTreeNode(1))),
            right=BinaryTreeNode(1),
        )

        right_left = BinaryTreeNode(1)

        right = BinaryTreeNode(1, left=right_left, right=right_right)

        root = BinaryTreeNode(1, right=right)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag_stack()
        expected = 3

        self.assertEqual(expected, actual)

    def test_2_with_stack(self):
        """should return 4 for tree=[1,1,1,null,1,null,null,1,1,null,1]"""

        left_right = BinaryTreeNode(
            1,
            right=BinaryTreeNode(1),
            left=(BinaryTreeNode(1, right=BinaryTreeNode(1))),
        )
        left = BinaryTreeNode(1, right=left_right)

        right = BinaryTreeNode(1)

        root = BinaryTreeNode(data=5, left=left, right=right)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag_stack()
        expected = 4
        self.assertEqual(expected, actual)

    def test_3_with_stack(self):
        """should return 0 for tree=[1]"""
        root = BinaryTreeNode(data=1)

        tree = BinaryTree(root=root)

        actual = tree.longest_zig_zag_stack()
        expected = 0
        self.assertEqual(expected, actual)


class BinaryTreeRightViewTest(unittest.TestCase):
    def test_1(self):
        """should return list of 1 element with root data for tree with root along"""
        root = BinaryTreeNode(1)

        tree = BinaryTree(root=root)

        expected = [1]
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return empty list for tree with no root"""
        tree = BinaryTree()

        expected = []
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_3(self):
        """should return list [1, 3, 7, 8] for tree:
                1
              /   \
             2    3
            / \  / \
           4   5 6  7
          /
         8
        """

        left = BinaryTreeNode(
            2, left=BinaryTreeNode(4, left=BinaryTreeNode(8)), right=BinaryTreeNode(5)
        )
        right = BinaryTreeNode(3, left=BinaryTreeNode(6), right=BinaryTreeNode(7))

        root = BinaryTreeNode(1, left=left, right=right)

        tree = BinaryTree(root)

        expected = [1, 3, 7, 8]
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_4(self):
        """should return list [1, 3, 4, 5] for tree:
            1
           /  \
          2    3
           \
            4
             \
              5
        """

        left = BinaryTreeNode(2, right=BinaryTreeNode(4, right=BinaryTreeNode(5)))
        right = BinaryTreeNode(3)

        root = BinaryTreeNode(1, left=left, right=right)

        tree = BinaryTree(root)

        expected = [1, 3, 4, 5]
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_5(self):
        """should return list [1, 3, 4] for tree:
            1
           /  \
          2    3
           \     \
            5     4
        """

        left = BinaryTreeNode(2, right=BinaryTreeNode(5))
        right = BinaryTreeNode(3, right=BinaryTreeNode(4))

        root = BinaryTreeNode(1, left=left, right=right)

        tree = BinaryTree(root)

        expected = [1, 3, 4]
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_6(self):
        """should return list [1, 3] for tree:
            1
             \
              3
        """

        right = BinaryTreeNode(3)

        root = BinaryTreeNode(1, right=right)

        tree = BinaryTree(root)

        expected = [1, 3]
        actual = tree.right_view()

        self.assertEqual(expected, actual)

    def test_7(self):
        """should return list [3, 20, 7] for tree:
            3       <-  3
           / \
          9   20    <-  20
             /  \
            15   7  <-  7
        """
        left = BinaryTreeNode(9)
        right = BinaryTreeNode(20, left=BinaryTreeNode(15), right=BinaryTreeNode(7))

        root = BinaryTreeNode(3, right=right, left=left)

        tree = BinaryTree(root)

        expected = [3, 20, 7]
        actual = tree.right_view()

        self.assertEqual(expected, actual)


class BinaryTreeMaxLevelSumTests(unittest.TestCase):
    def test_1_returns_1(self):
        """should return 1 for tree [1]"""
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)

        actual = tree.max_level_sum()
        expected = 1
        self.assertEqual(expected, actual)

    def test_null_returns_0(self):
        """should return 0 for tree [null]"""
        tree = BinaryTree()

        actual = tree.max_level_sum()
        expected = 0
        self.assertEqual(expected, actual)

    def test_1_7_0_7_neg8_null_null_returns_2(self):
        """should return 2 for tree 1,7,0,7,-8,null,null]"""
        left = BinaryTreeNode(7, left=BinaryTreeNode(7), right=BinaryTreeNode(-8))
        right = BinaryTreeNode(0)
        root = BinaryTreeNode(1, left=left, right=right)
        tree = BinaryTree(root=root)

        actual = tree.max_level_sum()
        expected = 2
        self.assertEqual(expected, actual)

    def test_neg100_neg200_neg300_neg20_neg5_neg10_null_returns_3(self):
        """should return 3 for tree [-100,-200,-300,-20,-5,-10,null]"""
        left = BinaryTreeNode(-200, left=BinaryTreeNode(-20), right=BinaryTreeNode(-5))

        right = BinaryTreeNode(-300, left=BinaryTreeNode(-10))

        root = BinaryTreeNode(-100, left=left, right=right)

        tree = BinaryTree(root=root)

        actual = tree.max_level_sum()
        expected = 3
        self.assertEqual(expected, actual)


class BinaryTreePreOrderTraversal(unittest.TestCase):
    def test_1(self):
        """Should return [F,B,A,D,C,E,G,I,H]"""
        expected = ["F", "B", "A", "D", "C", "E", "G", "I", "H"]
        right = BinaryTreeNode("G", right=BinaryTreeNode("I", left=BinaryTreeNode("H")))
        left = BinaryTreeNode("B", left=BinaryTreeNode("A"),
                              right=BinaryTreeNode("D", left=BinaryTreeNode("C"), right=BinaryTreeNode("E")))
        root = BinaryTreeNode("F", left=left, right=right)

        tree = BinaryTree(root=root)
        actual = tree.pre_order_traversal()
        self.assertListEqual(expected, actual)


class BinaryTreeInOrderTraversal(unittest.TestCase):
    def test_1(self):
        """Should return [A, B, C, D, E, F, G, H, I]"""
        expected = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        right = BinaryTreeNode("G", right=BinaryTreeNode("I", left=BinaryTreeNode("H")))
        left = BinaryTreeNode("B", left=BinaryTreeNode("A"),
                              right=BinaryTreeNode("D", left=BinaryTreeNode("C"), right=BinaryTreeNode("E")))
        root = BinaryTreeNode("F", left=left, right=right)

        tree = BinaryTree(root=root)
        actual = tree.inorder_traversal()
        self.assertListEqual(expected, actual)


class BinaryTreePostOrderTraversal(unittest.TestCase):
    def test_1(self):
        """Should return [A, C, E, D, B, H, I, G, F]"""
        expected = ["A", "C", "E", "D", "B", "H", "I", "G", "F"]
        right = BinaryTreeNode("G", right=BinaryTreeNode("I", left=BinaryTreeNode("H")))
        left = BinaryTreeNode("B", left=BinaryTreeNode("A"),
                              right=BinaryTreeNode("D", left=BinaryTreeNode("C"), right=BinaryTreeNode("E")))
        root = BinaryTreeNode("F", left=left, right=right)

        tree = BinaryTree(root=root)
        actual = tree.post_order_traversal()
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
