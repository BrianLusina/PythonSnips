from typing import List, Optional
from .. import Node


def merge_two_sorted_lists(
    head_one: Optional[Node], head_two: Optional[Node]
) -> Optional[Node]:
    """
    Merges two sorted linked list into 1 sorted linked list. Note that the assumption here is that the 2 linked lists
    are already sorted. If either of the heads of the linked list that is provided is None, the other head node is
    returned instead. If both are None, then none is returned.

    Complexity:
    Time O(n+m) where n is the number of nodes in 1 linked list while m is the number of nodes in the other linked list.
    This is because both linked lists have to be traversed to merge into a single linked list

    Space O(n+m) where n & m are the number of nodes in the respective linked list. This is because a new linked list
    is created from both linked lists and the nodes from each are merged into a single linke list.

    Args:
        head_one(Node): optional head node of linked list one
        head_two(Node): optional head node of linked list two
    Returns:
        Node: optional head node of merged linked list
    """
    if not head_one and not head_two:
        return None
    if head_one is None:
        return head_two
    if head_two is None:
        return head_one

    if head_one.data < head_two.data:
        merged_list = head_one
        head_one = head_one.next
    else:
        merged_list = head_two
        head_two = head_two.next

    current = merged_list

    while head_one is not None and head_two is not None:
        if head_one.data > head_two.data:
            current.next = head_two
            head_two = head_two.next
        else:
            current.next = head_one
            head_one = head_one.next
        current = current.next

    if head_one is not None:
        current.next = head_one

    if head_two is not None:
        current.next = head_two

    return merged_list


def merge_k_lists(lists: List[Node]) -> Optional[Node]:
    length = len(lists)

    if length == 0:
        return None

    if length == 1:
        return lists[0]

    interval = 1

    while interval < length:
        i = 0

        while i + interval < length:
            lists[i] = merge_two_sorted_lists(lists[i], lists[i + interval])
            i = i + interval * 2
        interval *= 2

    return lists[0]
