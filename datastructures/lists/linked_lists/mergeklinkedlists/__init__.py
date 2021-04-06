from .. import Node


def mergeTwoSortedLists(l1: Node, l2: Node) -> Node:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    output = None

    if l1.val < l2.val:
        output = l1
        l1 = l1.next
    else:
        output = l2
        l2 = l2.next

    curr = output

    while l1 is not None and l2 is not None:
        if l1.val > l2.val:
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


def mergeKLists(lists: List[Node]) -> Node:
    length = len(lists)

    if length == 0:
        return None

    if length == 1:
        return lists[0]

    interval = 1

    while interval < length:
        i = 0

        while i + interval < length:
            lists[i] = mergeTwoSortedLists(lists[i], lists[i + interval])
            i = i + interval * 2
        interval *= 2

    return lists[0]
