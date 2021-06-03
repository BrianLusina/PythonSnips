from datastructures.linked_lists.doubly_linked_list import DoublyLinkedList, DoubleNode


class LRUCache(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.lookup = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        """
        Gets an item from the cache.

        Complexity Analysis.
            Time Complexity: O(1)

        @param key:
        @return:
        """
        if key in self.lookup:
            node = self.lookup[key]
            result = node.data
            self.linked_list.delete_node(node)
            self.linked_list.prepend(node.data)
            return result

    def set(self, key, value):
        """
        Adds an item to the cache with the key and value

        Complexity Analysis.
            Time Complexity: O(1)

        @param key: Key to use
        @param value: Value of the item
        """
        node = self.lookup.get(key, None)

        if node:
            node.data = value
            self.linked_list.delete_node(node)
            self.linked_list.prepend(node.data)
        else:
            # key does not exist
            # if we are at max capacity
            if self.size == self.max_size:
                # remove oldest entry from linked list & Lookup
                self.lookup.pop(self.linked_list.tail.key, None)
                self.linked_list.remove_tail()
            else:
                self.size += 1
            new_node = DoubleNode(value)
            self.linked_list.prepend(new_node.data)
            self.lookup[key] = new_node
