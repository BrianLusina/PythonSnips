from collections import defaultdict

from datastructures.linked_lists import Node


class NodeWithRandomPointer(Node):
    def __init__(self, x: int, next: 'NodeWithRandomPointer' = None, random: 'NodeWithRandomPointer' = None):
        super.__init__(x, next)
        self.random = random


def copyRandomList(self, head: NodeWithRandomPointer) -> NodeWithRandomPointer:
    if not head:
        return None

    copy = defaultdict(lambda: NodeWithRandomPointer(0, None, None))
    copy[None] = None
    node = head

    while node:
        copy[node].val = node.val
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next
    return copy[head]
