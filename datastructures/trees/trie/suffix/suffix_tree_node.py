from typing import DefaultDict
from collections import defaultdict
from datastructures.trees.trie.trie_node import TrieNode
from datastructures.trees.trie.suffix.types import WordInfo, INF_WORD_INFO


class SuffixTreeNode(TrieNode):
    """
    This represents a node in our Suffix Trie structure.
    Each node stores its children and the index of the best word
    (shortest, earliest) that passes through this node.
    """

    def __init__(self):
        super().__init__()
        # index of best word passing through this node
        self.best_index = -1
        self.children: DefaultDict[str, SuffixTreeNode] = defaultdict(SuffixTreeNode)
        # Stores the best WordInfo (length, index) for any word that passes
        # through or ends at this node. Initialized to infinity.
        self.best_info: WordInfo = INF_WORD_INFO
