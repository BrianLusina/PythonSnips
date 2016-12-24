from data_structures.lists.linked_lists import LinkedList, Node


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list which will implement methods from LinkedList parent class
    Doubly linked lists have nodes which have reference to its predecessor and its successor
    """

    def delete_node(self, node):
        pass

    def __init__(self, value):
        super().__init__(value)
        self.prev = None

    def reverse(self):
        pass

    def search(self, node):
        pass


    def has_prev(self, node):
        """
        Check if the node has a predecessor
        :param node: the node to check whether it has a predecessor
        :return: True or False
         :rtype: bool
        """
        pass

    def delete(self):
        pass

    def __repr__(self):
        pass

    def has_next(self, node):
        pass


    def delete_last(self):
        """
        Delete the last item in the
        :return:
        """