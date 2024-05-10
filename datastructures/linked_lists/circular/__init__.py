from typing import Optional, Any, Union

from datastructures.linked_lists import LinkedList, Node, T
from .node import CircularNode


class CircularLinkedList(LinkedList):
    head: Optional[CircularNode] = None

    def __init__(self):
        super().__init__()

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
            new_node = CircularNode(value=data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        pass

    def reverse(self):
        pass

    def insert(self, node, pos):
        pass

    def insert_after_node(self, prev: Any, data: Any):
        pass

    def unshift(self, node):
        pass

    def shift(self):
        pass

    def pop(self) -> Optional[Node]:
        pass

    def delete_node(self, node: Node):
        pass

    def delete_node_at_position(self, position: int):
        pass

    def delete_node_by_data(self, data: Any):
        pass

    def delete_nodes_by_data(self, data: Any):
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
