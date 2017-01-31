from abc import ABCMeta, abstractmethod


class Node(object):
    """
    Node object in the Linked List
    """
    __metaclass__ = ABCMeta

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    @abstractmethod
    def get_next(self):
        """
        Get the next node
        :return:
        """
        pass

    def has_next(self, node):
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

    def get_last(self):
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
        Reverses the linked list, such that the Head points to the last item in the LinkedList and the tail
        points to its predecessor. The first node becomes the tail
        :return: New LinkedList which is reversed
        :rtype: LinkedList object
        """
        pass

    @abstractmethod
    def insert(self, node, pos):
        """
        Insert node at a particular position in the list
        :param node: node to insert
        :param pos: position to insert the node
        :return: inserted node in the list along with the predecessor and successor
        :rtype: Node object
        """
        pass

    def insert_after(self, node_to_insert, current_node):
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
