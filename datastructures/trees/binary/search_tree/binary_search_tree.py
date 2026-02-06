from typing import List, Any, Optional
from datastructures.trees.binary.node import BinaryTreeNode

from datastructures.queues.fifo import FifoQueue
from datastructures.stacks.dynamic import DynamicSizeStack
from datastructures.trees import T
from datastructures.trees.binary.tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        super().__init__(root)
        self.stack = DynamicSizeStack()

    def __len__(self) -> int:
        if not self.root:
            return 0

        counter = 1
        stack = DynamicSizeStack()
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

    @staticmethod
    def construct_bst(items: List[T]) -> Optional["BinarySearchTree"]:
        """
        Constructs a binary search tree from a sorted list of items.

        This method works by recursively finding the middle element of the list and assigning it to the root of the tree.
        The left and right subtrees are then constructed by recursively calling the method on the left and right halves
        of the list.

        @param items: A sorted list of items to construct the tree from.
        @return: A binary search tree constructed from the items.
        """
        if not items:
            return None

        def construct_bst_helper(left: int, right: int) -> Optional[BinaryTreeNode]:
            # base case for the method if the left is greater than the right
            if left > right:
                return None

            # Find the middle index - this element becomes the root
            # Using (left + right) // 2 ensures we get the left-middle for even-length arrays
            mid = (left + right) // 2
            root = BinaryTreeNode(items[mid])
            root.left = construct_bst_helper(left, mid - 1)
            root.right = construct_bst_helper(mid + 1, right)
            return root

        return BinarySearchTree(root=construct_bst_helper(0, len(items) - 1))

    def insert_node(self, data: Optional[T]):
        """
        Inserts a node in a BST given an element
        If there is no root, then create a new root node with the data and return it

        If there is a root, then check the data against the root node's data and determine if it should go left or right
        If the data is greater than the root node's data, then go right, if the data is less than the root node's data,
        then go left. Repeat this operation, until we can insert the node in the right place.
        """
        if not self.root:
            self.root = BinaryTreeNode(data)
            return

        def insert_helper(value: T, node: BinaryTreeNode) -> BinaryTreeNode:
            if not node:
                return BinaryTreeNode(data)
            if value < node.data:
                node.left = insert_helper(value, node.left)
            else:
                node.right = insert_helper(value, node.right)
            return node

        if data:
            insert_helper(data, self.root)

    def delete_node(self, key: T) -> Optional[BinaryTreeNode]:
        """Deletes a node from the Binary Search Tree. If the node is found, it is deleted and the tree re-ordered to
        remain a valid binary search tree.

        This will be typically an O(log(n) operation because deletion requires a search plus a few extra steps to deal
        with any hanging children.

        Args:
            key (T): Value to delete from binary search tree

        Return:
            BinaryTreeNode: New root of binary search tree
        """
        # nothing to delete here as root is none
        if self.root is None:
            return self.root

        def delete_helper(
            value: T, node: Optional[BinaryTreeNode]
        ) -> Optional[BinaryTreeNode]:
            # base case when we have hit the bottom of the tree, and the parent node has no children
            if node is None:
                return None
            # if the value to delete is less than or greater than the current node, we set the left or right child
            # respectively to be the return value of a recursive call of this very method on the current node's left or
            # right subtree
            elif value < node.data:
                node.left = delete_helper(value, node.left)

                # we return the current node (and its subtree if existent) to be used as the new value of its parent's
                # left or right child
                return node
            elif value > node.data:
                node.right = delete_helper(value, node.right)
                return node
            # if the current node is the one we want to delete
            elif value == node.data:
                # if the current node has no left child, we delete it by returning it's right child (and it's subtree if
                # existent) to be its parent's new subtree
                if node.left is None:
                    return node.right
                # if the node has no left nor right child, this ends up being None as per the first line of code in this
                # function
                elif node.right is None:
                    return node.left
                # if the current node has 2 children, we delete the current node by calling the lift function, which
                # changes the current node's value to the value of it's successor node
                else:
                    node.right = lift(node.right, node)
                    return node
            return None

        def lift(
            node: BinaryTreeNode, node_to_delete: BinaryTreeNode
        ) -> BinaryTreeNode:
            # if the current node of this function has a left child, we recursively call this function to continue down
            # the left subtree to find the successor node
            if node.left is not None:
                node.left = lift(node.left, node_to_delete)
                return node
            # if the current node has no left child, that means the current node of this function is the successor node
            # and we take its value and make it the new value of the node that we are deleting.
            else:
                node_to_delete.data = node.data
                # we return the successor node's right child to be now used as its parent's left child
                return node.right

        return delete_helper(key, self.root)

    @property
    def height(self) -> int:
        if self.root is None:
            return 0

        # if we don't have either left and right nodes from the root, we return 1
        if not self.root.left and not self.root.right:
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
        :return: Value of the second largest Node
        :rtype: object
        """
        if not self.root or (not self.root.left and not self.root.right):
            raise Exception("Tree must have at least 2 nodes")

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

    def find_kth_largest(self, k: int) -> Optional[BinaryTreeNode]:
        """
        Finds the kth largest value in a binary search tree. This uses a reverse in order traversal moving from right
        to root to left until the kth largest node can be found. We don't have to traverse the whole tree since binary
        search trees are already ordered following the property of the right subtree has nodes which have the left
        sub-tree always less than their parent and the right subtree has nodes with values that are either equal to or
        greater than the parent. With this property in mind, we perform a reverse in order traversal to be able to move
        from right to root to left to find the kth largest node in the tree.

        Complexity:
        Time: O(h + k): where h is the height of the tree and k is the input
        Space: O(h): where h is the height of the tree.

        Args:
            k (int): The kth largest value to find
        Returns:
            Optional[BinaryTreeNode]: The kth largest node
        """

        # This is a helper class that helps to track the algorithm's progress of traversing the tree
        class TreeInfo:
            def __init__(self):
                self.number_of_nodes_visited: int = 0
                self.latest_visited_node: Optional[BinaryTreeNode] = None

        def reverse_in_order_traverse(node: BinaryTreeNode, tree_information: TreeInfo):
            """
            Helper function to traverse the tree in reverse in order
            Args:
                node (BinaryTreeNode): The node to traverse
                tree_information (TreeInfo): The tree information
            """
            # base case: if node is None or we've already found the kth largest
            if not node or tree_information.number_of_nodes_visited >= k:
                return

            # traverse right subtree first for larger values
            reverse_in_order_traverse(node.right, tree_information)

            # Visit the current node if we haven't found k nodes yet
            if tree_information.number_of_nodes_visited < k:
                tree_information.number_of_nodes_visited += 1
                tree_information.latest_visited_node = node

            # traverse the left subtree for smaller values if needed
            reverse_in_order_traverse(node.left, tree_information)

        tree_info = TreeInfo()
        reverse_in_order_traverse(self.root, tree_info)
        return tree_info.latest_visited_node

    def find_closest_value_in_bst(self, target: T) -> Optional[BinaryTreeNode]:
        """
        Finds the closest value in the binary search tree to the given target value.

        Args:
            target T: Value to search for
        Returns:
            Node with the closest value to the target
        """
        # edge case for empty nodes, if none is provided, we can't find a value that is close to the target
        if not self.root:
            return None

        # if the node's data is the target, exit early by returning it
        if self.root.data == target:
            return self.root

        # this keeps track of the minimum on both the left and the right
        closest_node = self.root
        min_diff = abs(target - self.root.data)
        current = self.root

        # while the queue is not empty, we pop off nodes from the queue and check for their values
        while current:
            current_diff = abs(target - current.data)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_node = current

            if current.data == target:
                return current

            if target < current.data:
                current = current.left
            else:
                current = current.right

        return closest_node

    def range_sum(self, low: int, high: int):
        """
        returns the sum of datas of all nodes with a data in the range [low, high].

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
                if low <= node.data <= high:
                    ans += node.data

                if low < node.data:
                    if node.left:
                        stack.append(node.left)

                if node.data < high:
                    if node.right:
                        stack.append(node.right)

        return ans

    def breadth_first_search(self) -> List[Any]:
        """
        Performs a breadth first search through a Binary Tree
        This will traverse the tree level by level and depth by depth. Using a Queue to put elements into the queue
        """
        queue = FifoQueue()

        # start off by adding the root node
        queue.enqueue(self.root)

        # while the queue is not empty, we want to traverse the tree and add elements to the queue,
        while not queue.is_empty():
            current_node = queue.dequeue()

            if current_node.left:
                queue.enqueue(current_node.left)

            if current_node.right:
                queue.enqueue(current_node.right)

    def pre_order(self) -> List[Any]:
        """
        Type of Depth First Traversal (DFS) for binary trees which will start at root node and proceed to the left
        data and print it until it reaches the leaf(node with no more children) and then backtrack to the node and
        check if the current node has a right child and print it. This will continue until all nodes have been
        tracked and printed.
        """
        result = []
        stack = DynamicSizeStack()

        if not self.root:
            return result

        current = self.root

        while current or not stack.is_empty():
            while current:
                result.append(current.data)
                stack.push(current)
                current = current.left

            current = stack.pop()

            current = current.right

        return result

    def increasing_order_traversal(self) -> Optional[BinaryTreeNode]:
        if not self.root:
            return None

        def inorder(node: BinaryTreeNode):
            if node:
                yield from inorder(node.left)
                yield node.data
                yield from inorder(node.right)

        result = current = BinaryTreeNode(None)
        for data in inorder(self.root):
            current.right = BinaryTreeNode(data)
            current = current.right

        return result.right

    def in_order_recurse(self, node: BinaryTreeNode) -> List[T]:
        """
        Another type of Depth First Search (DFS) that traverses the tree from the left to middle to right of the tree.
        This type of search will begin at the left node and check if that node has a left child and continually check
        until that left node is a leaf(has no children) and will then print its data and "bubble up" back to the
        current node and execute that (in this case print it) and then print the right node. The same procedure is
        executed for the right side of the tree.
        """
        result = []
        if self.root:
            if self.root.left:
                self.in_order_recurse(self.root.left)

            result.append(self.root.data)

            if self.root.right:
                self.in_order_recurse(self.root.right)
        return result

    def in_order_iterate(self) -> List[T]:
        """
        Iterative approach using a stack
        """
        result = []
        stack = DynamicSizeStack()
        current = self.root

        while current or not stack.is_empty():
            while current:
                stack.push(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)
            current = current.right

        return result

    def in_order_morris_traversal(self) -> List[Any]:
        result = []
        current = self.root
        pre = None

        while current:
            if not current.left:
                # add the current data of the node
                result.append(current.data)
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

    def post_order(self) -> List[Any]:
        """
        1. Push root to first stack.
        2. Loop while first stack is not empty
            2.1 Pop a node from first stack and push it to second stack
            2.2 Push left and right children of the popped node to first stack
        3. Print contents of second stack
        """
        if not self.root:
            return []

        # create 2 stacks
        stack_one = DynamicSizeStack()
        stack_two = DynamicSizeStack()
        data = []

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
            data.append(node.data)

        return data

    def get_depth(self) -> int:
        pass

    def level_order_traversal(self) -> List[Any]:
        pass

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

    def is_valid(self):
        """
        Checks if a binary search tree is valid. A data of None is a valid Binary Search Tree
        Complexity Analysis:
        Space Complexity: O(n) as we are using a stack to keep track of the nodes, where n is the height of the tree
        Time Complexity: O(n), worst case we travers all the nodes of the tree(left sub tree and right sub tree) to
        check if the tree is a valid BST
        :rtype: bool
        :return: Boolean True if valid, False otherwise
        """

        # Tree with no root is still valid
        if not self.root:
            return True

        # start with the root with an arbitrarily low lower bound and an arbitrarily higher bound
        stack = [(float("-inf"), self.root, float("inf"))]

        # depth first traversal
        while stack:
            lower_bound, node, upper_bound = stack.pop()

            if not node:
                continue

            # if this node is invalid, return false immediately
            if node.data <= lower_bound or node.data >= upper_bound:
                return False

            if node.left:
                # this node must be less than the current node
                stack.append((lower_bound, node.left, node.data))

            if node.right:
                # this node must be greater than the current node
                stack.append((node.data, node.right, upper_bound))

        # if none of the nodes are invalid, return true
        # at this point we have checked all the nodes
        return True

    def is_valid_recursive(self):
        """
        This uses the call stack to check if the binary search tree node is valid.
        This will work, but is vulnerable to stack overflow error
        Possible :exception: OverflowError
        :return: True/False if the root is a valid binary search tree
        :rtype: bool
        """

        if not self.root:
            return True

        def is_valid_recursive_helper(
            node: BinaryTreeNode, low=-float("inf"), high=float("inf")
        ):
            """
            This uses the call stack to check if the binary search tree node is valid.
            This will work, but is vulnerable to stack overflow error
            Possible :exception: OverflowError
            :param node: Binary search tree node to check for
            :param low: the lower bound set arbitrarily
            :param high: upper bound set arbitrarily
            :return: True/False if the root is a valid binary search tree
            :rtype: bool
            """

            if not node:
                return True

            # if the data is out of bounds
            if node.data >= high or node.data <= low:
                return False

            return not (
                not is_valid_recursive_helper(node.left, low, node.data)
                or not is_valid_recursive_helper(node.right, node.data, high)
            )

        lower_bound = float("-inf")
        upper_bound = float("inf")
        return is_valid_recursive_helper(self.root, lower_bound, upper_bound)

    def search_node(self, data: T) -> bool:
        """
        Searches for the given data in a binary search tree. If the data exists in the tree, then True is returned,
        else false
        Arguments:
            data: data to search for
        """

        def search_helper(current: Optional[BinaryTreeNode], value: T) -> bool:
            """
            Search helper that is used to search the binary search tree for the given value
            Arguments:
                current: the current binary search tree node, could be a missing value
                value: the value to search for
            """
            if current:
                if current.data == value:
                    return True
                elif current.data < value:
                    return search_helper(current.right, value)
                else:
                    return search_helper(current.left, value)
            return False

        return search_helper(self.root, data)

    def merge_trees(self, other_node: BinaryTreeNode) -> BinaryTreeNode:
        """
        Merges this tree with another tree given another node
        :param other_node Other Root node, may be None, therefore we return the root node if availables
        :type BinaryTreeNode
        :returns Binary Tree Node
        """
        if not other_node:
            return self.root

        if not self.root:
            return other_node

        self.root.data += other_node.data

        self.root.left = self.merge_trees(other_node.left)
        self.root.right = self.merge_trees(other_node.right)

        return self.root

    def is_balanced(self) -> bool:
        """
        Checks if a binary tree is balanced
        :return: True/False, if a binary tree is balanced
        :rtype: bool
        """
        if self.root is None:
            return True

        tree_root = self.root

        # short circuit as soon as we find more than 2
        depths = []

        # treat this list as a stack, that will store tuples of (node, depth)
        # give the stack a maximum size of the length of the tree root
        # alternatively, we could use a list
        # nodes = []
        nodes = DynamicSizeStack()

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
                    if len(depths) > 2 or (
                        len(depths) == 2 and abs(depths[0] - depths[1]) > 1
                    ):
                        return False

            # case, this is not a leaf, keep stepping down
            else:
                if node.left:
                    nodes.push((node.left, depth + 1))
                if node.right:
                    nodes.push((node.right, depth + 1))

        return True

    def lowest_common_ancestor(
        self, node_one: BinaryTreeNode, node_two: BinaryTreeNode
    ) -> BinaryTreeNode:
        """
        Considering it is a BST, we can assume that this tree is a valid BST, we could also check for this
        If both of the datas in the 2 nodes provided are greater than the root node, then we move to the right.
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

        # if any of the node datas matches the data data for the root node, return the root node
        if self.root.data == node_one.data or self.root.data == node_two.data:
            return self.root

        while self.root:
            # if both node_one and node_two are smaller than root, then LCA lies in the left
            if self.root.data > node_one.data and self.root.data > node_two.data:
                self.root = self.root.left

            # if both node_one and node_two are greater than root, then LCA lies in the right
            elif self.root.data < node_one.data and self.root.data < node_two.data:
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

        stack = DynamicSizeStack()
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

    def inorder_successor(self, node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        """
        Returns the inorder successor of the node. If there is no node, None is returned. The inorder successor of the
        node is the node with the smallest value greater than node.data in the binary search tree.

        This assumes that the node is in the tree already.

        Complexity:

        Time Complexity: The time complexity of this solution is O(n) in the worst-case scenario where the given tree
        is skewed. However, for a balanced binary search tree, it will be O(logn).

        Space Complexity: O(1) because we don't use any additional space.

        Args:
            node (BinaryTreeNode): node to search for inorder successor
        Returns:
            Optional[BinaryTreeNode]: returns inorder successor of node if available, else None
        """
        if not self.root:
            return None

        successor = None
        current = self.root

        # current is the best candidate so far
        while current:
            # when current.data is greater than the node.data, we have found a valid successor, so, we save it in the
            # successor variable
            if current.data > node.data:
                successor = current
                # Move left to find a better(smaller) candidate. By moving to current.left, we are exploring values that
                # are smaller than current.data. Since we want the smallest possible successor, we must check the left
                # side of current to see if there is a node that is still greater than node.data, but close to node.data
                current = current.left
            else:
                # this node is too small, so we must go right to find a larger value
                current = current.right

        return successor

    def sum_nodes_in_range(self, low: int, high: int) -> int:
        """
        Finds and sums all the nodes in the range [low, high]. Utilizes pruning to avoid checking subtrees whose values
        fall outside the range [low, high].
        Args:
             low (int): Lower bound.
             high (int): Upper bound.
        Returns:
            int: Total sum of nodes within the range [low, high].
        """

        def dfs(node: Optional[BinaryTreeNode]):
            if not node:
                return 0
            if node.data < low:
                return dfs(node.right)
            if node.data > high:
                return dfs(node.left)
            return node.data + dfs(node.left) + dfs(node.right)

        return dfs(self.root)
