from typing import Optional, Tuple
from datastructures.linked_lists.singly_linked_list.node import SingleNode


def merge_and_weave(
    first_half_head: SingleNode, second_half_head: SingleNode
) -> Optional[SingleNode]:
    """
    Merges and weaves the first half and the second half of a linked list in place.
    Args:
        first_half_head: head node of the first half of the linked list
        second_half_head: head node of the reversed second half of the linked list
    Returns:
        head node of the merged and weaved linked list
    """
    if first_half_head is None or second_half_head is None:
        return None

    p1 = first_half_head
    p2 = second_half_head

    while p2:
        # save the pointer 1 next node to not loose it
        p1_next = p1.next
        p2_next = p2.next

        # now we can move the pointers
        p1.next = p2
        p2.next = p1_next

        p1, p2 = p1_next, p2_next

    return first_half_head


def reverse_list(head: SingleNode) -> Optional[SingleNode]:
    """
    Reverses a linked list given the head node
    Args:
        head Node: the head node of the linked list
    Returns:
        Optional[Node]: the new head node of the reversed linked list
    """
    if head is None or head.next is None:
        return head

    # track previous node, so we can point our next pointer to it
    previous = None
    # track node to loop through
    current_node = head

    while current_node:
        # track the next node to not lose it while adjusting pointers
        nxt = current_node.next

        # set the next pointer to the node behind it, previous
        current_node.next = previous

        # adjust the new previous node to the current node for subsequent loops
        previous = current_node

        # move our node pointer up to the next node in front of it
        current_node = nxt

    # return the new tail of the k-group which is our head
    return previous


def reverse_k_groups(head: SingleNode, k: int) -> Optional[SingleNode]:
    """
    Reverse k groups in a singly linked list given the head node
    Args:
        head(SingleNode): the head node of the linked list
        k(int): groups to reverse
    Returns:
        SingleNode: Head of linked list with k groups reversed
    """
    if k <= 1 or not head:
        return head

    dummy = SingleNode(value=None)
    dummy.next = head
    ptr = dummy

    def reverse_linked_list(
        node: Optional[SingleNode], n: int
    ) -> Tuple[SingleNode, SingleNode]:
        """
        Helper function that reversed linked list within the group of n
        Args:
            node(SingleNode): node of linkedlist
            n(int): number of nodes to reverse
        Returns:
            Tuple: tuple of previous and current node
        """
        prev, curr, nxt = None, node, None
        for _ in range(n):
            # temporarily store the nxt node
            nxt = curr.next
            # reverse the curr node
            curr.next = prev
            # before we move to the nxt node, point prev to the
            # curr node
            prev = curr
            # move to the nxt node
            curr = nxt
        return prev, curr

    while ptr is not None:
        tracker = ptr

        for i in range(k):
            if tracker is None:
                break

            tracker = tracker.next

        if tracker is None:
            break

        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next
