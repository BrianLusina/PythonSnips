def bst_checker(root):
    """
    Checks if a node in a binary search tree is valid. By extension, checks if the whole binary search tree is valid
    :param root: the binary search tree node to check
    :return: True/False based on whether the BST is valid
    :rtype: bool
    """

    # start with the root with an arbitrarily low lower bound and an arbitrarily higher bound
    node_bounds_stack = [(root, -float("inf"), float("inf"))]

    # depth first traversal
    while len(node_bounds_stack):
        node, lower_bound, upper_bound = node_bounds_stack.pop()

        # if this node is invalid, return false immediately
        if node < lower_bound or node > upper_bound:
            return False

        if node.left:
            # this node must be less than the current node
            node_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:
            # this node must be greater than the current node
            node_bounds_stack.append((node.right, node.value, upper_bound))

    # if none of the nodes are invalid, return true
    # at this point we have checked all the nodes
    return True


def bst_checker_recursive(root, lower_bound=-float("inf"), upper_bound=float("inf")):
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
        not bst_checker_recursive(root.left, lower_bound, root.value)
        or not bst_checker_recursive(root.right, root.value, upper_bound)
    )
