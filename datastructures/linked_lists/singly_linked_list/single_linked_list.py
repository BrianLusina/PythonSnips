from typing import Any, Union, Optional, Dict, List, Tuple

from datastructures.stacks.dynamic import DynamicSizeStack as Stack
from datastructures.linked_lists.singly_linked_list.node import SingleNode
from datastructures.linked_lists import LinkedList, T, Node
from datastructures.linked_lists.exceptions import EmptyLinkedList
from datastructures.linked_lists.singly_linked_list.single_linked_list_utils import (
    reverse_list,
    merge_and_weave,
)


class SinglyLinkedList(LinkedList):
    """
    Implementation of a SinglyLinked List
    """

    head: Optional[SingleNode] = None

    def __init__(self):
        # noinspection PyCompatibility
        super().__init__()

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        """Counts the number of nodes in this singly linked list. This takes O(n) time, where n is the number of nodes
        in the linked list"""
        count = 0

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def append(self, data: Any):
        """
        Add a node to the Linked List

        We have to traverse the linked list to get to the tail and assign the tail node's next node from None to the new
        node we intend to append.

        Complexities:
        Space Complexity = O(1) as no new variables are used in memory, this operation is done in place
        Time Complexity = O(n) as we are traversing only 1 linked list

        Args:
            data (Any): the data to add to the new node
        """
        node_ = data if isinstance(data, SingleNode) else SingleNode(data, None)

        if not self.head:
            self.head = node_
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node_

    def prepend(self, data):
        node_ = data if isinstance(data, SingleNode) else SingleNode(data)
        node_.next = self.head
        self.head = node_

    def insert_after_node(self, prev_node: Any, data: Any):
        if self.is_empty():
            raise EmptyLinkedList("LinkedList has no Nodes")
        if not prev_node:
            raise ValueError("Prev Node can not be None")
        if not data:
            raise ValueError("Data to insert can not be None")

        prev_node = (
            prev_node if isinstance(prev_node, SingleNode) else SingleNode(prev_node)
        )
        node_to_insert = SingleNode(data)

        current = self.head

        # traverse the linked list until we find the node to insert
        while current.next:
            if current == prev_node:
                node_to_insert.next = prev_node.next
                prev_node.next = node_to_insert
                # we have inserted the node, now we can exit
                break
            current = current.next

    def insert_before_node(self, next_key: Any, data: T):
        pass

    def get_nth_node(self, position: int) -> Union[SingleNode, None]:
        """
        Gets nth node in a linked list given the head of the linked list
        :raises: ValueError for position less than 0 or position is greater than length of linked list
        :rtype: SingleNode
        :returns: None when the head is None & SingleNode
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

    def delete_node_at_position(self, position: int) -> Optional[SingleNode]:
        """
        Deletes a node at the specified position
        """
        super().delete_node_at_position(position)

        current = self.head

        # we are re-assigning the head node in the linked list if the position is 0. Then we return the deleted node at
        # position 0
        if position == 0:
            self.head = current.next
            return current

        while current is not None:
            for _ in range(position):
                current = current.next

                if current is None:
                    raise ValueError(
                        f"Invalid position {position} found, reached end of list"
                    )

            current.data = current.next.data if current.next else None
            current.next = current.next.next if current.next else None

            return self.head
        return None

    def delete_node(self, single_node: SingleNode):
        if not self.head:
            return

        # if the node we are deleting is the head node
        if self.head == single_node:
            self.head = self.head.next
            return

        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == single_node.data:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

    def delete_node_by_key(self, key: Any):
        current = self.head

        # in the event we have a head node and the head node's data matches the data we intend to remove from the Linked
        # List, then we simply re-assign the head node to the next node
        if current and current.data == key:
            self.head = current.next

            return

        # this will be used to keep track of the previous node of the node to delete
        previous = None

        # we move the pointer down the LinkedList until we find the Node whose data matches what we want to delete
        while current and current.data != key:
            previous = current
            current = current.next

        # if there is no node that matches the condition above, we exit
        if not current:
            return

        # re-assign the pointers of the nodes around the node to delete. That is, moving the previous node's next
        # pointer to the current node's next pointer. This essentially 'deletes' the node by the data attribute
        previous.next = current.next

        return

    def delete_nodes_by_key(self, key: Any):
        dummy_head = SingleNode(-1)
        dummy_head.next = self.head
        current = dummy_head

        while current.next:
            if current.next.data == key:
                current.next = current.next.next

            else:
                current = current.next

        return dummy_head.next

    def delete_middle_node(self) -> Optional[SingleNode]:
        """
        Deletes the middle node of a linked list and returns it.
        Note that this uses 2 passes, the first pass is to get the node count which results in a Time complexity of O(n)
        where n is the number of nodes in the linked list. The first iteration to get the node count traverses the whole
        linked list, the second pass, traverses half of the linked list to get to the middle node.

        No extra space is used, therefore the space complexity is O(1)
        @return: middle node
        """
        if not self.head or not self.head.next:
            return None

        # Node count here is obtained which results in O(n)
        node_count = len(self)
        middle_index = node_count // 2

        current = self.head

        # traversing half the linked list to get to the predecessor of the middle node(i.e. the node before the middle node)
        for _ in range(middle_index - 1):
            current = current.next

        # we have the middle node, now we assign it and return it later
        middle_node = current.next

        # deleting is handled by moving the next pointer of the predecessor to the next pointer of the middle node
        current.next = current.next.next

        return middle_node

    def delete_middle_node_2_pointers(self) -> Optional[SingleNode]:
        """
        Deletes the middle node of a linked list and returns it, this is a variation of delete_middle_node which uses 2
        pointers which avoids making 2 passes like the first approach

        Time complexity of O(n) where n is the number of nodes in the linked list.

        No extra space is used, therefore the space complexity is O(1)
        @return: middle node
        """
        if not self.head or not self.head.next:
            return None

        slow, fast = self.head, self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # we have the middle node, now we assign it and return it later
        middle_node = slow.next

        # deleting is handled by moving the next pointer of the predecessor to the next pointer of the middle node
        slow.next = slow.next.next

        return middle_node

    def delete_nth_last_node(self, n: int) -> Optional[Node]:
        length_of_linked_list = len(self)

        if not 1 <= n <= length_of_linked_list:
            raise ValueError(f"Position {n} is out of bounds")

        if not self.head.next:
            return self.head

        position_of_node_to_delete = length_of_linked_list - n

        self.delete_node_at_position(position_of_node_to_delete)

        return self.head

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

    def pop(self) -> Union[SingleNode, None]:
        if not self.head:
            return None

        if not self.head.next:
            # for instances where there is no next Node. i.e. SinglyLinkedList has a length of 1
            node_ = self.head
            self.head = None
            return node_

        # pointer to current node
        current = self.head

        # holds a pointer reference to the node before the current pointer
        current_prev = self.head

        while current.next:
            # as we move the next pointer down the SinglyLinkedList, we also need to ensure that we are moving the
            # previous pointer down the linked list
            current_prev = current
            current = current.next

        # assign the current pointer's previous node's next to None
        current_prev.next = None
        return current

    def reverse(self) -> Optional[SingleNode]:
        """
        Returns the head of the newly reversed LinkedList

        Uses an iterative approach to reverse this linked list.
        If the linked list has only 0 or 1 node, then just return the head.
        If that is not the case, then the iterative approach is best where there are 2 pointers.
        1. reversed_list: A pointer to already reversed linked list. initialized to head
        2. list_to_reverse: pointer to the remaining list. initialized to head->next

        we then set the reversed_list->next to None, this then becomes the last node. reversed_list will
        always point to the head of the newly reversed linked list

        At each iteration, the list_to_reverse pointer moves forward (until it reaches NULL).
        The current node becomes the head of the new reversed linked list and starts pointing to the previous head of
        the reversed linked list.
        The loop terminates when list_to_reverse becomes NULL, and the reversed_list pointer is pointing to the new
        head at the termination of the loop.

        Another implementation/variation to this approach:
          prev = None
          cur = self.head
          while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
          self.head = prev
        """
        if self.head is None or self.head.next is None:
            return self.head

        list_to_reverse = self.head.next

        reversed_list = self.head
        reversed_list.next = None

        while list_to_reverse:
            temp = list_to_reverse

            # move the pointer to the next node
            list_to_reverse = list_to_reverse.next

            # point the list_to_reverse to the reversed linked list. Making the reversed_list the next node
            temp.next = reversed_list
            reversed_list = temp

        self.head = reversed_list
        return reversed_list

    def reverse_between(self, left: int, right: int) -> Optional[SingleNode]:
        """
        Reverse linked list between left and right node positions.
        This uses the iterative link reversal to reverse a sublist of the linked list between the left and the right
        positions in the linked list.
        This is based on the assumption that we don't have access to the data in the nodes themselves,
        but instead we can change the links between the nodes.

        Starting from the node at position left all the way to position right, we reverse the next pointers for
        all the nodes in between.

        Ref: https://leetcode.com/problems/reverse-linked-list-ii/solution/

        Time Complexity: O(N) considering the list consists of N nodes.
        We process each of the nodes at most once (we don't process the nodes after the right node from the beginning.)

        Space Complexity: O(1) since we simply adjust some pointers in the original linked list and only use O(1) additional
        memory for achieving the final result.

        Args:
            left (int): the starting position
            right (int): the end position

        Returns:
            Optional[SingleNode]: the head of the reversed linked list
        """
        if left > right:
            raise ValueError(f"left {left} cannot be greater than right {right}")

        if left < 1 or right < 1:
            raise ValueError("left and right must be positive integers")

        if self.head is None or self.head.next is None:
            return self.head

        if right > len(self):
            raise ValueError(
                f"right {right} cannot be greater than the length of the linked list {len(self)}"
            )

        if left == right:
            return self.head

        # Move the 2 pointers until they reach the proper starting point in the list
        current_pointer, previous_pointer = self.head, None

        while left > 1:
            previous_pointer = current_pointer
            current_pointer = current_pointer.next
            left, right = left - 1, right - 1

        # The 2 pointers that will fix the final connections
        tail_pointer, conn_pointer = current_pointer, previous_pointer

        # iteratively reverse the nodes until right becomes 0
        while right:
            third_pointer = current_pointer.next
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer
            current_pointer = third_pointer
            right -= 1

        # Adjust the final connections
        if conn_pointer:
            conn_pointer.next = previous_pointer
        else:
            self.head = previous_pointer

        tail_pointer.next = current_pointer
        return self.head

    def reverse_between_with_dummy(self, left: int, right: int) -> Optional[SingleNode]:
        """
        Reverse linked list between left and right node positions using a dummy node

        Algorithm steps:
        - We initialize a dummy node, which will be helpful in scenarios where the reversal of the sublist starts from
        the head of the list.
        - We set the next node of dummy to point to the head of the list.
        - We initialize a pointer, prev, to the dummy node. This pointer will help us reconnect the sublist to the
        entire list after it has been reversed.
        - We use a loop to traverse the list with the prev pointer and until it reaches the node immediately before the
        sublist to be reversed.
        - We initialize a curr pointer, which points to the node next to prev.
        - Another loop is used to reverse the sublist. This loop iterates right - left times, which is the number of
        nodes in the sublist minus one:
            - We set next_node to curr.next, representing the node to be moved to the front of the reversed sublist.
            - We update curr.next to next_node.next, effectively removing next_node from its current position in the
            sublist.
            - We set next_node.next to prev.next, inserting next_node at the beginning of the reversed sublist.
            - We update prev.next to next_node, adjusting the pointer to next_node for the next iteration.

        - Finally, we return dummy.next, which is the head of the modified linked list.

        Args:
            left (int): the starting position
            right (int): the end position

        Returns:
            Optional[SingleNode]: the head of the reversed linked list
        """
        if left > right:
            raise ValueError(f"left {left} cannot be greater than right {right}")

        if left < 1 or right < 1:
            raise ValueError("left and right must be positive integers")

        if self.head is None or self.head.next is None:
            return self.head

        if right > len(self):
            raise ValueError(
                f"right {right} cannot be greater than the length of the linked list {len(self)}"
            )

        if left == right:
            return self.head

        # Create a dummy node to handle edge case when left = 1
        dummy = SingleNode(0)
        dummy.next = self.head
        prev = dummy

        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Current node is the node at left position
        curr = prev.next

        # Reverse the portion of the linked list between left and right positions
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        # Return the updated head of the linked list
        return dummy.next

    def unshift(self, node_: SingleNode) -> SingleNode:
        node_.next = self.head
        self.head = node_
        return self.head

    def insert(self, node_, pos):
        counter = 1
        current = self.head

        if pos > 1:
            while current and counter < pos:
                if counter == pos - 1:
                    node_.next = current.next
                    current.next = node_
                current = current.next
                counter += 1
        elif pos == 1:
            node_.next = self.head
            self.head = node_

    def display(self):
        print("Displaying data...")
        current_node = self.head
        while current_node is not None:
            print(current_node.data, ">>>")
            current_node = current_node.next
        print(None)

    def display_backward(self):
        pass

    def display_forward(self):
        pass

    def contains_cycle(self) -> bool:
        """
        Check if the SinglyLinkedList contains a cycle, This uses floyd's cycle detection algorithm to check if a linked
        list contains a cycle. A cycle in a linked list is determined by a node in the linked list having its next pointer
        point to a node in the same liked list.

        Complexity Analysis:
        n is the number of nodes in the linked list

        Time: O(n), we traverse the nodes in the linked list iteratively, at the worst case, we traverse all the nodes
        in the linked list until we reach the end of the linked list

        Space: O(1) as there is no extra space used other than the pointers used to traverse the linked list.

        Returns:
            bool: True if the linked list contains a cycle, False otherwise
        """
        if not self.head or not self.head.next:
            return False

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

    def remove_duplicates(self) -> Optional[SingleNode]:
        """
        Removes duplicates from linked list. Uses a dictionary to keep track of seen values in the linked list.
        For every encountered duplicate value, it is discarded and removed from the linked list.

        Complexity:
        Where n is the number of nodes in the linked list:

        Time O(n): as this iterates through each node in the linked list checking its value against what's in the
        dictionary

        Space O(n); a dictionary is used to store duplicate values in the linked list. In the worst case no duplicates
        exist so, the dictionary has all the values from every node in the linked list.
        """

        if self.head is None or self.head.next is None:
            return self.head

        seen: Dict[Any, bool] = dict()
        current = self.head
        previous: Optional[SingleNode] = None

        while current:
            if current.data in seen:
                # remove node
                previous.next = current.next
                current = None
            else:
                # add node data to seen
                seen[current.data] = True
                previous = current

            current = previous.next

        return self.head

    def alternate_split(self) -> tuple:
        if not self.head or not self.head.next:
            raise ValueError("Head should not be none")

        current = self.head

        # head for the first linked list
        first = current

        # head for the second linked list
        second = current.next

        while current and current.next:
            temp = current.next

            # set the next node for the first linked list
            current.next = temp.next

            # check if the next node is available for the second linked list
            if current.next and current.next.next:
                # set the next node for the second linked list
                temp.next = current.next.next
            else:
                # we are at the end
                temp.next = None

            # keep moving the pointer
            current = current.next

        return first, second

    def is_palindrome(self) -> bool:
        """
        Checks to see if a Linked list is a Palindrome.
        Returns True if it is, false otherwise.
        Uses a stack, where we add the values/data of each node into a stack
        & reset the pointer back to the head. We then traverse the linked list from the head
        as we pop the data items from the stack(this will be the last added data item of the tail node)
        & check each node's value to the data item popped from the stack. If any differ, then it is not
        a Palindrome

        Complexity:
        We assume that n is the number of nodes in the linked list

        Time O(n): we traverse the linked list twice, the first time is to add the nodes to the stack, the second time(
        after the pointer has been reset to the head node) is to check each item as it's popped off from the stack if
        it matches the current data item at the pointer's position. This is O(2*n), but since we ignore constants it is
        O(n) as the worst case

        Space O(n): a stack data structure is used to store the data items of each node in the linked list. Therefore
        the stack needs to occupy space which results in it being the same size as the nodes in the linked list. At the
        first pass, it will contain all the data items of each node in the linked list.

        Returns:
            bool: True if the linked list is a palindrome, false otherwise.
        """

        # an empty linked list is consided a palindrome
        if not self.head or not self.head.next:
            return True

        current = self.head
        stack = Stack()

        while current:
            stack.push(current.data)
            current = current.next

        # reset the pointer
        current = self.head

        while current:
            data = stack.pop()
            if current.data != data:
                return False
            current = current.next

        return True

    def is_palindrome_2(self) -> bool:
        """
        Checks to see if a Linked list is a Palindrome. Returns True if it is, false otherwise.

        Uses two pointers approach to check if a linked list is a palindrome. First it finds the middle of the list using
        two pointers a fast and a slow pointer and then reverses the second half of the list. Once the second half is
        reversed, it compares the first half and the reversed second half

        This modifies the linked list

        Complexity:
        We assume that n is the number of nodes in the linked list

        Time O(n): we traverse the linked list to check for the palindrome property.
        Space O(1): No extra space is used when traversing the linked list

        Returns:
            bool: True if the linked list is a palindrome, false otherwise.
        """

        # An empty LinkedList or with 1 Node is a Palindrome
        if not self.head or not self.head.next:
            return True

        # Find the middle of the list using fast and slow pointers. The fast pointer will have gotten to the end of the
        # the linked list and the slow pointer will be at the middle of the linked list
        middle_node = self.middle_node()

        # reverse the second half of the list
        prev = self.reverse_list(middle_node)

        # now prev is the head of the reversed second half
        # compare the first half and the reversed second half
        left, right = self.head, prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

    def pairwise_swap_with_modification(self) -> Optional[SingleNode]:
        """
        Swaps nodes in pairs.
        However, this swaps the values of the nodes in pairs and not the pointers

        Return:
            SingleNode: new head node or None if no head exists.
        """
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

    def pairwise_swap(self) -> Optional[SingleNode]:
        """
        Swaps nodes in pairs without swapping the values in the nodes.

        Return:
            SingleNode: new head node or None if no head exists.
        """
        # nothing to do here
        if not self.head:
            return self.head

        # Create a dummy node with a value of None
        dummy_node = SingleNode(None)
        # This dummy node acts as the prev_node for the head node
        # of the list and hence stores pointer to the head node
        dummy_node.next = self.head
        prev_node = dummy_node

        # While the head node and the next node exist
        while self.head and self.head.next:
            # nodes to be swapped
            first_node = self.head
            second_node = self.head.next

            # perform swapping of nodes
            # i. Set the previous node's next node to be the second node
            prev_node.next = second_node
            # ii. Set the first node's next node to be the second node's next node
            first_node.next = second_node.next
            # iii. Set the second node's next node to be the first node
            second_node.next = first_node

            # re-initialise the head and the previous node for next swap
            prev_node = first_node
            self.head = first_node.next

        return dummy_node.next

    def swap_nodes_at_kth_and_k_plus_1(self, k: int) -> SingleNode:
        a, b = self.head, self.head

        for _ in range(1, k):
            a = a.next

        node_, a = a, a.next

        while a:
            a, b = a.next, b.next

        node_.data, b.data = b.data, node_.data

        return self.head

    def partition(self, data: Any) -> Union[SingleNode, None]:
        if not self.head:
            return None
        left = SinglyLinkedList()
        right = SinglyLinkedList()
        current = self.head

        while current:
            if current.data < data:
                left.append(current.data)
            elif current.data == data:
                right.prepend(current.data)
            else:
                right.append(current.data)
            current = current.next

        current_left = left.head

        if not current_left:
            return right.head
        else:
            while current_left.next:
                current_left = current_left.next

            current_left.next = right.head
            return left.head

    def move_to_front(self, node_: SingleNode):
        current = self.head
        prev = None
        if current:
            # move the pointer down the LinkedList until we reach the node that we want to move to the front
            while current and current.data != node_.data:
                prev = current
                current = current.next

            # that node does not seem to exist in the LinkedList, we should exit
            if not current:
                return

            # re-assign the pointers of the nodes around the node to delete. That is, moving the previous node's next
            # pointer to the current node's next pointer. This essentially 'deletes' the node by the data attribute
            prev.next = current.next
            return
        else:
            self.head = node_
            return

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            previous: Optional[SingleNode] = None

            while last.next:
                previous = last
                last = last.next

            last.next = self.head
            previous.next = None
            self.head = last

    def rotate(self, k: int) -> Optional[SingleNode]:
        if k == 0 or self.head is None or (self.head and not self.head.next):
            return self.head

        # initialize two pointers, a pivot node which will be set to the pivot point & last node which will be set to
        # the tail of the linked list. count helps in making the pivot_node & the last_node point to the right nodes in
        # the linked list.
        pivot_node = self.head
        last_node = self.head
        previous: Optional[SingleNode] = None
        count = 0

        # pivot_node and the last_node pointers are moved to the right positions as long as the pivot_node pointer is
        # not None & the count is less than the k position. Additionally, previous is updated to the pivot_node to
        # mark the previous node(or the node before the pivot point)
        while pivot_node and count < k:
            previous = pivot_node
            pivot_node = pivot_node.next
            last_node = last_node.next
            count += 1

        # this positions the first pointer correctly
        pivot_node = previous

        # now we move the last_node pointer to the last node in the linked list. This also keeps track of the previous
        # node before the last node
        while last_node:
            previous = last_node
            last_node = last_node.next

        last_node = previous

        # make the last node's next pointer point to the head node, This temporarily makes the linked list circular
        last_node.next = self.head
        # the new head node is now the next node after the pivot point.
        self.head = pivot_node.next

        # next we set the pivot points' next node. This breaks the circular linked list into a linear linked list
        pivot_node.next = None

        return self.head

    def reverse_groups(self, k: int) -> Optional[SingleNode]:
        """
        Reverses every k groups of a linked list and returns the new head node.
        @param k: number of groups in the linked list to reverse
        @return: new head node
        """

        def reverse_list(head_node: SingleNode) -> SingleNode:
            # track previous node, so we can point our next pointer to it
            previous = None
            # track node to loop through
            current_node = head_node

            while current_node:
                # track the next node to not lose it while adjusting pointers
                nxt = current_node.next

                # set the next pointer to the node behind it, previous
                current_node.next = previous

                # adjust the new previous node to the current node for subsequent loops
                previous = current_node

                # move our node pointer up to the next node in front of it
                current_node = nxt

            # return the new tail of the k-group which is our head
            return head_node

        if k <= 1:
            return self.head

        if self.head is None:
            return None

        # dummy node to simplify return
        dummy = SingleNode(None, self.head)

        # tail of previous k-group to fix our linked list pointers
        tail = dummy

        # set a tracking node, tracking_node, to cycle through linked list and a head of current linked list,
        # current_head
        tracking_node, current_head = self.head, self.head

        # while tracking node is tracking a node and hasn't reached end
        while tracking_node:
            # set count of current group, we start with a head so count = 1
            count = 1
            # loop until count reaches k nodes
            while count < k:
                # check if node hasn't reached end of list
                if tracking_node:
                    # move node up & increment counter
                    tracking_node = tracking_node.next
                    count += 1
                else:
                    # reached end without enough nodes, return early
                    return dummy.next

            # only perform below if we have enough nodes inside k-group and haven't reached end. node is currently at the
            # tail of the k-group after reversal it will be the head of the k-group
            if tracking_node:
                # track head of the next k group
                nxt = tracking_node.next if tracking_node else None

                # sever the list so we can reverse it
                tracking_node.next = None

                # reverse list, which will return new tail
                new_tail = reverse_list(current_head)

                # re-attach our new tail back to the remaining linked list
                new_tail.next = nxt

                # setup prev linked list to node, which was once the k-group's tail, but after reversal became the
                # k-group's head
                tail.next = tracking_node

                # update previous k-group tail to be the current groups tail
                tail = new_tail
                tracking_node, current_head = nxt, nxt

        # return head
        return dummy.next

    def remove_tail(self):
        pass

    def reorder_list(self) -> Optional[SingleNode]:
        """
        Reorders the linked list in place.
        Returns:
            head node of reversed linked list
        """
        # return early if there is no head node
        if self.head is None:
            return None

        # first split the linked list into two halves. To do this without knowing the length of the linked list beforehand
        # we must first find the middle node. This uses the slow and fast pointer approach
        middle_node = self.middle_node()

        # Store the second half head node
        second_half_head = middle_node.next
        # cut the connection between the first half and the second half
        middle_node.next = None

        # Now, we need to reverse the second half of the linked list in place
        # The reversal step involves taking the second half of the linked list and reversing it in place
        # for example, if the linked list is 1 -> 2 -> 3 -> 4 -> 5, the second half is 3 -> 4 -> 5
        # after reversing, it becomes 5 -> 4 -> 3
        reversed_second_half = self.reverse_list(second_half_head)

        # now we can merge and weave the first half and the reversed second half
        reordered_list = merge_and_weave(self.head, reversed_second_half)

        return reordered_list

    def kth_to_last_node(self, k: int) -> Optional[SingleNode]:
        """
        Gets the Kth to the last node.
        For example given a linked list of:

        a -> b -> c -> d

        if k is the number one then d should be returned
        if k is the number two then c should be returned
        if k is the number three then b should be returned
        if k is the number four then a should be returned
        if k exceeds the size of the list then None returned

        :param k: Position to get the node
        :return: Kth to the last node
        :raises: ValueError if k impossible to find kth to the last node
        """
        if k < 1:
            raise ValueError("Impossible to find less than first to last node %s" % k)

        left_node = self.head
        right_node = self.head

        for _ in range(k - 1):
            """
            Along the way, if a right node does not have a next, then k is greater than the length of the list
            thus, there can't be kth to the last node, we raise an error
            """
            if not right_node.next:
                raise ValueError(
                    "K is larger than the length of the linked list %s" % k
                )

            right_node = right_node.next

        """
        Starting with the left node on the head, move left node and right node down the list
        maintaining a distance of k between them until right node hits the end of the list
        """
        while right_node.next:
            left_node = left_node.next
            right_node = right_node.next

        """
        Since left node is k nodes behind right node
        left node is now the kth to last node
        """
        return left_node

    def odd_even_list(self) -> Optional[SingleNode]:
        if not self.head or not self.head.next:
            return None

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return self.head

    def maximum_pair_sum(self) -> int:
        if not self.head:
            return 0

        current = self.head
        values = []

        while current:
            values.append(current.data)
            current = current.next

        maximum_sum = 0
        left = 0
        right = len(values) - 1

        while left < right:
            maximum_sum = max(maximum_sum, values[left] + values[right])
            left += 1
            right -= 1

        return maximum_sum

    def maximum_pair_sum_stack(self) -> int:
        """
        Performs the same operation as maximum_pair_sum but uses a stack instead of a list of integers to keep track
        of twin nodes
        """
        if not self.head:
            return 0

        current = self.head
        stack = []

        while current:
            stack.append(current.data)
            current = current.next

        current = self.head
        size = len(stack)
        count = 1
        maximum_sum = 0

        while count <= size / 2:
            maximum_sum = max(maximum_sum, current.data + stack.pop())
            current = current.next
            count += 1

        return maximum_sum

    def maximum_pair_sum_reverse_in_place(self) -> int:
        """
        Performs the same operation as maximum_pair_sum but reverses 2nd half of a list of in place
        """
        if not self.head:
            return 0

        maximum_sum = 0
        middle_node = self.middle_node()

        # reverse the second half of linked list
        current, previous = middle_node, None

        while current:
            current.next, previous, current = previous, current, current.next

        start = self.head
        while previous:
            maximum_sum = max(maximum_sum, start.data + previous.data)
            previous = previous.next
            start = start.next

        return maximum_sum

    def pairs_with_sum(self, target: T) -> List[Tuple[SingleNode, SingleNode]]:
        pass
