from .. import Node


def compare_lists(llist1: Node, llist2: Node) -> bool:
    if not llist1 or not llist2:
        return False

    pointer_one = llist1
    pointer_two = llist2

    while pointer_one and pointer_two:
        if pointer_one.data != pointer_two.data:
            return False
        pointer_one = pointer_one.next
        pointer_two = pointer_two.next

    if (pointer_one and not pointer_two) or (pointer_two and not pointer_one):
        return False
    return True
