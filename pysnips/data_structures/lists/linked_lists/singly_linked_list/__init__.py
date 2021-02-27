from pysnips.data_structures.lists.linked_lists import LinkedList, Node


class SingleNode(Node):
    """
    Node implementation in a single linked list
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

    def delete_node_at_position(self, position: int) -> Node:
        """
        Deletes a node at the specified position
        """
        if self.head is None:
            return None

        current = self.head

        while current is not None:
            for _ in range(position):
                current = current.next
            
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

    def reverse(self):
        """
        Uses an iterative approach to reverse this linked list.
        If the linked list has only 0 or 1 node, then just return the head.
        If that is not the case, then the iterative approachis best where there are 2 pointers.
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

    def unshift(self, node):
        pass

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
