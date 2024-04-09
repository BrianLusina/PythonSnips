from typing import List, Optional
from datastructures.trees.binary.node import BinaryTreeNode, T


def path_sum(root: Optional[BinaryTreeNode], target_sum: T) -> List[List[T]]:
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
        root(BinaryTreeNode): optional binary tree root
        target_sum(T): the target sum

    Returns:
        list: list of all the values in the tree that add up to the target.
    """
    paths = []

    if not root:
        return paths

    def dfs(
        node: Optional[BinaryTreeNode], path: List[T], result: List, remaining_sum: T
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

    dfs(root, [], paths, target_sum)

    return paths
