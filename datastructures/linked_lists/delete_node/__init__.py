from .. import Node


def delete_node(node: Node) -> Node:
    """
    Given we don't have access to the head node, we can not traverse the linked list to move the pointer of the node
    that comes before the node we intend to delete to the node that comes after the node we want to delete.
    Therefore we make this current node(the node we want to delete)'s pointer move to the next node after this node, 
    that is "next.next" & we make the value of this node we intend to delete, the value of the node that comes next

    If the node to be deleted is None, we simply return None.

    If the node is the tail, then we simply return it
    """

    if node is None or node.next is None:
        return node

    node.value = node.next.data
    node.next = node.next.next
    return node
