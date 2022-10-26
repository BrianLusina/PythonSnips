from typing import List, Optional
from .. import Node


def merge_two_sorted_lists(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.data < l2.data:
        output = l1
        l1 = l1.next
    else:
        output = l2
        l2 = l2.next

    curr = output

    while l1 is not None and l2 is not None:
        if l1.data > l2.data:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next

    if l1 is not None:
        curr.next = l1

    if l2 is not None:
        curr.next = l2

    return output


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
