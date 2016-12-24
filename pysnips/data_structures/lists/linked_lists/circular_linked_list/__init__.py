from data_structures.lists.linked_lists import LinkedList


class CircularLinkedList(LinkedList):
    """
    Implementation of a CircularLinked List
    The last pointer in the list points to the head of the list
    """
    def __init__(self, value):
        """
        Creates a CircularLinked List object
        :param value:
        """
        super().__init__(value)

    def delete_last(self):
        pass

    def insert_last(self, node):
        pass

    def reverse(self):
        pass

    def insert_first(self, node):
        pass

    def search(self, node):
        pass

    def __repr__(self):
        pass

    def delete_first(self):
        pass

    def insert(self, node, pos):
        pass

    def has_next(self, node):
        pass

    def delete_node(self, node):
        pass
