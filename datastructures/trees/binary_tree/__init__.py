from .. import Tree
from ..binary_tree_node import BinaryTreeNode
from ...stacks import Stack


class BinaryTree(Tree):

    def __init__(self, root: BinaryTreeNode = None):
        self.root = root

    def lowest_common_ancestor(self, node_one: BinaryTreeNode, node_two: BinaryTreeNode) -> BinaryTreeNode:
        """
        The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of the nodes node_one or node_two, 
        return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would 
        then be the node for which both the subtree recursions return a True flag. 
        It can also be the node which itself is one of node_one or node_two and for which one of the subtree recursions returns a True flag.

        Let us look at the formal algorithm based on this idea.

        Algorithm

        - Start traversing the tree from the root node.
        - If the current node itself is one of node_one or node_two, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
        - If either of the left or the right branch returns True, this means one of the two nodes was found below.
        - If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.        
        
        Complexity Analysis

        Time Complexity: O(N) where NN is the number of nodes in the binary tree. 
        In the worst case we might be visiting all the nodes of the binary tree.

        Space Complexity: O(N). 
        This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.

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
