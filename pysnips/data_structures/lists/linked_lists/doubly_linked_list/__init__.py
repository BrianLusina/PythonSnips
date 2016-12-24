from data_structures.lists.linked_lists import LinkedList, Node


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list which will implement methods from LinkedList parent class
    Doubly linked lists have nodes which have reference to its predecessor and its successor
    """
    def __init__(self, value):
        super().__init__(value)
        self.prev = None

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
