from collections import defaultdict
from typing import Any, Union

from datastructures.linked_lists.doubly_linked_list import DoublyLinkedList, DoubleNode


class LFUCache:

    def __init__(self, capacity: int):
        """
        Initializes an instance of a LFUCache
        @param capacity: Capacity of the cache
        @type capacity int

        1. Dict named node self._lookup for retrieval of all nodes given a key. O(1) time to retrieve a node given a key
        2. Each frequency has a DoublyLinkedList stored in self._frequency where key is the frequency and value is an
        object of DoublyLinkedList
        3. minimum frequency through all nodes, this can be maintained in O(1) time, taking advantage of the fact that
        the frequency can only increment by 1. use the following 2 rules:
            i. Whenever we see the size of the DoublyLinkedList of current min frequency is 0, increment min_frequency
                by 1
            ii. Whenever we put in a new (key, value), the min frequency must be 1 (the new node)
        """
        self.capacity = capacity
        self._current_size = 0
        self._lookup = dict()
        self._frequency = defaultdict(DoublyLinkedList)
        self._minimum_frequency = 0

    def __update(self, node: DoubleNode):
        """
        Helper function used in 2 cases:
            1. When get(key) is called
            2. When put(key, value) is called and key exists

        Common point of the 2 cases:
            1. no new node comes in
            2. node is visited one more time -> node.frequency changed -> thus the place of this node will change

        Logic:
            1. Pop node from 'old' DoublyLinkedList with frequency
            2. Append node to 'new' DoublyLinkedList with frequency + 1
            3. If 'old' DoublyLinkedList has size 0 & self.minimum_frequency is frequency, update self.minimum_frequency
                to frequency + 1

        Complexity Analysis:
            Time Complexity: O(1) time

        @param node: Node to update in the Cache
        @type node DoubleNode
        """
        frequency = node.frequency

        # pop the node from the 'old' DoublyLinkedList
        self._frequency[frequency].delete_node(node)

        if self._minimum_frequency == frequency and not self._frequency[frequency]:
            self._minimum_frequency += 1

        node.frequency += 1
        frequency = node.frequency

        # add to 'new' DoublyLinkedList with new frequency
        self._frequency[frequency].prepend(node)

    def get(self, key: int) -> Union[Any, None]:
        """
        Gets an item from the Cache given the key
        @param key: Key to use to fetch data from Cache
        @return: Data mapped to the key
        """
        if key not in self._lookup:
            return None

        node = self._lookup[key]
        data = node.data
        self.__update(node)
        return data

    def put(self, key: int, value: Any) -> None:
        """
        If key is already present in the self._lookup, we perform same operations as get, except updating the node data
        to new value

        Otherwise, below operations are performed:
        1. If cache reaches capacity, pop least frequently used item.
            2 Facts:
            a. we maintain self._minimum_frequency, minimum possible frequency in cache
            b. All cache with the same frequency are stored as a DoublyLinkedList, with recently used order (Always
                append to head).

            Consequence is that the tail of the DoublyLinkedList with self._minimum_frequency is the least recently used
            one, pop it.

        2. Add new node to self._lookup
        3. add new node to DoublyLinkedList with frequency of 1
        4. reset minimum_frequency to 1

        @param key: Key to use for lookup
        @param value: Value to store in the cache
        @return: None
        """

        if self.capacity == 0:
            return None

        if key in self._lookup:
            node = self._lookup[key]
            self.__update(node)
            node.data = value
        else:
            if self._current_size == self.capacity:
                node = self._frequency[self._minimum_frequency].pop()
                self._lookup.pop(node.key)
                self._current_size -= 1

            node = DoubleNode(data=value, key=key)
            self._lookup[key] = node
            self._frequency[1].append(node)
            self._minimum_frequency = 1
            self._current_size += 1
