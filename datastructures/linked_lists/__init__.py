from typing import Any, Union, Optional, Generic, TypeVar, List, Tuple
from abc import ABCMeta, abstractmethod

from datastructures.linked_lists.exceptions import EmptyLinkedList

T = TypeVar("T")


class Node(Generic[T]):
    """
    Node object in the Linked List
    """

    __metaclass__ = ABCMeta

    def __init__(
        self,
        data: Optional[T] = None,
        next_: Optional["Node[Generic[T]]"] = None,
        key: Any = None,
    ):
        self.data = data
        self.next = next_
        # if no key is provided, the hash of the data becomes the key
        self.key = key or hash(data)

    def __str__(self) -> str:
        return f"Node(data={self.data}, key={self.key})"

    def __repr__(self) -> str:
        return f"Node(data={self.data}, key={self.key})"

    def __eq__(self, other: "Node") -> bool:
        return self.key == other.key


class LinkedList(Generic[T]):
    """
    The most basic LinkedList from which other types of Linked List will be subclassed
    """

    __metaclass__ = ABCMeta

    def __init__(self, head: Optional[Node[Generic[T]]] = None):
        self.head: Optional[Node[Generic[T]]] = head

    def __iter__(self):
        current = self.head
        if not current:
            return

        if current:
            if current.data:
                yield current.data

        if current.next:
            node = current.next
            while node:
                if node.data:
                    yield node.data
                node = node.next

    @abstractmethod
    def __str__(self):
        return "->".join([str(item) for item in self])

    @abstractmethod
    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        """
        Implements the len() for a linked list. This counts the number of nodes in a Linked List
        This uses an iterative method to find the length of the LinkedList
        Returns:
            int: Number of nodes
        """
        return len(tuple(iter(self)))

    @abstractmethod
    def append(self, data):
        """
        Add a node to the end of the linked list
        :param data: the node to add to the list
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def prepend(self, data):
        """
        Add a node to the beginning of the linked list
        :param data: the node to add to the list
        """
        raise NotImplementedError("Not yet implemented")

    def search(self, node):
        """
        Search method to search for a node in the LinkedList
        :param node: the node being sought
        :return: the node being sought
        """
        head = self.head
        if head is not None:
            while head.next is not None:
                if head.data == node:
                    return head
                head = head.next
            if head.data == node:
                return head
        return None

    def count_occurrences(self, data: Any) -> int:
        """
        Counts the number of occurrences of a data in a LinkedList. If the linked list is empty(no head). 0 is returned.
        otherwise the occurrences of the data element will be sought using the equality operator. This assumes that the
        data element in each node already implements this operator.

        Complexity:
        The assumption here is that n is the number of nodes in the linked list.

        Time O(n): This is because the algorithm iterates through each node in the linked list to find data values in
        each node that equal the provided data argument in the function. This is both for the worst and best case as
        each node in the linked list has to be checked

        Space O(1): no extra space is required other than the value being incremented for each node whose data element
        equals the provided data argument.

        Args:
            data(Any): the data element to count.
        Returns:
            int: the number of occurrences of an element in the linked list
        """
        if self.head is None:
            return 0
        else:
            occurrences = 0
            current = self.head
            while current:
                if current.data == data:
                    occurrences += 1
                current = current.next
            return occurrences

    def get_last(self):
        """
        Gets the last node in the Linked List. check each node and test if it has a successor
        if it does, continue checking
        :return: The last Node element
        :rtype: Node
        """
        if not self.head or not self.head.next:
            return self.head

        node = self.head
        while node.next:
            node = node.next

        return node

    def get_position(self, position: int) -> Union[Node, None]:
        """
        Returns the current node in the linked list if the current position of the node is equal to the position. Assume
        counting starts from 1
        :param position: Used to get the node at the given position
        :type position int
        :raises ValueError
        :return: Node
        :rtype: Node
        """
        if position < 0 or not isinstance(position, int):
            raise ValueError("Position should be a positive integer")
        counter = 1
        current = self.head

        if position == 0 and current is not None:
            return current
        if position < 1 and current is None:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def is_empty(self):
        """
        Check if the linked list is empty, essentially if the linked list's head's successor is None
        then the linked list is empty
        :return: True or False
        :rtype: bool
        """
        return self.head is None

    @abstractmethod
    def reverse(self):
        """
        Reverses the linked list, such that the Head points to the last item in the
        LinkedList and the tail points to its predecessor. The first node becomes the tail
        :return: New LinkedList which is reversed
        :rtype: LinkedList
        """
        raise NotImplementedError("Not Yet Implemented")

    @abstractmethod
    def insert(self, node, pos):
        """
        Insert node at a particular position in the list
        :param node: node to insert
        :param pos: position to insert the node
        :type pos int
        :return: inserted node in the list along with the predecessor and successor
        :rtype: Node
        """
        raise NotImplementedError()

    @abstractmethod
    def insert_after_node(self, prev_key: Any, data: T):
        """
        Inserts a given node data after a node's key in the Linked List. First find the node in the LinkedList with the
        provided key. Get its successor, store in temp variable and insert this node with data in the position,
        get this node's next as the successor of the current node
        Args:
            prev_key Any: The node's previous key to find
            data T: The data to insert
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def insert_before_node(self, next_key: Any, data: T):
        """
        Inserts a given node data before a node's key in the Linked List.
        Args:
            next_key Any: The node's next key to find
            data T: The data to insert
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def unshift(self, node):
        """
        Insert a node at the beginning of the list
        :return: Inserted node, its predecessor and successor
        :rtype: LinkedList object
        """
        pass

    @abstractmethod
    def shift(self):
        """
        Deletes a node from the beginning of the linked list, sets the new head to the successor of the deleted
        head node
        :return: the deleted node
        :rtype: Node
        """
        # check if the LinkedList is empty, return None
        if self.is_empty():
            return None

    @abstractmethod
    def pop(self) -> Optional[Node]:
        """
        Deletes the last node element from the LinkedList
        :return: Deleted node element
        :rtype: Node object
        """
        raise NotImplementedError("Not yet implemented")

    def delete_head(self) -> Union[Node, None]:
        """
        Delete the first node in the linked list
        """
        if self.head:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node
        else:
            return None

    @abstractmethod
    def delete_node(self, node: Node):
        """
        Finds the node from the linked list and deletes it from the LinkedList
        Moves the node's next to this node's previous link
        Moves this node's previous link to this node's next link
        :param node: Node element to be deleted
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete_node_at_position(self, position: int):
        """
        Deletes a node from the given provided position.
        :param position: Position of node to delete
        """
        if not 0 <= position <= len(self) - 1:
            raise ValueError(f"Position ${position} out of bounds")

        if self.head is None:
            return None

        # rest of the implementation is at the relevant subclasses

    @abstractmethod
    def delete_node_by_key(self, key: Any):
        """
        traverses the LinkedList until we find the data in a Node that matches and deletes that node. This uses the same
        approach as self.delete_node(node: Node) but instead of using the node to traverse the linked list, we use the
        data attribute of a node. Note that if there are duplicate Nodes in the LinkedList with the same data attributes
        only, the first Node is deleted.
        Args:
            key Any: Key of Node element to be deleted
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete_nodes_by_key(self, key: Any):
        """
        traverses the LinkedList until we find the key in a Node that matches and deletes those nodes. This uses the
        same approach as self.delete_node_by_key(key) but instead deletes multiple nodes with the same key
        Args:
            key Any: Key of Node elements to be deleted
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete_middle_node(self) -> Optional[Node]:
        """
        Deletes the middle node in the linked list and returns the deleted node
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete_nth_last_node(self, n: int) -> Optional[Node]:
        """
        Deletes the nth last node of the linked list and returns the head of the linked list.
        Example:
            n = 1
            43 -> 68 -> 11 -> 5 -> 69 -> 37 -> 70 -> None
            43 -> 68 -> 11 -> 5 -> 69 -> 37 -> None
        Args:
            n (int): the position from the last node of the node to delete
        Returns:
            Node: Head of the linked list
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def display(self):
        """
        Displays the whole of the LinkedList
        :return: LinkedList data structure
        """
        pass

    @abstractmethod
    def display_forward(self):
        """
        Display the complete list in a forward manner
        :return:The LinkedList displayed in 'ascending order' or in order of insertion
        """
        pass

    @abstractmethod
    def display_backward(self):
        """
        Display the complete list in a backward manner
        :return: The LinkedList displayed in 'descending order', not in the order of insertion
        """
        pass

    def has_cycle(self):
        """
        Detects if linked list has cycle, i.e. a node in the linked list points to a node already traversed.
        Will use Floyd-Cycle Detection algorithm to check for cycles. Will have a fast and slow pointer and check if
        the fast pointer
        catches up to the slow pointer. If this happens, there is a cycle. The fast pointer will move at twice the speed
        of slow pointer
        :return: True if there is a cycle, False otherwise
        :rtype: bool
        """
        fast_pointer = slow_pointer = self.head
        while fast_pointer and slow_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                return True
        return False

    def detect_node_with_cycle(self):
        """
        Detects the node with a cycle and returns it
        """
        if not self.has_cycle():
            return False
        else:
            slow_pointer = fast_pointer = self.head

            while fast_pointer and slow_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next

                if slow_pointer == fast_pointer:
                    break
            else:
                return None

            while self.head != slow_pointer:
                slow_pointer = slow_pointer.next
                self.head = self.head.next
            return self.head

    def remove_cycle(self):
        """
        Removes cycle if there exists. This will use the same concept as has_cycle method to check if there is a loop
        and remove the cycle
        if one is found.
        1) Detect Loop using Floyd’s Cycle detection algo and get the pointer to a loop node.
        2) Count the number of nodes in loop. Let the count be k.
        3) Fix one pointer to the head and another to kth node from head.
        4) Move both pointers at the same pace, they will meet at loop starting node.
        5) Get pointer to the last node of loop and make next of it as NULL.
        :return: True if the cycle has been removed, False otherwise
        :rtype: bool
        """
        fast_pointer = slow_pointer = self.head

        while fast_pointer and slow_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                pointer_1 = pointer_2 = slow_pointer

                # Count the number of nodes in loop
                k = 1
                while pointer_1.next != pointer_2:
                    pointer_1 = pointer_1.next
                    k += 1

            # Fix one pointer to head
            pointer_1 = self.head

            # And the other pointer to k nodes after head
            pointer_2 = self.head
            for _ in range(k):
                pointer_2 = pointer_2.next

            # Move both pointers at the same place
            # they will meet at loop starting node
            while pointer_2 != pointer_1:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next

            # Get pointer to the last node
            pointer_2 = pointer_2.next
            while pointer_2.next != pointer_1:
                pointer_2 = pointer_2.next

            # Set the next node of the loop ending node
            # to fix the loop
            pointer_2.next = None
            return True

        return False

    @abstractmethod
    def alternate_split(self):
        """
        Alternate split a linked list such that a linked list such as a->b->c->d->e becomes a->c->e->None and b->d->None
        """
        pass

    @abstractmethod
    def is_palindrome(self) -> bool:
        """
        Checks if the linked list is a Palndrome. That is, can be read from both back & front
        :return: boolean data. True if the LinkedList is a Palindrome
        """
        raise NotImplementedError("Method has not been implemented")

    def swap_nodes(self, data_one: Any, data_two: Any):
        """
        Swaps two nodes based on the data they contain. We search through the LinkedList looking for the data item in
        each node. Once the first is found, we keep track of it and move on until we find the next data item. Once that
        is found, we swap the two nodes' data items.

        If we can't find the first data item nor the second. No need to perform swap. If the 2 data items are similar
        no need to perform swap as well.

        If the LinkedList is empty (i.e. has no head node), return, no need to swap when we have no LinkedList :)
        """
        if not self.head:
            raise EmptyLinkedList("Empty LinkedList")

        # if they are the same, we do not need to swap
        if data_one == data_two:
            return

        # set the 2 pointers we will use to traverse the linked list
        current_one = self.head
        current_two = self.head

        # move the pointer down the LinkedList while the data item is not the same as the data item we are searching for
        while current_one and current_one.data != data_one:
            current_one = current_one.next

        # we look for the second data item
        while current_two and current_two.data != data_two:
            current_two = current_two.next

        # the data items do not exist in the LinkedList or only one of them exists, therefore we can not perform a swap
        if not current_one or not current_two:
            return

        # swap the data items of the nodes
        current_one.data, current_two.data = current_two.data, current_one.data

    @abstractmethod
    def pairwise_swap(self) -> Node:
        """
        Swaps nodes in a linked list in pairs.
        As there are different kinds of LinkedLists, it is up to the child class to implement this

        The premise(idea) is to swap the data of each node with the data of the next node. This is while using
        an iterative approach
        Example:
        1 -> 2 -> 3 -> 4
        becomes
        2 -> 1 -> 4 -> 3
        :return: New head of node
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def swap_nodes_at_kth_and_k_plus_1(self, k: int) -> Node:
        """
        Return the head of the linked list after swapping the datas of the kth node from the beginning and the kth node
        from the end (the list is 1-indexed).

        Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
        Output: [7,9,6,6,8,7,3,0,9,5]
        """
        raise NotImplementedError("Method has not been implemented")

    def get_kth_to_last_node(self, k: int) -> Optional[Node]:
        """
        Gets the kth to the last node in a Linked list.

        Assumptions:
        - k can not be an invalid integer, less than 0. A ValueError will be raised

        Algorithm:
        - set 2 pointers; fast_pointer & slow_pointer
        - Move fast_pointer k steps ahead
        - increment both pointers(fast_pointer & slow_pointer) until fast_pointer reaches end
        - return the slow_pointer

        Complexity Analysis:
        - Time Complexity O(n) where n is the number of nodes in the linked list to traverse
        - Space Complexity O(1). No extra space is needed

        @param k: integer value which will enable us to get the kth node from the end of the LinkedList
        @return: Kth node from the end
        @rtype: Node
        """
        if k < 0:
            raise ValueError("Invalid K value")
        if k > len(self):
            raise IndexError("K longer than linked list")
        fast_pointer, slow_pointer = self.head, self.head

        for _ in range(k - 1):
            fast_pointer = fast_pointer.next

            if not fast_pointer:
                return None

        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        return slow_pointer

    @abstractmethod
    def move_to_front(self, node: Node):
        """
        Moves a node from it's current position to the head of the linked list
        @param node:
        @return:
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def move_tail_to_head(self):
        """
        Moves the tail node to the head node making the tail node the new head of the linked list
        Uses two pointers where last pointer will be moved until it points to the last node in the linked list.
        The second pointer, previous, will point to the second last node in the linked list.

        Complexity Analysis:

        An assumption is made where n is the number of nodes in the linked list
        - Time: O(n) as the the pointers have to be moved through each node in the linked list until both point to the
        last and second last nodes in the linked list

        - Space O(1) as no extra space is incurred in the iteration. Only pointers are moved at the end to move the tail
         node to the head and make the second to last node the new tail
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def partition(self, data: Any) -> Union[Node, None]:
        """
        Partitions a LinkedList around a data point such that all nodes with values less than this data point come
        before all nodes greater than or equal to that data point

        Algorithm:
        - Create left & right LinkedLists
        - For each element/node in the linked list:
            - if element data < data:
                - append to the left list
            - if element data is equal to the data:
                - prepend to the right list
            - if element data is greater than the data:
                - append to the right list
        - Check if the left list is empty. Return right list if left is empty
        - Move the pointer of the left list up to the last node (O(n) operation)
        - set the next pointer of the last node in the left list to the head of the right list
        - return the head of the left list

        Complexity Analysis:
        - Space Complexity: O(n) - left & right lists to hold the partitions of the linked list with nodes n
        - Time Complexity: O(n) - where n is the number of nodes in the linked list

        @param data: Data point to compare nodes and create partitions
        @return: Head of the partitioned linked list
        @rtype: Node
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def remove_tail(self):
        """
        Remotes the tail of a linked list
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def remove_duplicates(self) -> Optional[Node]:
        """
        Remotes the duplicates from a linked list
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def rotate(self, k: int):
        """
        Rotates a linked list by k nodes
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def reverse_groups(self, k: int):
        """
        Reverses every k groups of a linked list
        """
        raise NotImplementedError("Not yet implemented")

    def middle_node(self) -> Optional[Node]:
        """
        Traverse the linked list to find the middle node
        Time Complexity: O(n) where n is the number of nodes in the linked list
        Space Complexity: O(1) as constant extra space is needed
        @return: Middle Node or None
        """
        if not self.head:
            return None

        fast_pointer, slow_pointer = self.head, self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

    @abstractmethod
    def odd_even_list(self) -> Optional[Node]:
        """
        Returns the odd even list where the even indexed nodes are grouped first and then the even indexed nodes
        @return: New head node
        """
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def maximum_pair_sum(self) -> int:
        """
        Returns the maximum twin sum of a node and its twin, where a node's twin is at the index (n-1-i) where n is the
        number of nodes in the linked list.
        For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only
        nodes with twins for n = 4.
        @return: maximum twin sum of a node and it's twin
        """
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def pairs_with_sum(self, target: T) -> List[Tuple[Node, Node]]:
        """
        Returns a list of tuples which contain nodes whose data sum equal the given target.
        Args:
            target T: the target with which each pair's data sums up to
        Return:
            List: list of pairs
        """
        raise NotImplementedError("not yet implemented")
