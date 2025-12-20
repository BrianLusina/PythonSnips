from typing import Optional
from datastructures.linked_lists import Node


def find_middle_node(head: Optional[Node]) -> Optional[Node]:
    """
    Traverse the linked list to find the middle node
    Time Complexity: O(n) where n is the number of nodes in the linked list
    Space Complexity: O(1) as constant extra space is needed
    @return: Middle Node or None
    """
    if not head:
        return None

    fast_pointer, slow_pointer = head, head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer
