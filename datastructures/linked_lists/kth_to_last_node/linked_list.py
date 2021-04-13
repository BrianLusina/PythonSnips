from datastructures.linked_lists import LinkedListNode

a = LinkedListNode("angel food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError("Impossible to find less than first to last node %s" % k)

    left_node = head
    right_node = head

    for _ in range(k - 1):
        """
        Along the way, if a right node does not have a next, then k is greater than the length of the list
        thus, there can't be kth to the last node, we raise an error
        """
        if not right_node.next:
            raise ValueError("K is larger than the length of the linked list %s" % k)

        right_node = right_node.next

    """
    Starting with thte lect node on the head, move left node and right node down the list
    maintaining a distance of k between them until right node hits the end of the list
    """
    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

    """
    Since left node is k nodes behind right node
    left node is now the kth to last node
    """
    return left_node


print(kth_to_last_node(2, a))
