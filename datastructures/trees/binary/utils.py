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
