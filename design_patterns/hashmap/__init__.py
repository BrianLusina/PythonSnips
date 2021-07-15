from typing import Any, List


class Item(object):
    """
    Represents an item in the HashMap
    """

    def __init__(self, key: int, data: Any):
        """
        Creates an instance of an Item in the HashMap.
        @param key: Unique Key Identifier for this item in the HashMap
        @param data: Represents what's actually stored. This could be any data type
        """
        self.key = key
        self.data = data


class HashMap(object):
    """
    Represents a HashMap/HashTable storing items by Key Value pairs
    """

    def __init__(self, size: int):
        """
        Creates an instance of a HashMap/HashTable
        @param size: This represents the the size of the items to be stored.
        """
        self.size: int = size
        self.table: List[list] = [[] for _ in range(size)]

    def _hash_function(self, key: int) -> int:
        """
        Hash Function used to calculate the key or where to place an item in the HashMap. This is a modulo operation
        of the key and the size of the HashMap
        @param key: Key of the item
        @return:
        """
        return key % self.size

    def set(self, key: int, value: Any) -> None:
        """
        Used to add an item to the HashMap/HashTable given it's unique Key and it's value. if the item is already in the
        HashMap, then an update to its value is performed.
        @param key: Key used to identify the item
        @param value: Represents the data of the Item
        """
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.data = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key: int) -> Any:
        """
        Gets the Item from the HashMap/HashTable given its key if available. Will throw a KeyError if no such key exists
        @param key: Key to use to retrieve an item from the HashMap
        @return: Data item of the item
        @raise KeyError if the key does not exist
        """
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.data
        raise KeyError(f"Key {key} does not exist")

    def remove(self, key: int) -> None:
        """
        Removes an item from the HashMap/HashTable given its key. Raises a Key error if the key does not exist.
        @param key: key to use to retrieve the item and delete it
        @raise: KeyError
        """
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                self.table[hash_index].pop(index)
                return
        raise KeyError(f"Key {key} does not exist")
