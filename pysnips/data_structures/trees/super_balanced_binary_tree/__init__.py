from pysnips.data_structures.stacks import Stack


def is_balanced(tree_root):
    """
    Checks if a binary tree is balanced
    :param tree_root: The tree root or a BinaryTreeNode
    :return: True/False, if a binary tree is balanced
    :rtype: bool
    """
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
