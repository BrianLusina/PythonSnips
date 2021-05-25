from typing import Union

from .. import Node


def delete_node(node: Node) -> Union[Node, None]:
    """
    Given we don't have access to the head node, we can not traverse the linked list to move the pointer of the node
    that comes before the node we intend to delete to the node that comes after the node we want to delete.
    Therefore we make this current node(the node we want to delete)'s pointer move to the next node after this node, 
    that is "next.next" & we make the value of this node we intend to delete, the value of the node that comes next

    If the node to be deleted is None, we simply return None.

    If the node is the tail, then we simply return it

    @note
    First, it doesn't work for deleting the last node in the list. We could change the node we're deleting to have a
    value of null, but the second-to-last node's next pointer would still point to a node, even though it should be null
    This could work—we could treat this last, "deleted" node with value null as a "dead node" or a "sentinel node," and
    adjust any node traversing code to stop traversing when it hits such a node. The trade-off there is we couldn't have
     non-dead nodes with values set to null. Instead we chose to throw an exception in this case.

     Complexity Analysis:
        O(1) time and O(1)O(1) space.
    """

    if node is None or node.next is None:
        return node

    node.value = node.next.data
    node.next = node.next.next
    return node
