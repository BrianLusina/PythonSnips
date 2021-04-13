from datastructures.stacks import Stack
from .. import LinkedList, Node


class SingleNode(Node):
    """
    SingleNode implementation in a single linked list
    """

    def __init__(self, value, next_):
        # noinspection PyCompatibility
        super().__init__(next_)
        self.value = value
        self.next = next_


class SinglyLinkedList(LinkedList):
    """
    Implementation of a SinglyLinked List
    """

    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def push(self, data):
        """
        Add a node to the Linked List
        :param data:
        :return:
        """
        node = SingleNode(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def get_nth_node(self, position: int) -> SingleNode:
        """
        Gets nth node in a linked list given the head of the linked list
        :raises: ValueError for position less than 0 or position is greater than length of linked list
        :rtype: SingleNode
        :returns: None when the head is None & SingleNode
        """
        if position < 0:
            raise ValueError("Position less than 0")

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError("Null node encountered")

            return current

    def delete_node_at_position(self, position: int) -> SingleNode:
        """
        Deletes a node at the specified position
        """
        if position < 0:
            raise ValueError("Position less than 0")

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError("Invalid position found, reached end of list")

            current.value = current.next.value
            current.next = current.next.next
            return self.head

    def delete_node(self, node):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.value == node:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

    def shift(self):
        """
        Since this is a singly linked list, this will have to make the head's next to the position of head
        :return: deleted node
        """
        # store the head node
        to_del = self.head
        # replace the head with the next value in the LinkedList
        self.head = self.head.next
        return to_del

    def pop(self):
        pass

    def reverse(self) -> SingleNode:
        """
        Uses an iterative approach to reverse this linked list.
        If the linked list has only 0 or 1 node, then just return the head.
        If that is not the case, then the iterative approach is best where there are 2 pointers.
        1. reversed_list: A pointer to already reversed linked list. initialized to head
        2. list_to_reverse: pointer to the remaining list. intialized to head->next

        we then set the reversed_list->next to None, this then becomes the last node. reversed_list will
        always point to the head of the newly reversed linked list

        At each iteration, the list_to_do pointer moves forward (until it reaches NULL). 
        The current node becomes the head of the new reversed linked list and starts pointing to the previous head of the reversed linked list.
        The loop terminates when list_to_do becomes NULL, and the reversed_list pointer is pointing to the new head at the termination of the loop.
        """
        if self.head == None or self.head.next == None:
            return self.head

        list_to_reverse = self.head.next

        reversed_list = self.head
        reversed_list.next = None

        while list_to_reverse != None:
            temp = list_to_reverse

            # move the pointer to the next node
            list_to_reverse = list_to_reverse.next

            # point the list_to_reverse to the reversed linked list. Making the reversed_list the next node
            temp.next = reversed_list
            reversed_list = temp

        return reversed_list

    def reverse_between(self, left: int, right: int):
        """
        Reverse linked list between left & right node positions.
        This uses the iterative link reversal to reverse a sublist of the linked list between the left & the right 
        positions in the linked list.
        This is based on the assumption that we don't have access to the data in the nodes themselves, 
        but instead we can change the links between the nodes.

        Starting from the node at position left all the way to position right, we reverse the next pointers for 
        all the nodes in between.

        Ref: https://leetcode.com/problems/reverse-linked-list-ii/solution/
        
        Time Complexity: O(N) considering the list consists of N nodes. 
        We process each of the nodes at most once (we don't process the nodes after the right node from the beginning.
        
        Space Complexity: O(1) since we simply adjust some pointers in the original linked list and only use O(1) additional 
        memory for achieving the final result.
        """
        if self.head is None or self.head.next is None:
            return self.head

        # Move the 2 pointers until they reach the proper starting point in the list
        current_pointer, previous_pointer = self.head, None

        while left > 1:
            previous_pointer = current_pointer
            current_pointer = current_pointer.next
            left, right = left - 1, right - 1

        # The 2 pointers that will fix the final connections
        tail_pointer, conn_pointer = current_pointer, previous_pointer

        # iteratively reverse the nodes until right becomes 0
        while right:
            third_pointer = current_pointer.next
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer
            current_pointer = third_pointer
            right -= 1

        # Adjust the final connections
        if conn_pointer:
            conn_pointer.next = previous_pointer
        else:
            self.head = previous_pointer

        tail_pointer.next = current_pointer
        return self.head

    def unshift(self, node: SingleNode) -> SingleNode:
        if self.head:
            return node
        node.next = self.head
        return node

    def insert(self, node, pos):
        counter = 1
        current = self.head

        if pos > 1:
            while current and counter < pos:
                if counter == pos - 1:
                    node.next = current.next
                    current.next = node
                current = current.next
                counter += 1
        elif pos == 1:
            node.next = self.head
            self.head = node

    def display(self):
        print("Displaying data...")
        current_node = self.head
        while current_node is not None:
            print(current_node.value, ">>>")
            current_node = current_node.next
        print(None)

    def display_backward(self):
        pass

    def display_forward(self):
        pass

    def contains_cycle(self):
        """
        Check if the SinglyLinkedList contains a cycle
        :return:
        """
        fast_runner = self.head
        slow_runner = self.head

        # until we reach the end of the list
        while fast_runner is not None and fast_runner.next is not None:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

            # fast runner is about to lap slow runner
            if fast_runner is slow_runner:
                return True

        # fast runner hit the end of the list
        return False

    def remove_duplicates(self):
        """
        Removes duplicates from linked list
        """

        if self.head is None or self.head.next is None:
            return self.head

        current = self.head
        next_ = self.head.next

        while current and next_:
            if next_.value == current.value:
                current.next = next_.next
                next_ = next_.next
            else:
                current = current.next
                next_ = next_.next

        return self.head

    def append(self, node: SingleNode) -> SingleNode:
        """
        Appends another linked list to this linked list & returns the head of the newly formed linked list
        if both linked lists are None, return None, if 1 of the linked lists is None, return the one that is
        not None.

        We have to traverse the linked list to get to the tail and assign the tail node's next node from None to 
        the linked list we intend to append.

        Complexities:
        Space Complexity = O(1) as no new variables are used in memory, this operation is done in place
        Time Complexity = O(n) as we are traversing only 1 linked list

        :param: node Head node of linked list to append
        :type: SingleNode
        :rtype: SingleNode
        """
        if node is None:
            return self.head
        if self.head is None:
            return node

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node
        return self.head

    def alternate_split(self) -> tuple:
        if not self.head or not self.head.next:
            raise ValueError("Head should not be none")

        current = self.head

        # head for the first linked list
        first = current

        # head for the second linked list
        second = current.next

        while current and current.next:
            temp = current.next

            # set the next node for the first linked list
            current.next = temp.next

            # check if the next node is available for the second linked list
            if current.next and current.next.next:
                # set the next node for the second linked list
                temp.next = current.next.next
            else:
                # we are at the end
                temp.next = None

            # keep moving the pointer
            current = current.next

        return first, second

    def is_palindrome(self) -> bool:
        """
        Checks to see if a Linked list is a Palindrome.
        Returns True if it is, false otherwise.
        Uses a stack, where we add the values/data of each node into a stack
        & reset the pointer back to the head. We then traverse the linked list from the head
        as we pop the data items from the stack(this will be the last added data item of the tail node) 
        & check each node's value to the data item popped from the stack. If any differ, then it is not
        a Palindrome
        :returns: True
        """

        if not self.head:
            return False

        # A LinkedList with 1 Node is a Palindrome
        if not self.head.next:
            return True

        current = self.head
        stack = Stack()

        while current:
            stack.push(current.data)
            current = current.next

        current = self.head

        while current:
            data = stack.pop()
            if current.value != data:
                return False
            current = current.next

        return True

    def pairwise_swap(self) -> SingleNode:
        # nothing to do here
        if not self.head:
            return self.head

        current = self.head

        # loop as long as there are at least 2 nodes left
        while current and current.next:

            # if both nodes have the same value/data
            if current.value == current.next.value:
                # no need to swap, move on to the next pair
                current = current.next.next
            else:
                # swap data of node with the next node's data
                current.value, current.next.value = current.next.value, current.value

                # move on to the next pair
                current = current.next.next

        # at this point, the linked list has been swapped in pairs
        return self.head

    def swap_nodes(self, k: int) -> Node:
        a, b = self.head, self.head

        for _ in range(1, k):
            a = a.next

        node, a = a, a.next

        while a:
            a, b = a.next, b.next

        node.value, b.value = b.value, node.value

        return self.head
