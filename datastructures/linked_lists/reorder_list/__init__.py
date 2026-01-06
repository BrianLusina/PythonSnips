from typing import Optional
from datastructures.linked_lists.singly_linked_list.node import SingleNode


def reorder_list(head: Optional[SingleNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # First find the middle of the linked list
    # Find the middle of the linked list using the two pointer approach, where we move the first
    # pointer two nodes forward while moving the slow pointer one node forward. When the fast pointer reaches
    # the end of the linked list, the slow pointer will be at the middle node

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # second half of the linked list will be the next node of the slow pointer
    second = slow.next
    # cut the connection between the second half and the first half
    slow.next = None
    # this will keep track of the previous node in the second half of the linked list
    previous = None

    # reversing the second portion of the list
    while second:
        # temporarily store the next node
        temp = second.next
        # set the next pointer to the previous node
        second.next = previous
        # move the previous node forward
        previous = second
        # move the second half head forward
        second = temp

    # The second half of the linked list has been reversed.
    # Now we merge and weave the first half and the second

    # first_half_head will point to the head node of the first half
    first = head
    # Set the second_half_head to previous as previous will now be the head of the second half of the linked list
    second = previous

    while second:
        # save the next pointers of both nodes to not lose track of them
        temp1, temp2 = first.next, second.next

        # Assign the first half head node's next to the second half head node
        # And assign the second half next node to the first half next node
        # This is where the merging and weaving happens

        first.next = second
        second.next = temp1

        # Move the pointers forward for further iterations
        first, second = temp1, temp2
