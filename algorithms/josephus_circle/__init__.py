from datastructures.linked_lists.circular import CircularLinkedList
from datastructures.linked_lists.circular.node import CircularNode


def josephus_circle(circular_list: CircularLinkedList, step: int) -> CircularNode:
    current = circular_list.head

    length = len(circular_list)
    while length > 1:
        count = 1
        while count != step:
            current = current.next
            count += 1
        circular_list.delete_node(current)
        current = current.next
        length -= 1

    return current
