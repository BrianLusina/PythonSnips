from datastructures.trees.binary_tree_node import BinaryTreeNode


def decode_huffman_tree(root: BinaryTreeNode, s: str) -> str:
    """
    If 0, we move to left, and if 1, we move to the right. 
    If there is no more child, we read the value of the leaf, and add it to the string. 
    We will need to reset the current node to root, so that we can read the next character    
    """
    result = ""
    current = root
    for code in s:
        if int(code) == 0:
            current = current.left
        else:
            current = current.right

        if not current.left and not current.right:
            result += current.data
            current = root

    return result
