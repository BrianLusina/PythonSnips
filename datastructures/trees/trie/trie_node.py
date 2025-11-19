from typing import DefaultDict
from collections import defaultdict


class TrieNode:
    def __init__(self):
        # self.char = char
        """
        Initializes a TrieNode instance.

        A TrieNode contains a character and a dictionary of its children. It also contains a boolean indicating whether the node is the end of a word in the Trie.

        Parameters:
            None

        Returns:
            None
        """
        self.children: DefaultDict[str, TrieNode] = defaultdict(TrieNode)
        self.is_end = False

    def __repr__(self):
        return f"TrieNode({self.children.items()}, {self.is_end})"
