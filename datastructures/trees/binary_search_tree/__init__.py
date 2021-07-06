from .. import Tree
from ..binary_tree_node import BinaryTreeNode
from ...queues.fifo import FifoQueue
from ...stacks import Stack


class BinarySearchTree(Tree):
    def __init__(self, root: BinaryTreeNode = None):
        self.root = root
        self.stack = Stack()

    @property
    def height(self) -> int:
        if not self.root:
            return 0

        # if we don't have either left and right nodes from the root, we return 0
        if not self.root.left and not self.root.right:
            return 0

        height = 1
        queue = FifoQueue()
        queue.add(self.root)

        while True:
            current_level_nodes = queue.size

            if current_level_nodes == 0:
                return height

            height += 1

            while current_level_nodes > 0:
                node = queue.dequeue()

                if node.left:
                    queue.add(node.left)

                if node.right:
                    queue.add(node.right)
                current_level_nodes -= 1

    def next(self) -> int:
        """
        Returns the next smallest number in a BST.
        This involves two major operations. One is where we pop an element from the stack which becomes the next smallest element to return. This is a O(1) operation. 
        However, we then make a call to our helper function _leftmost_inorder which iterates over a bunch of nodes. This is clearly a linear time operation i.e. O(N) in the worst case.
        However, the important thing to note here is that we only make such a call for nodes which have a right child. Otherwise, we simply return. 
        Also, even if we end up calling the helper function, it won't always process N nodes. They will be much lesser. Only if we have a skewed tree would there be N nodes for the root. 
        But that is the only node for which we would call the helper function.
        
        Thus, the amortized (average) time complexity for this function would still be O(1). We don't need to have a solution which gives constant time operations for every call. 
        We need that complexity on average and that is what we get.
        """

        # this is the smallest element in the BST
        topmost_node = self.stack.pop()

        # if the node has a right child, call the helper function for the right child to 
        # get the next smallest item
        # We don't need to check for the left child because of the way we have added nodes onto the stack. 
        # The topmost node either won't have a left child or would already have the left subtree processed. 
        # If it has a right child, then we call our helper function on the node's right child. 
        # This would comparatively be a costly operation depending upon the structure of the tree
        if topmost_node.right:
            self.__leftmost_inorder(topmost_node.right)

        return topmost_node.data

    def has_next(self) -> bool:
        """
        Checks if the BST has items left. Since this uses a stack, then we simply check if the stack still has items.
        This is used in an iterator approach to getting items from the BST. This returns True if there are items & False
        otherwise, the Time Complexity here is O(1)
        """
        return self.stack.is_empty()

    def __leftmost_inorder(self, root: BinaryTreeNode) -> None:
        # Add all the nodes of the left most branch to the stack
        while root:
            self.stack.push(root)
            root = root.left

    def insert_node(self, value: int) -> BinaryTreeNode:
        """
        Inserts a node in a BST given a value
        If there is not root, then create a new root node with the value and return.

        If there is a root, then check the value against the root node's value and determine if it should go left or right
        If the value is greater than the root node's value, then go right, if the value is less than the root node's value,
        then go left. Repeat this operation, until we can insert the node in the right place.

        Alternatively, this tree can be re-arranged to form a new tree.

        This has used an iterative approach. However, a recursive approach can also be adopted.

        if not self.root:
            return BinaryTreeNode(value)

        if value < self.root.value and self.root.left:
            self.insert_node(value, self.root.left)

        elif value <= self.root.value:
            self.root.left = BinaryTreeNode(value)
            
        elif value > self.root.value and self.root.right:
            self.insert_node(value, self.root.right)
        else:
            self.root.right = BinaryTreeNode(value)

        return self.root
        """
        if not self.root:
            return BinaryTreeNode(value)

        parent, dummy = self.root, self.root

        while self.root:
            parent = self.root

            if value < self.root.data:
                self.root = self.root.left
            else:
                self.root = self.root.right

        if not parent:
            parent = BinaryTreeNode(value)
        elif value < parent.data:
            parent.left = BinaryTreeNode(value)
        else:
            parent.right = BinaryTreeNode(value)

        return dummy

    def find_largest(self, node: BinaryTreeNode) -> BinaryTreeNode:
        """
        Simply finds the largest node in a BST. We walk rightward down the BST until the current node has no right child
        and return it. This assumes that the Tree is a valid BST
        :param node: root node, or current node
        :return: Value of the largest node
        :rtype: object
        """
        current = node
        while current:
            if not current.right:
                return current
            current = current.right

        return current

    def find_second_largest(self) -> BinaryTreeNode:
        """
        Finds the second largest node in the Binary Search Tree given a root node
        :param root_node: BinaryTreeNode
        :type root_node BinaryTreeNode
        :return: Value of the second largest Node
        :rtype: object
        """
        if not self.root or (not self.root.left and not self.root.right):
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
                return current

            current = current.right

        return current

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

    def breadth_first_search(self) -> list:
        """
        Performs a breadth first search through a Binary Tree
        This will traverse the tree level by level and depth by depth. Using a Queue to put elements into the queue
        """
        queue = FifoQueue()

        # start off by adding the root node
        queue.add(self.root)

        # while the queue is not empty, we want to traverse the tree and add elements to the queue,
        while not queue.is_empty():
            current_node = queue.dequeue()

            if current_node.left:
                queue.add(current_node.left)

            if current_node.right:
                queue.add(current_node.right)

    def pre_order(self) -> list:
        """
        Type of Depth First Traversal (DFS) for binary trees which will start at root node and proceed to the left
        value and print it until it reaches the leaf(node with no more children) and then backtrack to the node and
        check if the current node has a right child and print it. This will continue until all nodes have been
        tracked and printed.
        """
        result = []
        stack = Stack()

        if not self.root:
            return result

        current = self.root

        while current or not stack.is_empty():
            while current:
                result.append(current.value)
                stack.push(current)
                current = current.left

            current = stack.pop()

            current = current.right

        return result

    def increasing_order_traversal(self) -> BinaryTreeNode:
        if not self.root:
            return None

        def inorder(node: BinaryTreeNode):
            if node:
                yield from inorder(node.left)
                yield node.value
                yield from inorder(node.right)

        result = current = BinaryTreeNode(None)
        for value in inorder(self.root):
            current.right = BinaryTreeNode(value)
            current = current.right

        return result.right

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

    def in_order_iterate(self) -> list:
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
            result.append(current.data)
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

    def post_order(self) -> list:
        """
        1. Push root to first stack.
        2. Loop while first stack is not empty
            2.1 Pop a node from first stack and push it to second stack
            2.2 Push left and right children of the popped node to first stack
        3. Print contents of second stack        
        """
        if not self.root:
            return

        # create 2 stacks
        stack_one = Stack()
        stack_two = Stack()
        values = []

        # push root to stack one
        stack_one.push(self.root)

        # while stack 1 is not empty
        while stack_one:

            # pop a node from stack 1 and add it to stack 2
            node = stack_one.pop()
            stack_two.push(node)

            # push left & right children of removed item to stack one
            if node.left:
                stack_one.push(node.left)

            if node.right:
                stack_one.push(node.right)

        while stack_two:
            node = stack_two.pop()
            values.append(node.data)

        return values

    def is_binary_search_tree(self):
        """
        Checks if a binary search tree is valid. A value of None is a valid Binary Search Tree
        :rtype: bool
        :return: Boolean True if valid, False otherwise
        """

        # Tree with no root is still valid
        if not self.root:
            return True

        # start with the root with an arbitrarily low lower bound and an arbitrarily higher bound
        stack = [(float("-inf"), self.root, float("inf"))]

        # depth first traversal
        while len(stack):
            mind, node, maxd = stack.pop()

            if not node:
                continue

            # if this node is invalid, return false immediately
            if node.data < mind or node.data > maxd:
                return False

            if node.left:
                # this node must be less than the current node
                stack.append((mind, node.left, node.data))

            if node.right:
                # this node must be greater than the current node
                stack.append((node.data, node.right, maxd))

        # if none of the nodes are invalid, return true
        # at this point we have checked all the nodes
        return True

    def is_binary_search_tree_recursive(self, root: BinaryTreeNode, lower_bound=-float("inf"),
                                        upper_bound=float("inf")):
        """
        This uses the call stack to check if the binary search tree node is valid.
        This will work, but is vulnerable to stack overflow error
        Possible :exception: OverflowError
        :param root: Binary search tree node to check for
        :param lower_bound: the lower bound set arbitrarily
        :param upper_bound: upper bound set arbitrarily
        :return: True/False if the root is a valid binary search tree
        :rtype: bool
        """

        if not root:
            return True

        # if the value is out of bounds
        if root.value > upper_bound or root.value < lower_bound:
            return False

        return not (
                not self.is_binary_search_tree_recursive(root.left, lower_bound, root.value)
                or not self.is_binary_search_tree_recursive(root.right, root.value, upper_bound)
        )

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

    def is_balanced(self, node: BinaryTreeNode) -> bool:
        """
        Checks if a binary tree is balanced
        :param tree_root: The tree root or a BinaryTreeNode
        :return: True/False, if a binary tree is balanced
        :rtype: bool
        """
        tree_root = node or self.root

        # short circuit as soon as we find more than 2
        depths = []

        # treat this list as a stack, that will store tuples of (node, depth)
        # give the stack a maximum size of the length of the tree root
        # alternatively, we could use a list
        # nodes = []
        nodes = Stack(len(tree_root))

        # nodes.append((tree_root, 0))
        nodes.push((tree_root, 0))

        while len(nodes):
            # pop a node and its depth from the top of a stack
            node, depth = nodes.pop()

            # case, we found a leaf
            if not node.left and not node.right:

                # we only care if it is a new depth
                if depth not in depths:
                    depths.append(depth)

                    # two ways we might now have an unbalanced tree:
                    #   1) more than 2 different leaf depths
                    #   2) 2 leaf depths that are more than 1 apart
                    if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                        return False

            # case, this is not a leaf, keep stepping down
            else:
                if node.left:
                    nodes.push((node.left, depth + 1))
                if node.right:
                    nodes.push((node.right, depth + 1))

        return True

    def lowest_common_ancestor(self, node_one: BinaryTreeNode, node_two: BinaryTreeNode) -> BinaryTreeNode:
        """
        Considering it is a BST, we can assume that this tree is a valid BST, we could also check for this
        If both of the values in the 2 nodes provided are greater than the root node, then we move to the right.
        if the nodes are less than the root node, we move to the left.
        If there is no root node, then we exit and return None, as no common ancestor could exist in such a case with
        no root node.
        
        Assumptions:
        - assumes that the node itself can also be an ancestor/descendant of itself

        Complexity Analysis:

        Time Complexity: O(h).
        The Time Complexity of the above solution is O(h), where h is the height of the tree.

        Space Complexity: O(1).
        The space complexity of the above solution is constant.
        """

        if not self.root:
            return None

        # if any of the node values matches the data value for the root node, return the root node
        if self.root.data == node_one.value or self.root.data == node_two.value:
            return self.root

        while self.root:
            # if both node_one and node_two are smaller than root, then LCA lies in the left
            if self.root.data > node_one.value and self.root.data > node_two.value:
                self.root = self.root.left

            # if both node_one and node_two are greater than root, then LCA lies in the right
            elif self.root.data < node_one.value and self.root.data < node_two.value:
                self.root = self.root.right
            else:
                break

        return self.root

    @property
    def paths(self) -> list:
        """
        Gets all the paths of this tree from root node to leaf nodes
        """
        if not self.root:
            return []

        stack = Stack()
        stack.push((self.root, ""))
        res = []

        while stack:
            node, path = stack.pop()

            if not (node.left or node.right):
                res.append(path + str(node.data))

            if node.left:
                stack.push((node.left, path + str(node.data) + "->"))

            if node.right:
                stack.push((node.right, path + str(node.data) + "->"))

        return [list(map(int, x.split("->"))) for x in res]

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
