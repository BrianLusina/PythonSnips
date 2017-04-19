from data_structures.lists.linked_lists import LinkedList, Node


class SingleNode(Node):
    """
    Node implementation in a single linked list
    """
    def __init__(self, value, next_):
        # noinspection PyCompatibility
        super().__init__(next_)
        self.value = value
        self.next = next_

    def get_next(self):
        return self.next


class SinglyLinkedList(LinkedList):
    """
    Implementation of a SinglyLinked List
    """
    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def push(self, data):
        """
        Add a node to the Linked List
        :param data:
        :return:
        """
        node = SingleNode(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def delete_node(self, node):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.value == node:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

    def shift(self):
        """
        Since this is a singly linked list, this will have to make the head's next to the position of head
        :return: deleted node
        """
        # store the head node
        to_del = self.head
        # replace the head with the next value in the LinkedList
        self.head = self.head.next
        return to_del

    def pop(self):
        pass

    def reverse(self):
        pass

    def unshift(self, node):
        pass

    def insert(self, node, pos):
        pass

    def display(self):
        print("Displaying data...")
        current_node = self.head
        while current_node is not None:
            print(current_node.value, ">>>")
            current_node = current_node.next
        print(None)

    def display_backward(self):
        pass

    def display_forward(self):
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
