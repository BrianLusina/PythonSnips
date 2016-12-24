class Node(object):
    def __init__(self):
        self.data = None
        self.next_node = None

    def set_and_return_Next(self):
        self.next_node = Node()
        return self.next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def delete(self, node):
        """
        Deletes a node from the linked list
        :param node
        :return: the deleted node
        """
    def has_next(self, node):
        """
        Checks if the node has a successor
        :param node, the node to check in the linked list
        :return: True or False
        :rtype: bool
        """

    def has_prev(self, node):
        """
        Check if the node has a predecessor
        :param node: the node to check whether it has a predecessor
        :return: True or False
         :rtype: bool
        """

    def is_empty(self):
        """
        Check if the linked list is empty, essentially if the linked list's head's successor is None
        then the linked list is empty
        :return: True or False
        :rtype: bool
        """
        return self.head is None

    def search(self, node):
        """
        Search through the linked list to find a node
        :param node, the node to search for in the LinkedList
        :return: The sought after node if available, return None, if the node does not exist
         :rtype: LinkedList object or None
        """

    def reverse(self):
        """
        Reverses the linked list, such that the Head points to the last item in the LinkedList and the tail
        points to its predecessor. The first node becomes the tail
        :return: New LinkedList which is reversed
        :rtype: LinkedList object
        """

    def insert(self, node, pos):
        """
        Insert a node at a particular position in the Linked list
        :return: Inserted node, its predecessor and sucessor
        :rtype: LinkedList object
        """

    def __repr__(self):
        """
        :return: Human redable string representation of the LinkedList
        """
        tail = self.value if not self.has_next(self.value) else None
        return "head:{}, body, Tail:{}".format(self.head, tail)

    def build_list(self, array):
        self.head = Node()
        self.head.set_data(array[0])
        self.temp = self.head
        for i in array[1:]:
            self.temp = self.temp.set_and_return_Next()
            self.temp.set_data(i)
            self.tail = self.temp
        return self.head

    def print_list(self):
        temp_node = self.head
        while temp_node != self.tail:
            print(temp_node.get_data())
            temp_node = temp_node.get_next()
        print(self.tail.get_data())
