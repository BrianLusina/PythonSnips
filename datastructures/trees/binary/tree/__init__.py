import math
from typing import Optional, List, Any, Generator, Dict, Iterator
from collections import defaultdict, deque

from datastructures.stacks import Stack
from datastructures.trees import Tree, TreeNode, T
from datastructures.trees.binary.node import BinaryTreeNode
from datastructures.queues.fifo import FifoQueue


class BinaryTree(Tree):
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        self.root = root

    def next(self) -> int:
        pass

    @staticmethod
    def create_tree(elements: List[T]) -> "BinaryTree":
        """
        Factory method to creates a BinaryTree given a list of values
        If the index of any element in the array is i, the element in the index 2i+1 will become the left child and
        the element in the index 2i+2 will become the right child. The parent of any element at index is the lower bound
        of (i-1)/2
        """

        if not elements:
            return BinaryTree()

        def level_order(arr: List[T], index: int):
            node = None
            if index < len(elements):
                node = BinaryTreeNode(data=arr[index])

                node.left = level_order(arr, 2 * index + 1)
                node.right = level_order(arr, 2 * index + 2)

            return node

        root = level_order(elements, 0)
        tree = BinaryTree(root=root)

        return tree

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

    def inorder_traversal(self) -> List[T]:
        data = []
        if not self.root:
            return data

        def inorder_helper(root: BinaryTreeNode):
            if not root:
                return
            inorder_helper(root.left)
            data.append(root.data)
            inorder_helper(root.right)

        inorder_helper(self.root)
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

        Time Complexity: O(N) where N is the number of nodes in the binary tree.
        In the worst case we might be visiting all the nodes of the binary tree.

        Space Complexity: O(N).
        This is because the maximum amount of space utilized by the recursion stack would be N since the height of a
        skewed binary tree could be N.

        Args:
            node_one(BinaryTreeNode): Node 1
            node_two(BinaryTreeNode): Node 2

        Return:
            BinaryTreeNode: if there is a lowest common ancestor node for both nodes, it is returned. if not, None is
            returned. Note that None is returned if 1 of the nodes it not present in the tree
        """

        if not self.root:
            return None

        def lca_util(
                node: Optional[BinaryTreeNode],
                node_one_value: T,
                node_two_val: T,
                node_lookup: List[bool],
        ) -> Optional[BinaryTreeNode]:
            """Returns the Lowest Common Ancestor of 2 node values.This updates a node lookup list that has 2 values.
            The first index is for node_one_value and the second index is for node_two_value. They will be updated to
            True if either node is available in the tree. This will recursively go down the tree until a leaf node is
            encountered

            Args:
                node(BinaryTreeNode): root node of subtree
                node_one_value(T): Value for node 1
                node_two_val(T): Value for node 2
                node_lookup(list): Node lookup list to update the presence of a node value in the tree

            Return:
                BinaryTreeNode: Lowest Common Ancestor for the tree if available
            """

            if node is None:
                return None

            if node.data == node_one_value:
                node_lookup[0] = True
                return node

            if node.data == node_two_val:
                node_lookup[1] = True
                return node

            left_lca = lca_util(node.left, node_one_value, node_two_val, node_lookup)
            right_lca = lca_util(node.right, node_one_value, node_two_val, node_lookup)

            if left_lca and right_lca:
                return node

            return left_lca if left_lca is not None else right_lca

        def is_key_in_subtree(current_node: Optional[BinaryTreeNode], key: T) -> bool:
            # If reached the end of a branch, return False.
            if current_node is None:
                return False

            # If key is present at root, or if left subtree or right subtree , return true
            if (
                    current_node.data == key
                    or is_key_in_subtree(current_node.left, key)
                    or is_key_in_subtree(current_node.right, key)
            ):
                return True

            return False

        lookup = [False, False]
        lca = lca_util(self.root, node_one.data, node_two.data, lookup)

        if (
                lookup[0]
                and lookup[1]
                or lookup[0]
                and is_key_in_subtree(lca, node_two.data)
                or lookup[1]
                and is_key_in_subtree(lca, node_one.data)
        ):
            return lca

        return None

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

            return is_complete_helper(root.left, 2 * idx + 1) and is_complete_helper(
                root.right, 2 * index + 2
            )

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

            return is_perfect_helper(root.left, level + 1) and is_perfect_helper(
                root.right, level + 1
            )

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

    def leaf_similar(self, other: "BinaryTree") -> bool:
        if (self.root is None and other.root is not None) or (
                other.root is None and self.root is not None
        ):
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

    def number_of_good_nodes(self) -> int:
        # no root, no nodes, therefore, return 0
        if self.root is None:
            return 0

        # root is regarded as good, so, if there are no left & right children, return 1
        if not self.root.left and not self.root.right:
            return 1

        def good_nodes_helper(node: BinaryTreeNode, data: T) -> int:
            if node is not None:
                node_count = good_nodes_helper(
                    node.left, max(data, node.data)
                ) + good_nodes_helper(node.right, max(data, node.data))
                if node.data >= data:
                    node_count += 1
                return node_count
            return 0

        return good_nodes_helper(self.root, self.root.data)

    def path_sum(self, target: T) -> int:
        if self.root is None:
            return 0

        def count_paths(
                sum_hash: Dict[int, int], prefix_sum: T, node: BinaryTreeNode
        ) -> int:
            if node is None:
                return 0

            # sum of current path
            prefix_sum += node.data

            # number of paths that end at current node
            path = sum_hash[prefix_sum - target]

            # add current sum to prefix sum hash
            sum_hash[prefix_sum] += 1

            # traverse left and right of tree
            path += count_paths(sum_hash, prefix_sum, node.left) + count_paths(
                sum_hash, prefix_sum, node.right
            )

            # remove current sum from prefix sum hash
            sum_hash[prefix_sum] -= 1

            return path

        # DFS, initialize sum_hash with prefix sum of 0, occurring once
        return count_paths(defaultdict(int, {0: 1}), 0, self.root)

    def paths_to_target(self, target: T) -> List[T]:
        """Finds all the paths of a tree that add up to the target.

        Uses a DFS approach to traverse the tree from the root to leaf nodes checking if the sum along the path adds up to
        the target. If that path is found, it's added to the path list and backtracked up a level to traverse down another
        subtree along the same path recursively.

        Complexity: here 'n' is the number of nodes in the tree

        Time Complexity: O(n):
            As traversal is done using DFS, the time complexity at the worst and best case is O(n) as the algorithm has to
            check all paths to find all the possible paths that add up to the target

        Space Complexity: O(n):
            The algorithm stores each path found that adds up to the target in a 'paths' list. The worst case is that all
            paths add up to the target sum and we end up storing the whole tree in the list and returning it.

        Args:
            target(T): the target

        Returns:
            list: list of all the values in the tree that add up to the target.
        """
        paths = []

        if not self.root:
            return paths

        def dfs(
                node: Optional[BinaryTreeNode],
                path: List[T],
                result: List,
                remaining_sum: T,
        ):
            """Traverses the tree from root to leaf paths in a depth first search manner.

            The Remaining sum is subtracted from the node's value when the tree is being traversed. If a leaf node is reached
            and the remaining sum is equal to the leaf node's value, then it's added to the path.
            if path = [5,4,11,2] and remainingSum = targetSum = 22
            traverse node 5, remainingSum = 22 - 5 = 17
            traverse node 4, remainingSum = 17 - 4 = 13
            traverse node 11, remainingSum = 13 - 11 = 2
            traverse node 2, remainingSum = 2 - 2 = 0
            remainingSum is 0 which means the sum of the current path is equal to targetSum
            so how to find another path?
            We can backtrack here,
            we can pop back a node and try another
            e.g. path = [5, 4, 11, 7]
            pop 7 out = [5, 4, 11]
            push 2 = [5, 4, 11, 2]
            ... etc

            Args:
                node(BinaryTreeNode): root of subtree
                path(list): store the current route
                result(list): final result of dfs traversal is updated here
                remaining_sum(T): store the remaining sum that is needed to calculate the initial target_sum.

            Returns:
                None
            """
            if not node:
                return

            # add the current node to a path
            path.append(node.data)

            # this checks if the current node is a leaf node
            # the remaining_sum == node.data, checks if the remaining_sum - node.data == 0
            # if both are true, then one of the paths has been found
            if not node.left and not node.right and remaining_sum == node.data:
                # lists passed a function are just references (i.e., Pass By Reference)
                # and path.pop() would pop them all eventually,
                # therefore, you need to create a new list there
                # or your can use ans.append(path[:]) / ans.append(path.copy())
                result.append(path[:])

            # traverse left subtree with an updated remaining sum
            # we don't need to check if left subtree is null or not
            # as we handle it in the first line of this function
            dfs(node.left, path, result, remaining_sum - node.data)

            # traverse right subtree with an updated remaining sum
            # we don't need to check if right subtree is null or not
            # as we handle it in the first line of this function
            dfs(node.right, path, result, remaining_sum - node.data)

            # backtrack
            path.pop()

        dfs(self.root, [], paths, target)

        return paths

    def longest_zig_zag(self) -> int:
        if self.root is None or (self.root.left is None and self.root.right is None):
            return 0

        self.path_length = 0

        def dfs(node: Optional[BinaryTreeNode], go_left: bool, steps: int):
            if node is not None:
                self.path_length = max(self.path_length, steps)
                if go_left:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)

        dfs(self.root, False, 0)
        dfs(self.root, True, 0)

        return self.path_length

    def longest_zig_zag_stack(self) -> int:
        if self.root is None or (self.root.left is None and self.root.right is None):
            return 0

        path_length = 0
        stack = [(self.root, 0, None)]

        while stack:
            node, length, last = stack.pop()
            if last is None:
                if node.left is not None:
                    stack.append((node.left, length + 1, "left"))
                if node.right is not None:
                    stack.append((node.right, length + 1, "right"))
            elif last == "left":
                if node.left is not None:
                    stack.append((node.left, 1, "left"))
                if node.right is not None:
                    stack.append((node.right, length + 1, "right"))
                path_length = max(path_length, length)
            elif last == "right":
                if node.right is not None:
                    stack.append((node.right, 1, "right"))
                if node.left is not None:
                    stack.append((node.left, length + 1, "left"))
                path_length = max(path_length, length)

        return path_length

    def right_view(self) -> List[T]:
        """Return a list of values representing the right view of a binary tree

        Returns:
            List: list of values in each node
        """
        if self.root is None:
            return []

        if self.root.left is None and self.root.right is None:
            return [self.root.data]

        result = []

        queue = deque([self.root])
        while queue:
            level_length = len(queue)

            result.append(queue[0].data)

            for x in range(level_length):
                node = queue.popleft()

                if node.right is not None:
                    queue.append(node.right)

                if node.left is not None:
                    queue.append(node.left)

        return result

    def max_level_sum(self) -> int:
        """Uses BFS to find the highest level with the maximum sum of all the nodes at that level"""
        if self.root is None:
            return 0

        if self.root.left is None and self.root.right is None:
            return 1

        maximum_sum = self.root.data
        level = 0
        smallest_level = 1

        levels = deque()
        levels.append(self.root)

        while levels:
            level += 1
            sum_at_current_level_sum = 0

            for _ in range(len(levels)):
                node = levels.popleft()
                sum_at_current_level_sum += node.data

                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)

            if sum_at_current_level_sum > maximum_sum:
                smallest_level = level
                maximum_sum = sum_at_current_level_sum

        return smallest_level

    def visible_tree_nodes(self) -> int:
        """Finds the visible tree nodes. We define a node "visible" when no node on the root-to-itself path (inclusive)
        has a strictly greater value. The root is always "visible" since there are no other nodes between the root and
        itself

        Complexity:

        - Time Complexity: O(n)
            There are n nodes and n - 1 edges in a tree so if we traverse each once then the total traversal is O(2n - 1)
            which is O(n).

        - Space Complexity: O(h)
            stack memory where h is the height of the tree, which is O(n) in the worst case.

        Returns:
            int: number of visible nodes
        """

        def dfs(node: Optional[BinaryTreeNode], max_so_far: T) -> int:
            if node is None:
                return 0

            total = 0
            if node.data >= max_so_far:
                total += 1

            # max_so_far for child node is the largest of previous max and current node val
            total += dfs(node.left, max(max_so_far, node.data))
            total += dfs(node.right, max(max_so_far, node.data))

            return total

        return dfs(self.root, -math.inf)

    def serialize(self) -> str:
        result = []

        def dfs(node: BinaryTreeNode):
            if not node:
                # x denotes an empty value, that is None
                result.append("x")
                return
            result.append(str(node.data))
            dfs(node.left)
            dfs(node.right)

        dfs(self.root)

        return " ".join(result)

    @staticmethod
    def deserialize(tree_str: str) -> Optional[BinaryTreeNode]:
        def dfs(nodes: Iterator[str]) -> Optional[BinaryTreeNode]:
            data = next(nodes)

            if data == "x":
                return

            current = BinaryTreeNode(data)
            current.left = dfs(nodes)
            current.right = dfs(nodes)
            return current

        return dfs(iter(tree_str.split()))
