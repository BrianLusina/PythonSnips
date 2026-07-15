from typing import Optional, Deque, List
from collections import deque
from datastructures.trees.binary.node import BinaryTreeNode


def lowest_common_ancestor(
    node_one: BinaryTreeNode, node_two: BinaryTreeNode
) -> BinaryTreeNode | None:
    """
    Returns the lowest common ancestor of 2 nodes in the Binary Tree.
    The lowest common ancestor of 2 nodes is the node farthest from the root that is an ancestor of both nodes.
    This function first collects all ancestors of node_one by traversing upwards from node_one to the root, collecting
    all nodes.
    Then, it performs a depth-first search from node_two, checking each ancestor. The first node it finds that's already
    in its set is the lowest common ancestor.
    If no lowest common ancestor is found, None is returned.

    :param node_one: BinaryTreeNode
    :param node_two: BinaryTreeNode
    :return: BinaryTreeNode | None
    """
    # create a set to store all ancestors of node_one. We traverse upward from node_one to the root, collecting all nodes
    ancestors = set()

    current = node_one
    while current is not None:
        # add the current node to the ancestor set
        ancestors.add(current)
        # move up to the parent
        current = current.parent

    # Now perform DFS from node_two, checking each ancestor. The first node we find that's already in our set is the
    # LCA
    current = node_two
    while current is not None:
        if current in ancestors:
            # This is the first common ancestor we've found. Since we're traversing from bottom to top, this is the
            # lowest common ancestor
            return current
        # move up to the parent
        current = current.parent

    # given the constraints, this should not happen
    return None


def lowest_common_ancestor_ptr(
    node_one: BinaryTreeNode, node_two: BinaryTreeNode
) -> BinaryTreeNode | None:
    """
    Returns the lowest common ancestor of 2 nodes in the Binary Tree using a two-pointer approach.

    This algorithm uses two pointers starting at node_one and node_two. Both pointers move up the tree
    via parent pointers. When a pointer reaches the root (parent is None), it switches to the other
    starting node. By switching starting points, both pointers travel the same total distance and meet
    at the lowest common ancestor.

    Time Complexity: O(h) where h is the height of the tree
    Space Complexity: O(1) as only two pointers are used

    :param node_one: BinaryTreeNode
    :param node_two: BinaryTreeNode
    :return: BinaryTreeNode | None - The lowest common ancestor, or None if not found
    """
    ptr1, ptr2 = node_one, node_two

    while ptr1 != ptr2:
        ptr1 = ptr1.parent if ptr1.parent else node_two
        ptr2 = ptr2.parent if ptr2.parent else node_one

    return ptr1


def connect_all_siblings(root: Optional[BinaryTreeNode]) -> Optional[BinaryTreeNode]:
    """
    Connects all siblings of a binary tree given the root, such that, the right most node is connected to the first node
    on the next level using a 'next' pointer forming a kind of linked list data structure. The right most node on the
    last level is set to None. On each level the nodes are pointed to each other via the next pointer
    This assumes that the provided root is part of a perfect binary tree.

    This uses a level order traversal utilizing a queue to traverse the nodes from the first level to the last level
    adding the nodes to a list for further traversal. The levels list is then traversed connecting nodes to the next
    node in the list via the next pointer. At this point the levels list will have the nodes in the correct order using
    the level order traversal technique.

    After the traversal, the root node will be the first element in the levels list and we simply return that which
    will contain the modified tree with all siblings connected

    This uses Space of O(n) as the levels list is required to handle the final iteration for the connections.
    Time complexity is O(n) as we travers all the nodes in the tree.

    Args:
        root(BinaryTreeNode): root of a perfect binary tree
    Returns:
        BinaryTreeNode root such that the next pointer has been set to point to siblings
    """
    if not root:
        return root

    # Queue will have the root node initially
    queue: Deque[BinaryTreeNode] = deque([root])
    levels: List[BinaryTreeNode] = [root]

    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            levels.append(node.left)
        if node.right:
            queue.append(node.right)
            levels.append(node.right)

    for idx in range(len(levels) - 1):
        levels[idx].next = levels[idx + 1]

    return levels[0]


def connect_all_siblings_ptr(
    root: Optional[BinaryTreeNode],
) -> Optional[BinaryTreeNode]:
    """
    Connects all siblings of a binary tree given the root, such that, the right most node is connected to the first node
    on the next level using a 'next' pointer forming a kind of linked list data structure. The right most node on the
    last level is set to None. On each level the nodes are pointed to each other via the next pointer
    This assumes that the provided root is part of a perfect binary tree.

    This performs a level order traversal using two pointers to traverse the tree utilizing constant space in the process
    making it efficient in terms of space. However, this incurs a time complexity of O(n) as all the nodes in the tree
     have to be traversed from the root to make the connections

    Args:
        root(BinaryTreeNode): root of a perfect binary tree
    Returns:
        BinaryTreeNode root such that the next pointer has been set to point to siblings

    """
    # If the tree is empty, there's nothing to connect
    if root is None:
        return root

    # Initialize two pointers:
    # 'current' points to the current node being processed
    # 'last' keeps track of the last node that was connected
    current = root
    last = root

    # Loop continues until there are no more left children in the current level
    while current.left:
        # Connect the last node's 'next' to the current node's left child
        last.next = current.left
        # Update 'last' to point to this left child
        last = last.next

        # Connect the last node's 'next' to the current node's right child
        last.next = current.right
        # Update 'last' to point to this right child
        last = last.next

        # Move 'current' to the next node at the same level
        current = current.next

    # Return the root of the modified tree
    return root


def mirror_binary_tree(root: Optional[BinaryTreeNode]) -> Optional[BinaryTreeNode]:
    """
    Inverts a binary tree such that the left subtree becomes the right and vice versa.
    Args:
        root(BinaryTreeNode): Root of the binary tree
    Returns:
        BinaryTreeNode: root of the inverted binary tree
    """
    if not root:
        return None

    # Perform a post order traversal of the tree, starting from the left subtree and then the right subtree and then
    # the current node
    if root.left:
        mirror_binary_tree(root.left)

    if root.right:
        mirror_binary_tree(root.right)

    # Swap left and right at the current level
    root.left, root.right = root.right, root.left

    return root
