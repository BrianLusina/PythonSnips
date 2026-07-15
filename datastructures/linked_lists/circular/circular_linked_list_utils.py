from typing import List
from datastructures.linked_lists.circular.node import CircularNode


def split_circular_linked_list(head: CircularNode) -> List[CircularNode]:
    # Initialize two pointers for the traversal: slow and fast
    slow = fast = head

    # Traverse the circular linked list to find the middle point
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # At this point, slow is at the middle of the list
    head1 = head
    head2 = slow.next

    # Split the circular linked list into two halves
    slow.next = head1
    # To complete the second half, traverse to its end
    fast = head2
    while fast.next != head:
        fast = fast.next
    fast.next = head2
    # Return the heads of the two split circular linked lists
    return [head1, head2]
