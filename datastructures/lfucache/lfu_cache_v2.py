from collections import defaultdict
from typing import Any, Union, Dict

from datastructures.linked_lists.doubly_linked_list import DoublyLinkedList
from datastructures.lfucache.lfu_cache_node import LfuCacheNodeV2


class LFUCacheV2:
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
        self._lookup: Dict[Any, LfuCacheNodeV2] = dict()
        self._frequency_map: Dict[int, DoublyLinkedList] = defaultdict(DoublyLinkedList)
        self._minimum_frequency = 0

    # Helper function to maintain the order of the keys with respect to the frequency of their use
    def promote_key(self, key):
        node = self._lookup[key]

        # If the key is new
        if node.frequency == 0:
            node.frequency += 1
        else:
            # Detach the node from its current linked list
            empty = self._frequency_map[node.frequency].detach_node(node)

            # If the corresponding linked list becomes empty and current node is LFU
            if empty and self._minimum_frequency == node.frequency:
                self._minimum_frequency += 1

            node.frequency += 1

            # If the incremented frequency doesn't exist
            if node.frequency not in self._frequency_map:
                self._frequency_map[node.frequency] = DoublyLinkedList()

        # Insert the node at tail
        self._frequency_map[node.frequency].insert_at_tail(node)

    def get(self, key: int) -> Union[Any, None]:
        """
        Gets an item from the Cache given the key
        @param key: Key to use to fetch data from Cache
        @return: Data mapped to the key
        """
        if key not in self._lookup:
            return None

        self.promote_key(key)

        node = self._lookup[key]
        data = node.data
        # Return the value associated with the key
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

        # If the key exists
        if key in self._lookup:
            # Update it's value
            self._lookup[key].data = value
        else:
            # If the key does not exist
            # if the cache has reached its limit
            if len(self._lookup) == self.capacity:
                node = self._frequency_map[self._minimum_frequency].remove_head_node()
                del self._lookup[node.key]

            # Create new node
            node = LfuCacheNodeV2(data=value, key=key)
            self._lookup[key] = node
            self._minimum_frequency = 1

        self.promote_key(key)
        return None
