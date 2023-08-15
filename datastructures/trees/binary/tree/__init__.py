from typing import Optional, List, Any, Generator

from datastructures.stacks import Stack
from datastructures.trees import Tree, TreeNode
from datastructures.trees.binary.node import BinaryTreeNode
from datastructures.queues.fifo import FifoQueue


class BinaryTree(Tree):
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        self.root = root

    def next(self) -> int:
        pass

    def height(self) -> int:
        if self.root is None:
            return 0

        # if we don't have either left and right nodes from the root, we return 1
        if self.root.left is None and self.root.right is None:
            return 1

        height = 0
        queue = FifoQueue()
        queue.enqueue(self.root)

        while True:
            current_level_nodes = queue.size

            if current_level_nodes == 0:
                return height

            height += 1

            while current_level_nodes > 0:
                node = queue.dequeue()

                if node.left is not None:
                    queue.enqueue(node.left)

                if node.right is not None:
                    queue.enqueue(node.right)
                current_level_nodes -= 1

    def has_next(self) -> bool:
        pass

    def increasing_order_traversal(self) -> TreeNode:
        pass

    def get_depth(self) -> int:
        depth = 0
        node = self.root
        while node:
            depth += 1
            node = node.left
        return depth

    def insert_node(self, value) -> TreeNode:
        pass

    def paths(self) -> list:
        pass

    def level_order_traversal(self) -> List[Any]:
        if not self.root:
            return []

        current_level = [self.root]
        levels = []
        while current_level:
            level = []
            next_level = []

            for node in current_level:
                level.append(node.data)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            levels.append(level)
            current_level = next_level

        return levels

    def pre_order_traversal(self) -> List[Any]:
        data = []
        if not self.root:
            return data

        def pre_order_helper(root: BinaryTreeNode):
            if not root:
                return
            data.append(root.data)
            pre_order_helper(root.left)
            pre_order_helper(root.right)

        pre_order_helper(self.root)
        return data

    def flatten_into_linked_list(self) -> None:
        """
        Flattens a binary tree into a linked list.
        @return:
        """
        dfs = [self.root]
        while self.root and dfs:
            tree_node = dfs.pop()
            if tree_node.right:
                dfs.append(tree_node.right)
            if tree_node.left:
                dfs.append(tree_node.left)
                tree_node.right = tree_node.left
                tree_node.left = None
            else:
                if dfs:
                    tree_node.right = dfs[-1]
                    tree_node.left = None

    def lowest_common_ancestor(
            self, node_one: BinaryTreeNode, node_two: BinaryTreeNode
    ) -> Optional[BinaryTreeNode]:
        """
        The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of
        the nodes node_one or node_two,
        return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths.
        The least common ancestor would
        then be the node for which both the subtree recursions return a True flag.
        It can also be the node which itself is one of node_one or node_two and for which one of the subtree recursions
         returns a True flag.

        Let us look at the formal algorithm based on this idea.

        Algorithm

        - Start traversing the tree from the root node.
        - If the current node itself is one of node_one or node_two, we would mark a variable mid as True and continue
        the search for the other node in the left and right branches.
        - If either of the left or the right branch returns True, this means one of the two nodes was found below.
        - If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have
        found the lowest common ancestor for the nodes p and q.

        Complexity Analysis

        Time Complexity: O(N) where NN is the number of nodes in the binary tree.
        In the worst case we might be visiting all the nodes of the binary tree.

        Space Complexity: O(N).
        This is because the maximum amount of space utilized by the recursion stack would be N since the height of a
        skewed binary tree could be N.

        """

        if not self.root:
            return None

        lca = None

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of node_one or node_two
            mid = current_node == node_one or current_node == node_two

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                lca = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        recurse_tree(self.root)
        return lca

    def __len__(self) -> int:
        if not self.root:
            return 0

        counter = 1
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            node = stack.pop()

            if node.left:
                counter += 1
                stack.push(node.left)

            if node.right:
                counter += 1
                stack.push(node.right)

        return counter

    def is_full(self) -> bool:
        """
        Checks if a binary tree is a full binary tree.
        A full binary tree is a tree whose nodes(parent & internal) have either 2 or no children
        :return: True if binary tree is full, false otherwise
        """

        def is_full_helper(root: BinaryTreeNode) -> bool:
            """
            Helper function that recurses over subtrees from the root checking if each subtree is a full binary tree
            :param root: Root of binary subtree
            :return: True if the binary subtree is a full binary tree
            """
            # if we have no root, then this is not a tree, yet, to begin with
            if root is None:
                return False

            # if the root has no left nor right subtrees, then this is a full binary tree by definition
            if root.left is None and root.right is None:
                return True

            if root.left is not None and root.right is not None:
                return is_full_helper(root.left) and is_full_helper(root.right)

            return False

        return is_full_helper(self.root)

    def is_complete(self) -> bool:
        """
        Checks if a binary tree is a complete binary tree
        :return: true if is a complete binary tree, false otherwise
        """
        if self.root is None:
            return True

        node_count = len(self)

        def is_complete_helper(root, idx: int) -> bool:
            if root is None:
                return True

            if idx >= node_count:
                return False

            return is_complete_helper(root.left, 2 * idx + 1) and is_complete_helper(root.right, 2 * index + 2)

        index = 0
        return is_complete_helper(self.root, index)

    def is_perfect(self) -> bool:
        """
        Checks if a binary tree is perfect
        :return: true if tree is perfect, false otherwise
        """
        if self.root is None:
            return False

        if self.root.left is None and self.root.right is None:
            return True

        depth = self.get_depth()

        def is_perfect_helper(root: BinaryTreeNode, level: int = 0) -> bool:
            if root is None:
                return True

            if root.left is None and root.right is None:
                return depth == level + 1

            if root.left is None and root.right is None:
                return False

            return is_perfect_helper(root.left, level + 1) and is_perfect_helper(root.right, level + 1)

        return is_perfect_helper(self.root, 0)

    def is_balanced(self) -> bool:
        """
        Checks if a binary is balanced
        @return:
        """
        if self.root is None:
            return True

        def is_height_balanced(node: BinaryTreeNode) -> bool:
            left_height = 0
            right_height = 0

            if node is None:
                return True

            l = is_height_balanced(node.left)
            r = is_height_balanced(node.right)

            if abs(left_height - right_height) <= 1:
                return l and r

            return False

        return is_height_balanced(self.root)

    def leaf_similar(self, other: 'BinaryTree') -> bool:
        if (self.root is None and other.root is not None) or (other.root is None and self.root is not None):
            return False

        def dfs(node: Optional[BinaryTreeNode]) -> Generator:
            if node is not None:
                if node.left is None and node.right is None:
                    yield node.data
                yield from dfs(node.left)
                yield from dfs(node.right)

        leaves1 = list(dfs(self.root))
        leaves2 = list(dfs(other.root))

        return leaves1 == leaves2
