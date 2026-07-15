from typing import Dict
from collections import Counter

from datastructures.trees.trie import TrieNode


class MapSumBruteForce(object):
    """
    This solution to creating a map sum data structure that finds the sum of keys with a matching prefix uses a
    Hash Table combined with Brute-Force Search and String Matching.

    Time Complexity: Every insert operation is O(1). Every sum operation is O(N*P) where N is the number of items in the
    map, and P is the length of the input prefix.

    Space Complexity: The space used by map is linear in the size of all input key and val values combined.
    """

    def __init__(self):
        self.mapping: Dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        """
        Inserts the key with the given value into the hash table
        Args:
            key (str): key to insert
            val (int): value to insert
        """
        self.mapping[key] = val

    def sum(self, prefix: str) -> int:
        """
        Finds the sum of all keys with the prefix `prefix`.
        Args:
            prefix (str): prefix to search for
        Returns:
            int: sum of all keys with the prefix `prefix`
        """
        running_sum = 0
        for k, v in self.mapping.items():
            if k.startswith(prefix):
                running_sum += v

        return running_sum


class MapSumPrefix(object):
    """
    We can remember the answer for all possible prefixes in a HashMap score. When we get a new (key, val) pair, we
    update every prefix of key appropriately: each prefix will be changed by delta = val - map[key], where map is the
    previously associated value of key (zero if undefined.)

    Time Complexity: Every insert operation is O(K^2), where K is the length of the key, as K strings are made of an
    average length of K. Every sum operation is O(1).

    Space Complexity: The space used by map is linear in the size of all input key and val values combined.
    """

    def __init__(self):
        self.mapping: Dict[str, int] = {}
        self.score = Counter()

    def insert(self, key: str, val: int) -> None:
        """
        Inserts the key with the given value into the hash table
        Args:
            key (str): key to insert
            val (int): value to insert
        """
        delta = val - self.mapping.get(key, 0)
        self.mapping[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix: str) -> int:
        """
        Finds the sum of all keys with the prefix `prefix`.
        Args:
            prefix (str): prefix to search for
        Returns:
            int: sum of all keys with the prefix `prefix`
        """
        return self.score[prefix]


class MapSumTrie(object):
    """
    Since we are dealing with prefixes, a Trie (prefix tree) is a natural data structure to approach this problem. For
    every node of the trie corresponding to some prefix, we will remember the desired answer (score) and store it at
    this node. As in the approach of using a prefix has map, this involves modifying each node by delta = val - map[key].

    Time Complexity: Every insert operation is O(K), where K is the length of the key. Every sum operation is O(K).
    Space Complexity: The space used is linear in the size of the total input.
    """

    def __init__(self):
        self.mapping: Dict[str, int] = {}
        self.score = Counter()
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        """
        Inserts the key with the given value into the hash table
        Args:
            key (str): key to insert
            val (int): value to insert
        """
        delta = val - self.mapping.get(key, 0)
        self.mapping[key] = val
        current = self.root
        current.score += delta
        for char in key:
            current = current.children[char]
            current.score += delta

    def sum(self, prefix: str) -> int:
        """
        Finds the sum of all keys with the prefix `prefix`.
        Args:
            prefix (str): prefix to search for
        Returns:
            int: sum of all keys with the prefix `prefix`
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.score
