# coding=utf-8
from abc import ABCMeta, abstractmethod
from typing import Union, Any


class Node(object):
    """
    Node object in the Linked List
    """
    __metaclass__ = ABCMeta

    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return f"Node({self.data})"

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList(object):
    """
    The most basic LinkedList from which other types of Linked List will be subclassed
    """
    __metaclass__ = ABCMeta
    head = None

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Not Yet implemented")

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError("Not Yet implemented")

    def __len__(self):
        """
        Implements the len() for a linked list. This counts the number of nodes in a Linked List
        This uses an iterative method to find the length of the LinkedList
        :return: Number of nodes
        :rtype: int
        """
        return len(tuple(iter(self)))

    @abstractmethod
    def append(self, data):
        """
        Add a node to the end of the linked list
        :param data: the node to add to the list
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def prepend(self, data):
        """
        Add a node to the beginning of the linked list
        :param data: the node to add to the list
        """
        raise NotImplementedError("Not yet implemented")

    def search(self, node):
        """
        Search method to search for a node in the LinkedList
        :param node: the node being sought
        :return: the node being sought
        """
        head = self.head
        if head is not None:
            while head.next is not None:
                if head.data == node:
                    return head
                head = head.next
            if head.data == node:
                return head
        return None

    def count(self, data):
        """
        Counts the number of occurrences of a data in a LinkedList
        :param data: Data to count
        :return:
        """
        if self.head is None:
            return 0
        else:
            count_ = 0
            temp = self.head
            while temp:
                if temp.data == data:
                    count_ += 1
                temp = temp.next
            return count_

    def get_last(self):
        """
        Gets the last node in the Linked List. check each node and test if it has a successor
        if it does, continue checking
        :return: The last Node element
        :rtype: Node
        """
        if not self.head or not self.head.next:
            return self.head

        node = self.head
        while node.next:
            node = node.next

        return node

    def get_position(self, position: int) -> Union[Node, None]:
        """
        Returns the current node in the linked list if the current position of the node is equal to the position. Assume
        counting starts from 1
        :param position: Used to get the node at the given position
        :type position int
        :raises ValueError
        :return: Node
        :rtype: Node
        """
        if position < 0 or not isinstance(position, int):
            raise ValueError("Position should be a positive integer")
        counter = 1
        current = self.head

        if position == 0 and current is not None:
            return current
        if position < 1 and current is None:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def is_empty(self):
        """
        Check if the linked list is empty, essentially if the linked list's head's successor is None
        then the linked list is empty
        :return: True or False
        :rtype: bool
        """
        return self.head is None

    @abstractmethod
    def reverse(self):
        """
        Reverses the linked list, such that the Head points to the last item in the
        LinkedList and the tail points to its predecessor. The first node becomes the tail
        :return: New LinkedList which is reversed
        :rtype: LinkedList
        """
        raise NotImplementedError("Not Yet Implemented")

    @abstractmethod
    def insert(self, node, pos):
        """
        Insert node at a particular position in the list
        :param node: node to insert
        :param pos: position to insert the node
        :type pos int
        :return: inserted node in the list along with the predecessor and successor
        :rtype: Node
        """
        raise NotImplementedError()

    @abstractmethod
    def insert_after_node(self, prev_node: Node, data: Any):
        """
        Inserts a node after a node in the Linked List. First find the node in the LinkedList,
        Get its successor, store in temp variable and insert this node in the position,
        get this node's next as the successor of the current node
        :param prev_node: The node to find
        :param data: the data for the node to insert
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def unshift(self, node):
        """
        Insert a node at the beginning of the list
        :return: Inserted node, its predecessor and successor
        :rtype: LinkedList object
        """
        pass

    @abstractmethod
    def shift(self):
        """
        Deletes a node from the beginning of the linked list, sets the new head to the successor of the deleted
        head node
        :return: the deleted node
        :rtype: Node
        """
        # check if the LinkedList is empty, return None
        if self.is_empty():
            return None

    @abstractmethod
    def pop(self) -> Union[Node, None]:
        """
        Deletes the last node element from the LinkedList
        :return: Deleted node element
        :rtype: Node object
        """
        raise NotImplementedError("Not yet implemented")

    def delete_head(self) -> Union[Node, None]:
        """
        Delete the first node in the linked list
        """
        if self.head:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node
        else:
            return None

    @abstractmethod
    def delete_node(self, node: Node):
        """
        Finds the node from the linked list and deletes it from the LinkedList
        Moves the node's next to this node's previous link
        Moves this node's previous link to this node's next link
        :param node: Node element to be deleted
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete_node_at_position(self, position: int):
        """
        Deletes a node from the given provided position
        :param position: Position of node to delete
        """
        if not 0 <= position <= len(self) - 1:
            raise ValueError("Position out of bounds")

        if self.head is None:
            return None

        # rest of the implementation is at the relevant subclasses

    @abstractmethod
    def delete_node_by_data(self, data: Any):
        """
        traverses the LinkedList until we find the data in a Node that matches and deletes that node. This uses the same
        approach as self.delete_node(node: Node) but instead of using the node to traverse the linked list, we use the
        data attribute of a node. Note that if there are duplicate Nodes in the LinkedList with the same data attributes
        only, the first Node is deleted.
        :param data: Data of Node element to be deleted
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def display(self):
        """
        Displays the whole of the LinkedList
        :return: LinkedList data structure
        """
        pass

    @abstractmethod
    def display_forward(self):
        """
        Display the complete list in a forward manner
        :return:The LinkedList displayed in 'ascending order' or in order of insertion
        """
        pass

    @abstractmethod
    def display_backward(self):
        """
        Display the complete list in a backward manner
        :return: The LinkedList displayed in 'descending order', not in the order of insertion
        """
        pass

    def has_cycle(self):
        """
        Detects if linked list has cycle, i.e. a node in the linked list points to a node already traversed.
        Will use Floyd-Cycle Detection algorithm to check for cycles. Will have a fast and slow pointer and check if the fast pointer
        catches up to the slow pointer. If this happens, there is a cycle. The fast pointer will move at twice the speed of slow pointer
        :return: True if there is a cycle, False otherwise
        :rtype: bool
        """
        fast_pointer = slow_pointer = self.head
        while fast_pointer and slow_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                return True
        return False

    def detect_node_with_cycle(self):
        """
        Detects the node with a cycle and returns it
        """
        if not self.has_cycle():
            return False
        else:
            slow_pointer = fast_pointer = self.head

            while fast_pointer and slow_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next

                if slow_pointer == fast_pointer:
                    break
            else:
                return None

            while self.head != slow_pointer:
                slow_pointer = slow_pointer.next
                self.head = self.head.next
            return self.head

    def remove_cycle(self):
        """
        Removes cycle if there exists. This will use the same concept as has_cycle method to check if there is a loop and remove the cycle
        if one is found.
        1) Detect Loop using Floyd’s Cycle detection algo and get the pointer to a loop node.
        2) Count the number of nodes in loop. Let the count be k.
        3) Fix one pointer to the head and another to kth node from head.
        4) Move both pointers at the same pace, they will meet at loop starting node.
        5) Get pointer to the last node of loop and make next of it as NULL.
        :return: True if the cycle has been removed, False otherwise
        :rtype: bool
        """
        fast_pointer = slow_pointer = self.head

        while fast_pointer and slow_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                pointer_1 = pointer_2 = slow_pointer

                # Count the number of nodes in loop
                k = 1
                while (pointer_1.next != pointer_2):
                    pointer_1 = pointer_1.next
                    k += 1

            # Fix one pointer to head
            pointer_1 = self.head

            # And the other pointer to k nodes after head
            pointer_2 = self.head
            for _ in range(k):
                pointer_2 = pointer_2.next

            # Move both pointers at the same place
            # they will meet at loop starting node
            while (pointer_2 != pointer_1):
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next

            # Get pointer to the last node
            pointer_2 = pointer_2.next
            while (pointer_2.next != pointer_1):
                pointer_2 = pointer_2.next

            # Set the next node of the loop ending node
            # to fix the loop
            pointer_2.next = None
            return True

        return False

    @abstractmethod
    def alternate_split(self):
        """
        Alternate split a linked list such that a linked list such as a->b->c->d->e becomes a->c->e->None and b->d->None
        """
        pass

    @abstractmethod
    def is_palindrome(self) -> bool:
        """
        Checks if the linked list is a Palndrome. That is, can be read from both back & front
        :return: boolean data. True if the LinkedList is a Palindrome
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def pairwise_swap(self) -> Node:
        """
        Swaps nodes in a linked list in pairs.
        As there are different kinds of LinkedLists, it is up to the child class to implement this

        The premise(idea) is to swap the data of each node with the data of the next node. This is while using
        an iterative approach
        Example:
        1 -> 2 -> 3 -> 4
        becomes
        2 -> 1 -> 4 -> 3
        :return: New head of node
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def swap_nodes_at_kth_and_k_plus_1(self, k: int) -> Node:
        """
        Return the head of the linked list after swapping the datas of the kth node from the beginning and the kth node
        from the end (the list is 1-indexed).

        Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
        Output: [7,9,6,6,8,7,3,0,9,5]
        """
        raise NotImplementedError("Method has not been implemented")
