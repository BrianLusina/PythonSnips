from .. import Node


def sorted_insert(head: Node, new_node: Node):
    current = None

    if head is None or head.value >= new_node.value:
        new_node.next = head
        head = new_node
    else:
        current = head

        while current.next is not None and current.next.data < new_node.value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return head


def insert_sort(head):
    if not head or not head.next:
        return head

    sorted_ll = None
    current = head

    while current:
        next_ = current.next

        sorted_ll = sorted_insert(sorted_ll, current)

        current = next_

    head = sorted_ll

    return head
