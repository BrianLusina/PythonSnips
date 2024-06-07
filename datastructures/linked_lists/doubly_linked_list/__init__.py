from typing import Any, Union, Optional, Dict

from datastructures.linked_lists import LinkedList, Node, T
from datastructures.linked_lists.exceptions import EmptyLinkedList
from .node import DoubleNode


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list which will implement methods from LinkedList parent class
    Doubly linked lists have nodes which have reference to its predecessor and its successor
    """

    def __init__(self):
        super().__init__()
        self.head: Optional[DoubleNode] = None
        self.tail: Optional[DoubleNode] = None

    def __str__(self):
        return "<->".join([f"DoubleNode(data={item})" for item in self])

    def __repr__(self):
        return "<->".join([f"DoubleNode(data={item})" for item in self])

    def __len__(self):
        count = 0

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def append(self, data: T):
        """
        Add a node to the end of Linked List

        We have to traverse the linked list to get to the tail and assign the tail node's next node from None to
        the linked list we intend to append.

        Complexities:
        Space Complexity = O(1) as no new variables are used in memory, this operation is done in place
        Time Complexity = O(n) as we are traversing only 1 linked list
        """
        new_node = data if isinstance(data, DoubleNode) else DoubleNode(data)

        # if the head does not exist, set the head to the node
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.previous = self.tail
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.previous = current
            return

    def prepend(self, data: T):
        node = data if isinstance(data, DoubleNode) else DoubleNode(data)
        if self.head:
            self.head.previous = node
            node.next = self.head
            self.head = node
            return
        # no head node, means that this is empty. Thus, we set the head node to this node
        self.head = node
        return

    def insert_after_node(self, key: Any, data: T):
        if self.is_empty():
            raise EmptyLinkedList("LinkedList has no Nodes")
        if not key:
            raise ValueError("Prev Node Key can not be None")
        if not data:
            raise ValueError("Data to insert can not be None")

        current = self.head

        # traverse the linked list until we find the node to insert
        while current:
            # if we are at the end, then simply append the node to the end
            if not current.next and current.key == key:
                self.append(data)
                return

            # if the key matches the current node
            elif current.key == key:
                # create the new node
                node_to_insert = DoubleNode(data)
                # set the next node in a temporary variable, nxt in this case
                nxt = current.next
                # set the current next pointer to point to the new node
                current.next = node_to_insert
                # set the new node's next pointer to point to the nxt variable, this represents the current node's next
                # pointer
                node_to_insert.next = nxt
                # set the previous pointer of the new node to point to the current node
                node_to_insert.previous = current
                # we are done with insertion, we can exit the loop and function
                return
            # move the pointer to the next node
            current = current.next

    def insert_before_node(self, next_key: Any, data: T):
        current = self.head
        while current:
            if not current.previous and current.key == next_key:
                self.prepend(data)
                return
            elif current.key == next_key:
                new_node = DoubleNode(data)
                previous = current.previous
                previous.next = new_node
                current.previous = new_node
                new_node.next = current
                new_node.previous = previous
                return

            current = current.next

    def pop(self) -> Optional[DoubleNode]:
        """
        Removes the last item from the list and returns it. This performs the operation in O(1) time as we already know
        the last node in the linked list
        :return: Node at the last position
        """
        if not self.head:
            return None

        if not self.head.next:
            # for instances where there is no next Node. i.e. DoublyLinkedList has a length of 1
            node = self.head
            self.head = None
            self.tail = None
            return node

        last_node = self.tail
        last_node_prev = self.tail.previous
        last_node_prev.next = None
        self.tail = last_node_prev
        return last_node

        # Below is a viable option if we are not keeping track of the tail node in the linked list. This involves
        # needing to traverse the whole linked list to reach the last node. Note that this ends up being an O(n) operation

        # current = self.head
        #
        # while current.next:
        #     current = current.next
        #
        # # if the current node has a pointer to the previous node
        # if current.prev:
        #     # we assign the previous pointer to a 'temp' variable
        #     last_node_prev = current.prev
        #
        #     # then assign the next node to None
        #     last_node_prev.next = None
        #
        #     # and lastly set the new tail
        #     self.tail = last_node_prev
        #
        # # return the last node
        # return current

    def shift(self) -> Optional[Any]:
        """
        Removes value at the front of the doubly linked list. If there is no head node, None is returned.
        :return: deleted node's data
        """
        if self.head:
            data = self.head.data
            new_head_ = self.head.next

            # set the previous pointer for the head node to None if one exists.
            if new_head_:
                new_head_.prev = None

            self.head = new_head_
            return data
        return None

    def unshift(self, value: Any):
        """
        Inserts a value at the front of the doubly linked list
        :param value: data to add at the front of the list
        """
        return self.prepend(value)

    def get_nth_node(self, position: int) -> Union[Node, None]:
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

    def delete_nodes_by_key(self, key: Any):
        # no head node, means nothing to delete
        if not self.head:
            return

        # set the pointer to the head node
        current = self.head
        # move through each node in the list as long as it is not None
        while current:
            # check if this node's key should be deleted
            if current.key == key:
                # re-assign the nodes by deleting this node
                self.delete_node_by_key(current.key)

            # move on to the next node either after successful deletion or not
            current = current.next

    def delete_middle_node(self) -> Optional[Node]:
        pass

    def delete_node_at_position(self, position: int) -> Union[DoubleNode, None]:
        """
        Deletes a node at the specified position
        """
        super().delete_node_at_position(position)

        current = self.head

        # we are re-assigning the head node in the linked list if the position is 0. Then we return the deleted node at
        # position 0
        if position == 0:
            self.head = current.next
            current.next.prev = self.head
            return current

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError("Invalid position found, reached end of list")

            current.data = current.next.data
            current.next = current.next.next
            current.next.prev = current.previous
            return self.head

    def delete_node(self, double_node: DoubleNode):
        # if it is the first node
        if double_node.key == self.head.key:
            # if there is a node after the head
            if self.head.next:
                next_node = self.head.next
                next_node.prev = None
                self.head = next_node
                double_node.next = None
                return
            self.head = None
            return

        current_node = self.head
        while current_node:
            if current_node.key == double_node.key:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

            current_node = current_node.next

    def delete_node_by_key(self, key: Any):
        # no head node, means nothing to delete
        if not self.head:
            return

        # no next node, means we check if the head node is the one we should delete
        if not self.head.next:
            # if the head node's key matches what we are looking for
            if self.head.key == key:
                self.head = None
                return

        # in the event we have a head node and the head node's key matches the key we intend to remove from the Linked
        # List, then we simply re-assign the head node to the next node and the head node's next's previous pointer is
        # set to None
        if self.head.key == key:
            self.head.previous = None
            self.head = self.head.next
            return

        # at this point, we have more than 1 node to check, we set the pointer to the head node(marked as current)
        current = self.head
        # this will be used to keep track of the previous node of the node to delete
        previous: Optional[DoubleNode] = None

        # we move the pointer down the LinkedList until we find the Node whose key matches what we want to delete
        while current and current.key != key:
            previous = current
            current = current.next

        # if there is no node that matches the condition above, we exit
        if not current:
            return

        # re-assign the pointers of the nodes around the node to delete. That is, moving the previous node's next
        # pointer to the current node's next pointer and then assign current to None. This essentially 'deletes'
        # the node by the data attribute
        previous.next = current.next

        # it is possible that this is the tail node, so, the current pointer, may not have a next set, we check if
        # there is a next and set that node to point to the previous
        if current.next:
            current.next.prev = previous
        # set the current pointer to None to complete the deletion
        current = None
        return

    def reverse(self) -> Optional[DoubleNode]:
        """
        Order of operations is important here. We set the current node's next pointer to next before setting previous to
        the current pointer's next
        We return previous because when we exit, current pointer is None, which means that the last
        node we visited—previous—was the tail of the original list, and thus the head of
        our reversed list.

        Complexity:
        O(n) time and O(1) space.

        We pass over the list only once, and maintain a constant number of variables in memory.

        Another implementation/variation to this approach:
          prev = None
          cur = self.head
          while cur:
            nxt = cur.next
            cur.next = prev
            cur.prev = nxt
            prev = cur
            cur = nxt
          self.head = prev

        Returns:
            DoublyLinkedList: reversed doubly linked list
        """

        if self.head is None:
            return None

        # nothing to reverse here
        if self.head.next is None:
            return self.head

        current = self.head
        previous: Optional[DoubleNode] = None

        # do this, until we are at the end of the linked list
        while current:
            # copy a pointer to the next element, before we overwrite the current
            next_ = current.next

            # reverse the next pointer & previous pointer
            current.next = previous
            current.previous = next_

            # step forward in the list
            previous = current
            current = next_

        # actually reverses the current DoublyLinkedList
        self.head = previous

        # returns the head of the reversed DoublyLinkedList
        return previous

    def insert_sorted(self, node: DoubleNode, data: int):
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
            new_tail = DoubleNode(data, previous=node)
            node.next = new_tail
            return node

        # if at the node the data value is already less than the data we intend to insert we make
        # this node the head of the doubly linked list
        if node.data > data:
            new_head = DoubleNode(data, next_=node)
            node.previous = new_head
            return new_head

        current = node

        while current:
            next_node = current.next

            # we are at the end of the doubly linked list, so we create a new DoubleNode and make it the tail
            if next_node is None:
                new_node = DoubleNode(data, previous=current)
                current.next_node = new_node
                return node

            # we create a new node and insert it into 2 nodes iff it is less than the next node value and
            # less than the previous node value
            if current.data <= data <= next_node.data:
                new_node = DoubleNode(data=data, previous=current, next_=next_node)
                next_node.prev = new_node
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
            print(
                current_node.previous.data
                if hasattr(current_node.previous, "value")
                else None
            )
            print(current_node.data)
            print(
                current_node.next.data if hasattr(current_node.next, "value") else None
            )
            current_node = current_node.next
        print("*" * 10)

    def display_backward(self):
        pass

    def display_forward(self):
        pass

    def remove_duplicates(self):
        """
        Removes duplicates from linked list
        """

        if self.head is None or self.head.next is None:
            return

        seen: Dict[Any, bool] = dict()
        current = self.head

        while current:
            if current.key not in seen:
                seen[current.key] = True
                current = current.next
            else:
                # retrieve the next and the previous pointers of the current duplicate node
                next_ = current.next
                previous = current.previous

                # set the previous node of this current node to point to the current node's next
                previous.next = next_
                # next_ could possibly be None and if so, this means we are at the end of the linked list. Therefore, we
                # check that it's available and set it's previous pointer
                if next_:
                    next_.previous = previous

                # move the pointer to the next node
                current = next_

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
                current.next_node.next_node.previous = temp
            else:
                # we are at the end
                temp.next_node = None

            # keep moving the pointer
            current = current.next_node

        return first, second

    def is_palindrome(self) -> bool:
        """
        Uses two pointer approach to check if this is a palindrome linked list. Since this is a doubly linked list, each
        node knows about the previous node in the linked list. Therefore, it is possible to do this in 2 passes. First
        two pointers are initialized and set to the head node, then the last pointer is traversed until it reaches the
        last node in the doubly linked list. This results in an O(n) computation task, where n is the number of nodes.

        Second, the second pass compares the first pointer to the last pointer as long as we don't reach the middle,then
        we can check the data item at each pointer. if they do not match, then we return false, if they do, the first
        pointer moves 1 position, while the last pointer moves in the opposite direction using the previous pointer.
        This continues until the two pointers reach the middle.

        Space Complexity results in O(1) as no extra space is required other than reference to the pointers in the list.
        Time is O(n) as the algorithm has to traverse the linked list to set the last pointer to the end of the linked
        list.
        """
        if self.head:
            # A LinkedList with 1 Node is a Palindrome
            if not self.head.next:
                return True

            first_pointer = self.head
            last_pointer = self.head

            while last_pointer.next:
                last_pointer = last_pointer.next

            while first_pointer.next != last_pointer.previous:
                if first_pointer.data != last_pointer.data:
                    return False
                first_pointer = first_pointer.next
                last_pointer = last_pointer.previous

            return True
        else:
            return True

    def pairwise_swap(self) -> DoubleNode:
        # nothing to do here
        if not self.head:
            return self.head

        current = self.head

        # loop as long as there are at least 2 nodes left
        while current and current.next:
            # if both nodes have the same value/data
            if current.data == current.next.data:
                # no need to swap, move on to the next pair
                current = current.next.next
            else:
                # swap data of node with the next node's data
                current.data, current.next.data = current.next.data, current.data

                # move on to the next pair
                current = current.next.next

        # at this point, the linked list has been swapped in pairs
        return self.head

    def swap_nodes_at_kth_and_k_plus_1(self, k: int) -> DoubleNode:
        a, b = self.head, self.head

        for _ in range(1, k):
            a = a.next

        node, a = a, a.next

        while a:
            a, b = a.next, b.next

        node.data, b.data = b.data, node.data

        return self.head

    def move_to_front(self, node: DoubleNode):
        if self.head:
            prev = node.previous
            prev.next = node.next
            node.next.prev = prev
            node.next = self.head
            self.head.previous = node
        else:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.previous = self.head

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head

            while last.next:
                last = last.next

            # we can obtain the second_to_last node from the last node
            second_to_last = last.previous

            # set the current head node's second_to_last pointer to the last node
            self.head.previous = last
            # set the next pointer of the last node to the head node
            last.next = self.head
            # remove the second_to_last pointer of the last node
            last.previous = None
            # remove the next pointer of the second_to_last node
            second_to_last.next = None

            # set the head node as the last node
            self.head = last

    def remove_tail(self):
        current = self.head

        if not current:
            return
        else:
            while current:
                current = current.next

            prev = current.previous
            prev.next = None

    def partition(self, data: Any) -> Union[Node, None]:
        pass

    def rotate(self, k: int):
        pass

    def reverse_groups(self, k: int):
        pass

    def odd_even_list(self) -> Optional[Node]:
        pass

    def maximum_pair_sum(self) -> int:
        pass
