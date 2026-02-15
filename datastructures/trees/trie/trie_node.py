from typing import DefaultDict, Optional
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
        self.index: Optional[int] = None

    def __repr__(self):
        return f"TrieNode(children={self.children.items()}, index={self.index}, is_end={self.is_end})"

    def insert(self, word: str, index: int):
        """
        Inserts a word into the TrieNode.

        Parameters:
            word (str): The word to insert
            index (int): The index of the word

        Returns:
            None
        """
        curr = self
        for char in word:
            curr = curr.children[char]
            curr.index = min(curr.index or float("inf"), index)
        curr.is_end = True

    def search_prefix(self, prefix: str) -> int:
        """
        Searches for a prefix in the TrieNode.

        Parameters:
            prefix (str): The prefix to search for

        Returns:
            int: The index of the word if the prefix is found, -1 otherwise
        """
        current = self

        for char in prefix:
            if char not in current.children:
                return -1

            # Traverse to the next node
            current = current.children[char]

        return current.index if current.index is not None else -1

    def search(self, word: str) -> bool:
        """
        Check if a word can be built character by character, where each prefix is also a word.

        Args:
            word: The word to search for

        Returns:
            True if every prefix of the word (including the word itself) exists as a complete word
        """
        current_node = self

        for char in word:
            # Move to the child node
            current_node = current_node.children[char]

            # Check if this prefix is a complete word
            if not current_node.is_end:
                return False

        return True
