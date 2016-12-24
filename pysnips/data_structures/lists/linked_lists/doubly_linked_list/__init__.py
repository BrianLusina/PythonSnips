from data_structures.lists.linked_lists import LinkedList, Node


class DoubleNode(Node):
    """
    Node implementation of DoubleLinkedList
    """

    def __init__(self, value, prev, next):
        super().__init__(value, next)
        self.value = value
        self.prev = prev
        self.next = next

    def get_next(self):
        pass

    def has_prev(self, node):
        """
        Check if the node has a predecessor
        :param node: the node to check for predecessors
        :return: True or False, whether the node has a predecessor
        :rtype: Node object
        """
        pass

        # # if the node has a successor and predecessor, move the successor's prev link to this node's next link
        # if self.has_next(node) and self.has_prev(node):
        #     temp = node.prev
        #     node.prev.next = node.next
        #     node.prev = temp
        #     return node
        # # check if the node has no next, that is it is the last node, move it's prev link to None
        # if not self.has_next(node):
        #     node.prev.next = None
        #     return node
        # # if the node is the head, i.e. has no prev, move this node's next's prev to None
        # if node == self.head:
        #     self.head.next.prev = None
        #     return node


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list which will implement methods from LinkedList parent class
    Doubly linked lists have nodes which have reference to its predecessor and its successor
    """

    def __init__(self):
        super().__init__()

    def add(self, data):
        """
        Add a node to the Linked List
        :param data:
        :return:
        """
        node = DoubleNode(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def delete_node(self, node):
        """
        :param node: The node to delete
        :return: deleted node
        """
        current_node = self.head
        while current_node is not None:
            if current_node.value == node:
                # if it is not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

                current_node = current_node.next

    def delete_last(self):
        pass

    def insert_last(self, node):
        pass

    def reverse(self):
        pass

    def insert_first(self, node):
        pass

    def __repr__(self):
        pass

    def insert(self, node, pos):
        pass

    def delete_first(self):
        """
        Since this is a doubly linked list, this will have to move the head's next link's previous link to None
        :return: deleted node

        """
        # move the head's next previous link to None
        self.head.next.prev = None
        return self.head

    def display(self):
        print("Show list data...")
        current_node = self.head
        while current_node is not None:
            print(current_node.prev.value if hasattr(current_node.prev, "value") else None)
            print(current_node.value)
            print(current_node.next.value if hasattr(current_node.next, "value") else None)
            current_node = current_node.next
        print("*" * 10)

    def display_backward(self):
        pass

    def display_forward(self):
        pass
