from typing import List
from datastructures.trees.trie import Trie


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    trie = Trie()

    for word in strs:
        trie.insert(word)

    def find_longest_common_prefix(trie_tree: Trie):
        prefix = ""
        node = trie_tree.root
        while node and not node.is_end and len(node.children) == 1:
            char, next_node = list(node.children.items())[0]
            prefix += char
            node = next_node
        return prefix

    return find_longest_common_prefix(trie)
