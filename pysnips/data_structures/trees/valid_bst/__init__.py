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
