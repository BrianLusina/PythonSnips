from abc import ABCMeta, abstractmethod


class Node(object):
    """
    Node object in the Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next


class LinkedList(object):
    """
    The most basic LinkedList from which other types of Linked List will be subclassed
    """
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self.value = value
        self.head = None

    @abstractmethod
    def add(self, data):
        """
        Add a node to the linked list
        :param data: the node to add to the list
        """
        pass

    def get_last(self):
        """
        Gets the last node in the Linked List. check each node and test if it has a successor
        if it does, continue checking
        :return: The last Node elemen
        :rtype: Node
        """
        last_node = None
        while not self.has_next(self.value.next):
            last_node = self.value
        return last_node

    def has_next(self, node):
        """
        Checks if the node has a successor
        :param node, the node to check in the linked list
        :return: True or False
        :rtype: bool
        """
        return node.next is None

    def is_empty(self):
        """
        Check if the linked list is empty, essentially if the linked list's head's successor is None
        then the linked list is empty
        :return: True or False
        :rtype: bool
        """
        return self.head is None

    @abstractmethod
    def search(self, node):
        """
        Search through the linked list to find a node
        :param node, the node to search for in the LinkedList
        :return: The sought after node if available, return None, if the node does not exist
         :rtype: LinkedList object or None
        """
        pass

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
    def insert_first(self, node):
        """
        Insert a node at the beginning of the list
        :return: Inserted node, its predecessor and successor
        :rtype: LinkedList object
        """
        pass

    @abstractmethod
    def insert_last(self, node):
        """
        Inserts the node as the first item in the LinkedList
        :param node: the node to insert as the head
        :return: the inserted node element
        :rtype: Node
        """
        pass

    @abstractmethod
    def delete_first(self):
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
    def delete_last(self):
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

    def build_list(self, array):
        self.head.set_data(array[0])
        self.temp = self.head
        for i in array[1:]:
            self.temp = self.temp.set_and_return_next()
            self.temp.set_data(i)
            self.tail = self.temp
        return self.head

    def display(self):
        """
        Displays the whole of the LinkedList
        :return: LinkedList data structure
        """
        temp_node = self.head
        while temp_node != self.tail:
            print(temp_node.get_data())
            temp_node = temp_node.get_next()
        print(self.tail.get_data())

    def display_forward(self):
        """
        Display the complete list in a forward manner
        :return:The LinkedList displayed in 'ascending order' or in order of insertion
        """
        pass

    def display_backward(self):
        """
        Display the complete list in a backward manner
        :return: The LinkedList displayed in 'descending order', not in the order of insertion
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        :return: Human redable string representation of the LinkedList
        """
        tail = self.value if not self.has_next(self.value) else None
        return "head:{}, body, Tail:{}".format(self.head, tail)
