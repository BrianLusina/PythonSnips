from data_structures.lists.linked_lists import LinkedList, Node


class CircularNode(Node):
    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def get_next(self):
        pass


class CircularLinkedList(LinkedList):
    """
    Implementation of a CircularLinked List
    The last pointer in the list points to the head of the list
    """

    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def delete_node(self, node):
        pass

    def insert(self, node, pos):
        pass

    def display(self):
        pass

    def shift(self):
        pass

    def pop(self):
        pass

    def unshift(self, node):
        pass

    def display_backward(self):
        pass

    def reverse(self):
        pass

    def insert_last(self, node):
        pass

    def display_forward(self):
        pass

    def push(self, data):
        pass
