from typing import Optional, Callable, Any
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


def has_cycle(
    head: Optional[Node], func: Optional[Callable[[Node, Node], Any]] = None
) -> bool:
    f"""
    Checks if a given linked list has a cycle if a head node is provided. A cycle is when a linked list node can be
    reached again after traversing the entire linked list
    Args:
        head(Node): head node of a linked list
        func(Callable): An optional callable function that if passed in will be executed
    Returns:
        bool: True if there is a cycle, False otherwise
    """
    if not head or not head.next:
        return False

    fast_pointer, slow_pointer = head, head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer is fast_pointer:
            # do something after detecting cycle passing in the two nodes
            if func:
                func(slow_pointer, fast_pointer)
            return True
    return False


def cycle_length(head: Optional[Node]) -> int:
    """
    Determines the length of the cycle in a linked list if it has one. The length of the cycle is the number
    of nodes that are 'caught' in the cycle
    Args:
        head(Node): head node of linked list
    Returns:
        int: length of the cycle or number of nodes in the cycle
    """
    if not head:
        return 0
    slow_pointer = fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        # Cycle detected
        if slow_pointer is fast_pointer:
            length = 1
            # Move slow-pointer by one step to start counting
            slow_pointer = slow_pointer.next

            # Continue moving the slow pointer until it meets the fast pointer again
            while slow_pointer is not fast_pointer:
                length += 1
                slow_pointer = slow_pointer.next

            return length
    return 0


def detect_node_with_cycle(head: Optional[Node]) -> Optional[Node]:
    """
    Detects a node with a cycle in a Linked List and returns it. The node with a cycle is the entry point of the loop
    Args:
        head(Node): head node of a linked list
    Returns:
        Node: node with a cycle if the linked list has a cycle
    """
    slow_pointer = fast_pointer = head

    while fast_pointer and slow_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

        if slow_pointer == fast_pointer:
            break
    else:
        return None

    current = head
    while current is not slow_pointer:
        slow_pointer = slow_pointer.next
        current = current.next
    return current


def remove_cycle(head: Optional[Node]) -> Optional[Node]:
    """
    Removes cycle from a linked list given the head node
    Args:
        head(Node): head node of a linked list
    Returns:
        Node: head node without the cycle
    """
    # This is the entry point of the cycle
    node_with_cycle = detect_node_with_cycle(head)

    # If there is no node with a cycle, return the head node as is
    if not node_with_cycle:
        return head

    # Now, with the node with the cycle, we set a current pointer that will move a node at a time, until its next pointer
    # points back to the fixed pointer
    current = node_with_cycle
    fixed_pointer = node_with_cycle

    # Move the pointer on this current until the next pointer reaches the fixed pointer
    while current.next is not fixed_pointer:
        current = current.next

    # Remove the cycle by setting the next to None
    current.next = None

    return head


def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    """
    Removes the nth node from a linked list from the head given the head of the linked list and the position from the
    end of the linked list to remove.
    Args:
        head(Node): head node of linkedlist
        n(int): the position of the last node from the tail in the linked list to remove
    Returns:
        Node: head node of modified linked list
    """
    if not head:
        return head

    # Initialize two pointers, both starting at the head node
    fast = slow = head

    # Move the fast pointer until it reaches position n in the linked list
    for _ in range(n):
        fast = fast.next

    # If there is no node at this pointers position, then we have reached the end of the linked list and we return the
    # next node from the head. This means, we are removing the head node
    if not fast:
        return head.next

    # Move the fast pointer, until it reaches the end of the linked list and until the slow pointer reaches n nodes from
    # the end of the linked list
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Set the next pointer of the node at the slow pointer's position to the next node's next pointer, removing the node in the middle
    slow.next = slow.next.next

    # Return the modified head node of the linked list with the node removed
    return head


def sum_of_linked_lists(
    head_one: Optional[Node], head_two: Optional[Node]
) -> Optional[Node]:
    """
    Sums two linked lists together to create a new linked list. The two heads of the two linked lists provided represent
    two non-negative integers. The digits are in reverse order and each of their nodes contains a single digit. This
    adds the two numbers and returns the sum as a linked list. This assumes that the two numbers do not contain any
    leading zero, except the number 0 itself.

    Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

    Complexity:
    Time: O(max(m, n)). Assume that m and n represent the lengths of the first and the second linked lists respectively,
    the algorithm iterates at most max(m, n) times

    Space: O(1). The length of the new linked list is at most max(m, n) + 1

    Args:
        head_one(Node): head node of the first linked list
        head_two(Node): head node of the second linked list
    Returns:
        Node: head node of newly created linked list
    """
    if not head_one and not head_two:
        return None

    dummy_head = Node(0)
    carry = 0
    pointer_one, pointer_two = head_one, head_two
    current = dummy_head

    while pointer_one or pointer_two:
        x = pointer_one.data if pointer_one else 0
        y = pointer_two.data if pointer_two else 0
        current_sum = carry + x + y
        carry = current_sum // 10
        current.next = Node(current_sum % 10)
        current = current.next

        if pointer_one:
            pointer_one = pointer_one.next
        if pointer_two:
            pointer_two = pointer_two.next

        if carry > 0:
            current.next = Node(carry)

    return dummy_head.next
