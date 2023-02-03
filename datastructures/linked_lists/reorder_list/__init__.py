from typing import Optional, List
from ..singly_linked_list.node import SingleNode


def reorder_list(head: Optional[SingleNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # first find the middle of the linked list
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # second half of the list
    second = slow.next
    slow.next = None
    previous = None

    # reversing the second portion of the list
    while second:
        temp = second.next
        second.next = previous
        previous = second
        second = temp

    # merge the 2 halves
    first = head
    second = previous

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
