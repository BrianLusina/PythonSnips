from typing import Optional, Any, Union, Tuple, Self

from datastructures.linked_lists import LinkedList, Node, T
from .node import CircularNode


class CircularLinkedList(LinkedList):
    def __init__(self, head: Optional[CircularNode] = None):
        super().__init__(head)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            # break out of the loop when the next node is back at the head node to avoid a continuous loop
            if current.next == self.head:
                break
            current = current.next

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def append(self, data: T):
        """
        Adds a new node to the end of this linked list. To maintain circular pointers where the last node points back
        to the head node, the pointer keeping track of the nodes as it traverses through the list checks to see if the
        next pointer equals the head node. If it is, the pointer exists the loop, otherwise this becomes an infinite
        loop. Once the pointer is at the end, the last node's next pointer is set to the new node and the new node's
        next pointer is set to the head node.
        If there is not head node, then the new node becomes the head node and it's next pointer points to itself.
        Args:
            data T: data to insert in the linked list
        """
        new_node = CircularNode(value=data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data: T):
        new_node = CircularNode(value=data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def reverse(self):
        pass

    def insert(self, node, pos):
        pass

    def insert_after_node(self, prev_key: Any, data: Any):
        pass

    def unshift(self, node):
        pass

    def shift(self):
        pass

    def pop(self) -> Optional[Node]:
        pass

    def delete_node(self, node_: CircularNode):
        if self.head:
            # if the head node matches the node we are looking for
            if self.head == node_:
                # set the current pointer to the head node. This will be used to track the last node as the pointer
                # moves through the list
                current = self.head
                # move through the list until we reach the pointer that points batck to the head node.
                while current.next != self.head:
                    current = current.next

                # if the head node equals the next node, that means that this linked list has a length of 1, i.e. just 1
                # node. The head node can be set to None
                if self.head == self.head.next:
                    self.head = None
                else:
                    # set the current pointer to point to the current head's next
                    current.next = self.head.next
                    # set the head to now become the next node
                    self.head = self.head.next
            else:
                # we have a situation where the head node's key is not equal to the head node, therefore, we need to
                # traverse the list to find the first node whose key matches the given key. Setting current to the head
                # node acts as the pointer that we keep track of
                current = self.head
                # previous pointer helps to keep track of the previous node as we traverse, it is initially set to None
                previous: Optional[CircularNode] = None

                # we iterate through the linked list as long as the next pointer of the current head is not equal to
                # the head node. This is to avoid an infinite loop as this is a circular linked list.
                while current.next != self.head:
                    # we set the previous pointer to the current node to keep track of the node before we reset the
                    # current pointer to the next node
                    previous = current
                    # move the current pointer to the next node
                    current = current.next
                    # if the current node's key is equal to the key we are searching for
                    if current == node_:
                        # we set the previous node's next pointer to point to the current node's next pointer.
                        # Essentially removing the current node from the list
                        previous.next = current.next
                        # set the current node to the current's next node
                        current = current.next

    def delete_node_at_position(self, position: int):
        pass

    def delete_node_by_key(self, key: Any):
        if self.head:
            # if the head node's key matches the key we are looking for
            if self.head.key == key:
                # set the current pointer to the head node. This will be used to track the last node as the pointer
                # moves through the list
                current = self.head
                # move through the list until we reach the pointer that points batck to the head node.
                while current.next != self.head:
                    current = current.next

                # if the head node equals the next node, that means that this linked list has a length of 1, i.e. just 1
                # node. The head node can be set to None
                if self.head == self.head.next:
                    self.head = None
                else:
                    # set the current pointer to point to the current head's next
                    current.next = self.head.next
                    # set the head to now become the next node
                    self.head = self.head.next
            else:
                # we have a situation where the head node's key is not equal to the head node, therefore, we need to
                # traverse the list to find the first node whose key matches the given key. Setting current to the head
                # node acts as the pointer that we keep track of
                current = self.head
                # previous pointer helps to keep track of the previous node as we traverse, it is initially set to None
                previous: Optional[CircularNode] = None

                # we iterate through the linked list as long as the next pointer of the current head is not equal to
                # the head node. This is to avoid an infinite loop as this is a circular linked list.
                while current.next != self.head:
                    # we set the previous pointer to the current node to keep track of the node before we reset the
                    # current pointer to the next node
                    previous = current
                    # move the current pointer to the next node
                    current = current.next
                    # if the current node's key is equal to the key we are searching for
                    if current.key == key:
                        # we set the previous node's next pointer to point to the current node's next pointer.
                        # Essentially removing the current node from the list
                        previous.next = current.next
                        # set the current node to the current's next node
                        current = current.next

    def delete_nodes_by_key(self, key: T):
        pass

    def delete_middle_node(self) -> Optional[Node]:
        pass

    def display(self):
        pass

    def display_forward(self):
        pass

    def display_backward(self):
        pass

    def alternate_split(self):
        pass

    def split_list(self) -> Optional[Tuple[Self, Optional[Self]]]:
        """
        Splits a circular linked list into two halves and returns the two halves in a tuple. If the size is 0, i.e. no
        nodes are in this linked list, then it returns None. If the size is 1, then the first portion of the tuple, at
        index 0 will be the head of this circular linked list, while the second portion will be None.
        Returns:
            Tuple: tuple with two circular linked lists
        """
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head, None

        mid = size // 2
        count = 0

        previous: Optional[CircularNode] = None
        current = self.head

        while current and count < mid:
            count += 1
            previous = current
            current = current.next

        previous.next = self.head

        second_list = CircularLinkedList()
        while current.next != self.head:
            second_list.append(current.data)
            current = current.next

        second_list.append(current.data)

        return self, second_list

    def is_palindrome(self) -> bool:
        pass

    def pairwise_swap(self) -> Node:
        pass

    def swap_nodes_at_kth_and_k_plus_1(self, k: int) -> Node:
        pass

    def move_to_front(self, node: Node):
        pass

    def move_tail_to_head(self):
        pass

    def partition(self, data: Any) -> Union[Node, None]:
        pass

    def remove_tail(self):
        pass

    def remove_duplicates(self) -> Optional[Node]:
        pass

    def rotate(self, k: int):
        pass

    def reverse_groups(self, k: int):
        pass

    def odd_even_list(self) -> Optional[Node]:
        pass

    def maximum_pair_sum(self) -> int:
        pass
