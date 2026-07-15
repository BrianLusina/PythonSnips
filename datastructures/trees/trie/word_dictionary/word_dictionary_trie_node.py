from typing import List, Optional
from datastructures.trees.trie.trie_node import TrieNode


class WordDictionaryTrieNode(TrieNode):
    def __init__(self):
        super().__init__()
        self.children: List[Optional[TrieNode]] = []
        # Create 26 child nodes for each letter of alphabet
        for i in range(0, 26):
            self.children.append(None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.children})"
