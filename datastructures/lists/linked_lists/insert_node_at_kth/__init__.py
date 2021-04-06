from .. import Node


def insertNodeAtPosition(head: Node, data: int, position: int) -> Node:
    if head is None:
        # make this the new head
        return Node(data)

    curr = head

    if position == 0:
        node = Node(data)
        node.next = head
        return node

    while curr is not None:
        node = Node(data)

        for _ in range(position - 1):
            curr = curr.next

        node.next = curr.next
        curr.next = node
        return head
