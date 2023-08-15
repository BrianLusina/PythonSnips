from typing import List, Dict
from math import ceil
from collections import defaultdict
from .. import T


class BTreeNode:
    def __init__(self, degree=3, leaf=False):
        """
        Creates a BTree Node of degree 'm'
        @param degree: The maximum number of children in a node
        @param leaf:
        """
        self.leaf = leaf
        self.degree = degree

        self.children: Dict[int, BTreeNode] = defaultdict()
        self.min_children = ceil(self.degree / 2)

        self.keys: Dict[int, T] = defaultdict()
        self.max_keys = self.degree - 1
        self.min_keys = ceil((self.degree / 2) - 1)

    def add_key(self, key: T):
        """
        Adds a key to the node at index 0. Raises an exception if there is a key at that index
        @param key: Key to add
        """
        self.__validate_key_size(key)
        self.add_key_at(key=key, index=0)

    def add_key_at(self, key: T, index: int):
        """
        Adds a key to the node at a given index
        @param key: Key to add
        @param index: position to add key
        """
        self.__validate_key_size(key)

        key_at_index_exists = self.keys.get(index, None)
        if key_at_index_exists:
            raise Exception(f"Key at index {index} already exists")

        self.keys[key] = index

    def remove_key(self, key: T) -> T:
        """
        Removes a key from the node and returns it
        @param key: Key to remove
        @return: Key to remove
        """
        if len(self.keys) == self.min_keys:
            raise Exception(f"Deleting key {key} from {self} will violate minimum keys of this node.")

        key_exists = self.keys.get(key, False)
        if not key_exists:
            raise Exception(f"Key {key} does not exist on node")

        data = self.keys.pop(key)
        return data

    def add_child(self, node: 'BTreeNode'):
        """
        Adds a child to the list of children on this node
        @param node to add as a child to this node
        """
        if len(self.children) == self.degree:
            raise Exception("Node has maximum children already")
        self.children.append(node)

    def __validate_key_size(self, key: T):
        if len(self.keys) == self.max_keys:
            raise Exception(f"Adding key {key} to {self} will violate maximum keys of this node.")
