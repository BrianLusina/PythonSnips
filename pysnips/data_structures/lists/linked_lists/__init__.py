# coding=utf-8
from abc import ABCMeta, abstractmethod


class Node(object):
    """
    Node object in the Linked List
    """
    __metaclass__ = ABCMeta

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def get_next(self):
        """
        Get the next node
        :return:
        """
        return self.next

    @staticmethod
    def has_next(node):
        """
        Checks if the node has a successor
        :param node, the node to check in the linked list
        :return: True or False
        :rtype: bool
        """
        return node.next is None


class LinkedList(object):
    """
    The most basic LinkedList from which other types of Linked List will be subclassed
    """
    __metaclass__ = ABCMeta
    head = None
    tail = None

    def __init__(self):
        self.head = None

    @abstractmethod
    def push(self, data):
        """
        Add a node to the end of the linked list
        :param data: the node to add to the list
        """
        pass

    def __len__(self):
        """
        Implements the len() for a linked list. This counts the number of nodes in a Linked List
        This uses an iterative method to find the length of the LinkedList
        :return: Number of nodes
        :rtype: int
        """
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

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
                if temp.next == data:
                    count_ += 1
                temp = temp.next
            return count_

    @staticmethod
    def get_last():
        """
        Gets the last node in the Linked List. check each node and test if it has a successor
        if it does, continue checking
        :return: The last Node elemen
        :rtype: Node
        """
        # last_node = None
        # while not self.has_next(self.value.next):
        #     last_node = self.value
        # return last_node
        pass

    def delete_first(self):
        """
        Delete the first node in the linked list
        :return:
        """
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

    def get_position(self, position):
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
        pass

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

    @staticmethod
    def insert_after(node_to_insert, current_node):
        """
        Inserts a node after a node in the Linked List. First find the node in the LinkedList,
        Get its successor, store in temp variable and insert this node in the position,
        get this node's next as the successor of the current node
        :param node_to_insert: The node to be inserted
        :param current_node: the current node to look for to perform insertion
        :return: Node object
        :rtype: Node
        """
        pass

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
    def pop(self):
        """
        Deletes the last node element from the LinkedList
        :return: Deleted node element
        :rtype: Node object
        """

    @abstractmethod
    def delete_node(self, node):
        """
        Finds the node from the linked list and deletes it from the LinkedList
        Moves the node's next to this node's previous link
        Moves this node's previous link to this node's next link
        :param node: Node element to be deleted
        :return: Deleted node
        """
        pass

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
                while(pointer_1.next != pointer_2):
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
            while(pointer_2 != pointer_1):
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next
 
            # Get pointer to the last node
            pointer_2 = pointer_2.next
            while(pointer_2.next != pointer_1):
                pointer_2 = pointer_2.next
 
            # Set the next node of the loop ending node
            # to fix the loop
            pointer_2.next = None
            return True

        return False

    def __str__(self):
        """
        :return: String presentation of LinkedList
        """
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += p.value
                p = p.next
            s += p.value
        return s
