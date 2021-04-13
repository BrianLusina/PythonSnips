from datastructures.linked_lists import LinkedList, Node


class DoubleNode(Node):
    """
    Node implementation of DoubleLinkedList
    """

    def __init__(self, value, prev_node=None, next_node=None):
        # noinspection PyCompatibility
        super().__init__(value, next_node)
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_next(self):
        """
        Gets the next node
        :return: the next node
        """
        return self.next_node

    def get_previous(self):
        """
        gets the previous node
        :return: previous node 
        """
        return self.prev_node


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list which will implement methods from LinkedList parent class
    Doubly linked lists have nodes which have reference to its predecessor and its successor
    """

    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def push(self, data):
        """
        Add a node to the end of Linked List
        :param data: Data to add
        :return:
        """
        node = DoubleNode(data, prev_node=self.tail)
        if self.tail:
            self.tail.next_node = node

        # if the head does not exist, set the head to the node
        if not self.head:
            self.head = node
        self.tail = node

    def pop(self):
        """
        Removes the last item from the list and returns it
        :return: Node at the last position
        """
        last_node = self.tail.value
        self.tail = self.tail.prev_node
        return last_node

    def shift(self):
        """
        Removes value at the front of the doubly linked list
        :return: deleted node
        """
        value = self.head.value
        self.head = self.head.next_node
        return value

    def unshift(self, value):
        """
        Inserts a value at the front of the doubly linked list
        :param value: data to add at the front of the list
        """
        node = DoubleNode(value, next_node=self.head)
        if self.head:
            self.head.prev_node = node
        if not self.tail:
            self.tail = node
        self.head = node

    def get_nth_node(self, position: int) -> Node:
        """
        Gets nth node in a linked list given the head of the linked list
        :raises: ValueError for position less than 0 or position is greater than length of linked list
        :rtype: Node
        :returns: None when the head is None & Node
        """
        if position < 0:
            raise ValueError("Position less than 0")

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError("Null node encountered")

            return current

    def delete_node_at_position(self, position: int) -> DoubleNode:
        """
        Deletes a node at the specified position
        """
        if position < 0:
            raise ValueError("Position less than 0 not allowed")

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError("Invalid position found, reached end of list")

            current.value = current.next.value
            current.next = current.next.next
            current.next.prev_node = current.prev_node
            return self.head

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
                    # otherwise we have no prev (it's None), head is the next one, and prev
                    #  becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

                current_node = current_node.next

    def reverse(self) -> DoubleNode:
        """
        Order of operations is important here. We set the current.next to next before
        setting previous to current.next
        We return previous because when we exit, current is None, which means that the last
        node we visited—previous—was the tail of the original list, and thus the head of
        our reversed list.
        
        Complexity:
        O(n) time and O(1) space. We pass over the list only once, and maintain a
        constant number of variables in memory.
        
        :return: a reversed LinkedList
        :rtype: DoublyLinkedList
        """

        if self.head is None:
            return None

        # nothing to reverse here
        if self.head.next_node is None:
            return self.head

        current = self.head
        previous = None
        next_ = None

        # do this, until we are at the end of the linked list
        while current:
            # copy a pointer to the next element, before we overwrite the current
            next_ = current.next_node

            # reverse the next pointer & previous pointer
            current.next_node = previous
            current.prev_node = next_

            # step forward in the list
            previous = current
            current = next_

        return previous

    def insertSorted(self, node: DoubleNode, data: int):
        """
        Inserts a node with data value into a sorted DoublyLinked List. The assumption here is that 
        the double linked list node is already sorted
        """
        # if there is no node, make this node the new head of the list
        if node is None:
            return DoubleNode(data)

        # if there is no next node, no need to traverse the doubly linked list, simply create a new
        # DoubleNode and insert it at the tail
        if node.next is None:
            new_tail = DoubleNode(data, prev_node=node)
            node.next = new_tail
            return node

        # if at the node the data value is already less than the data we intend to insert we make 
        # this node the head of the doubly linked list
        if node.value > data:
            new_head = DoubleNode(data, next_node=node)
            node.prev_node = new_head
            return new_head

        current = node

        while current:
            next_node = current.next

            # we are at the end of the doubly linked list, so we create a new DoubleNode and make it the tail
            if next_node is None:
                new_node = DoubleNode(data, prev_node=current)
                current.next_node = new_node
                return node

            # we create a new node and insert it into 2 nodes iff it is less than the next node value and 
            # less than the previous node value
            if current.value <= data and next_node.data >= data:
                new_node = DoubleNode(data, prev_node=current, next_node=next_node)
                next_node.prev_node = new_node
                current.next_node = new_node
                return node

            # move pointer to next node
            current = next_node

    def insert(self, node: DoubleNode, position: int):
        """
        Inserts a node at the specified position in the doubly linked list
        """
        if node is None:
            return node

        curr = node

        if position == 0:
            node.next = self.head
            return node

        while curr is not None:

            for _ in range(position - 1):
                curr = curr.next

            node.next = curr.next
            curr.next = node
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

    def append(self, node: DoubleNode) -> DoubleNode:
        """
        Appends another linked list to this linked list & returns the head of the newly formed linked list
        if both linked lists are None, return None, if 1 of the linked lists is None, return the one that is
        not None.

        We have to traverse the linked list to get to the tail and assign the tail node's next node from None to 
        the linked list we intend to append.

        Complexities:
        Space Complexity = O(1) as no new variables are used in memory, this operation is done in place
        Time Complexity = O(n) as we are traversing only 1 linked list

        :param: node Head node of linked list to append
        :type: Node
        :rtype: Node
        """
        if node is None:
            return self.head
        if self.head is None:
            return node

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node
        node.prev_node = current
        return self.head

    def remove_duplicates(self):
        """
        Removes duplicates from linked list
        """

        if self.head is None or self.head.next_node is None:
            return self.head

        current = self.head
        next_ = current.next_node

        while next_:
            if next_.value == current.value:
                current.next_node = current.next_node.next_node
                current = current.next_node.prev_node
                next_ = current.next_node
            else:
                current = next_
                next_ = current.next_node

        return self.head

    def stringify(self, node: DoubleNode):
        """
        :return: String presentation of DoubleLinkedList from the node
        """
        return "None" if node is None else f"{str(node.value)} <-> {self.stringify(node.next_node)}"

    def alternate_split(self) -> tuple:
        if not self.head or not self.head.next:
            raise ValueError("Head should not be none")

        current = self.head

        # head for the first linked list
        first = current

        # head for the second linked list
        second = current.next_node

        while current and current.next_node:
            temp = current.next_node

            # set the next node for the first linked list
            current.next_node = temp.next_node
            temp.next_node.prev_node = current

            # check if the next node is available for the second linked list
            if current.next_node and current.next_node.next_node:
                # set the next node for the second linked list
                temp.next_node = current.next_node.next_node
                current.next_node.next_node.prev_node = temp
            else:
                # we are at the end
                temp.next_node = None

            # keep moving the pointer
            current = current.next_node

        return first, second
