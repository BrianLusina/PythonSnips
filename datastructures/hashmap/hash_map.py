from typing import Any, List
from datastructures.hashmap.bucket import Bucket


class HashMap:
    """
    Represents a HashMap/HashTable storing items by Key Value pairs
    """

    def __init__(self, key_space: int = 2069):
        """
        Creates an instance of a HashMap/HashTable
        Args:
            key_space (int, optional): The size of the key space. Defaults to 2069.
        """
        self.key_space: int = key_space
        self.buckets: List[Bucket] = [Bucket() for _ in range(key_space)]

    def __hash_function(self, key: int) -> int:
        """
        Hash Function used to calculate the key or where to place an item in the HashMap. This is a modulo operation
        of the key and the size of the HashMap
        Args:
            key (int): The key to hash
        Returns:
            int: The key or where to place an item in the HashMap
        """
        return key % self.key_space

    def set(self, key: int, value: Any) -> None:
        """
        Used to add an item to the HashMap/HashTable given it's unique Key and it's value. if the item is already in the
        HashMap, then an update to its value is performed.
        @param key: Key used to identify the item
        @param value: Represents the data of the Item
        """
        hash_key = self.__hash_function(key)
        self.buckets[hash_key].update(key, value)

    def get(self, key: int) -> Any:
        """
        Gets the Item from the HashMap/HashTable given its key if available. Will throw a KeyError if no such key exists
        Args:
            key (int): Key used to identify the item
        Raises:
            KeyError: If no such key exists
        Returns:
            Any: The Item from the HashMap
        """
        hash_key = self.__hash_function(key)
        return self.buckets[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes an item from the HashMap/HashTable given its key. Raises a Key error if the key does not exist.
        Args:
            key (int): Key used to identify the item
        Raises:
            KeyError: If no such key exists
        """
        hash_key = self.__hash_function(key)
        self.buckets[hash_key].remove(key)
