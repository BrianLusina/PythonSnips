from queue import Queue
from pysnips.data_structures.trees import BinaryTreeNode
from pysnips.data_structures.stacks import Stack

class BinarySearchTree(object):
    def __init__(self, root: BinaryTreeNode = None):
        self.root = root

    def find_largest(self, node):
        current = node
        while current:
            if not current.right:
                return current.value
            current = current.right

    def find_second_largest(self):
        if self.root is None or (self.root.left is None and self.root.right is None):
            raise Exception('Tree must have at least 2 nodes')

        current = self.root

        while current:
            # case: current is largest and has a left subtree
            # 2nd largest is the largest in that subtree
            if current.left and not current.right:
                return self.find_largest(current.left)

            # case: current is parent of largest, and
            # largest has no children, so
            # current is 2nd largest
            if current.right and not current.right.left and not current.right.right:
                return current.value

            current = current.right

    def range_sum(self, low: int, high: int):
        """
        returns the sum of values of all nodes with a value in the range [low, high].

        Example:
        Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
        Output: 32

        Uses an iterative approach to solving the problem with Breadth First Search Traversal

        Complexity Analysis:
        - Time Complexity: O(N), where N is the number of nodes in the tree
        - Space Complexity: O(N)
          - The stack will contain no more than 2 levels of the nodes. The maximal number of nodes in a binary tree is
          N/2. Therefore, the maximal space needed for the stack is O(N)
        """

        ans = 0

        stack = [self.root]

        while stack:
            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    ans += node.val

                if low < node.val:
                    if node.left:
                        stack.append(node.left)

                if node.val < high:
                    if node.right:
                        stack.append(node.right)

        return ans

    def breadth_first_search(self):
        """
        Performs a breadth first search through a Binary Tree
        This will traverse the tree level by level and depth by depth. Using a Queue to put elements into the queue
        """
        queue = Queue()

        # start off by adding the root node
        queue.put(self)

        # while the queue is not empty, we want to traverse the tree and add elements to the queue,
        while not queue.empty():
            current_node = queue.get()

            if current_node.left:
                queue.put(current_node.left)

            if current_node.right:
                queue.put(current_node.right)

    def pre_order(self):
        """
        Type of Depth First Traversal (DFS) for binary trees which will start at root node and proceed to the left
        value and print it until it reaches the leaf(node with no more children) and then backtrack to the node and
        check if the current node has a right child and print it. This will continue until all nodes have been
        tracked and printed.
        """

        if self.root.left:
            self.pre_order()

        if self.root.right:
            self.pre_order()

    def in_order_recurse(self, node: BinaryTreeNode):
        """
        Another type of Depth First Search (DFS) that traverses the tree from the left to middle to right of the tree.
        This type of search will begin at the left node and check if that node has a left child and continually check
        until that left node is a leaf(has no children) and will then print its value and "bubble up" back to the
        current node and execute that (in this case print it) and then print the right node. The same procedure is
        executed for the right side of the tree.
        """
        result = []
        if self.root:
            if self.root.left:
                self.in_order_recurse(self.root.left)

            result.append(self.root.value)

            if self.root.right:
                self.in_order_recurse(self.root.right)

    def in_order_iterate(self):
        """
        Iterative approach using a stack
        """
        result = []
        stack = Stack()
        current = self.root

        while current or not stack.is_empty():
            while current:
                stack.push(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def in_order_morris_traversal(self):
        result = []
        current = self.root
        pre = None

        while current:
            if not current.left:
                # add the current value of the node
                result.append(current.value)
                # Move to next right node
                current = current.right
            else:
                # we have a left subtree
                pre = current.left
                
                # find rightmost
                while pre.right:
                    pre = pre.right

                # put current after the pre node
                pre.right = current
                # store current node
                temp = current
                # move current to top of new tree
                current = current.left
                # original current left be None, avoid infinite loops
                temp.left = None

        return result

    def post_order(self):
        """
        Post order is a another kind of Depth First Search (DFS) algorithm that will search the tree from the left first
         then the right first before
        then proceeding to the middle last, in this case, the root node
        """
        if self.root.left:
            self.post_order()

        if self.root.right:
            self.post_order()

    def is_binary_search_tree(self):
        """
        Checks if a binary search tree is valid. A value of None is a valid Binary Search Tree
        :rtype: bool
        :return: Boolean True if valid, False otherwise
        """
        if self.root is None:
            return True

        stack = [(float("-inf"), self.root, float("inf"))]

        while stack:
            mind, node, maxd = stack.pop()

            if not (mind < node.data < maxd):
                return False

            if node.left is not None:
                stack.append((mind, node.left, node.data))

            if node.right is not None:
                stack.append((node.data, node.right, maxd))
        return True

    def search_node(self, value, node: BinaryTreeNode = None):
        """
        Searches for the given value in a binary search tree. If the value exists in the tree, then True is returned,
        else false
        :param value the value to search for
        :rtype: bool
        """
        if not node:
            node = self.root

        # check if the value is less than the root node and recursively check on the left of the tree
        if value < node.value and node.left:
            return self.search_node(value, node.left)

        # check if the current value is greater than the root node and that the right node exist,
        # then proceed to the right to perform the search
        if value > node.value and node.right:
            return self.search_node(value, node.right)

        # if the root node is equal to the value, then return True if they are equal
        return value == node.value

    def merge_trees(self, otherNode: BinaryTreeNode) -> BinaryTreeNode:
        """
        Merges this tree with another tree given another node
        :param otherNode Other Root node, may be None, therefore we return the root node if availables
        :type BinaryTreeNode
        :returns Binary Tree Node
        """
        if not otherNode:
            return self.root
        
        if not self.root:
            return otherNode

        self.root.value += otherNode.value

        self.root.left = self.merge_trees(otherNode.left)
        self.root.right = self.merge_trees(otherNode.right)

        return self.root

