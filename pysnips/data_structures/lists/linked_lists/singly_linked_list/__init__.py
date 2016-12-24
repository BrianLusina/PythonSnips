from data_structures.lists.linked_lists import LinkedList, Node


class SingleNode(Node):
    """
    Node implementation in a single linked list
    """
    def __init__(self, value, next):
        super().__init__(next)
        self.value = value
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList(LinkedList):
    """
    Implementation of a SinglyLinked List
    """

    def __init__(self):
        super().__init__()

    def add(self, data):
        """
        Add a node to the Linked List
        :param data:
        :return:
        """
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

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

    def delete_node(self, node):
        temp = node.prev
        node.prev.next = node.next
        node.prev = temp
        return node

    def delete_first(self):
        """
        Since this is a singly linked list, this will have to make the head's next to the position of head
        :return: deleted node
        """
        # store the head node
        to_del = self.head
        # replace the head with the next value in the LinkedList
        self.head = self.head.next
        return to_del

    def insert(self, node, pos):
        pass

    def contains_cycle(self):
        """
        Check if the SinglyLinkedList contains a cycle
        :return:
        """
        fast_runner = self.head
        slow_runner = self.head

        # until we reach the end of the list
        while fast_runner is not None and fast_runner.next is not None:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

            # fast runner is about to lap slow runner
            if fast_runner is slow_runner:
                return True

        # fast runner hit the end of the list
        return False
