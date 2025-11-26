from datastructures.trees.trie.suffix.suffix_tree_node import SuffixTreeNode
from datastructures.trees.trie.suffix.types import WordInfo


class SuffixTree:
    """
    A suffix tree is a Trie that checks on suffixes of words instead of prefixes. This has been modified to meet the needs
    of checking for suffixes of words that have a best match.

    Basically, this is a Trie optimized for suffix matching by storing reversed strings.
    Each node tracks the best candidate word for tie-breaking.
    """
    def __init__(self):
        super().__init__()
        self.root = SuffixTreeNode()

    @staticmethod
    def _update_best_info(current_info: WordInfo, new_info: WordInfo) -> WordInfo:
        """
        Applies the tie-breaking rules to select the better WordInfo.

        Rules: 1. Smallest length wins. 2. Earliest index wins if lengths are equal.
        """
        new_length, new_index = new_info
        current_length, current_index = current_info

        if new_length < current_length:
            return new_info
        elif new_length == current_length and new_index < current_index:
            return new_info
        return current_info

    def insert(self, word: str, original_index: int):
        """Inserts a reversed word and updates best_info along the path."""
        # The length of the original word is the primary sorting key
        original_length = len(word)
        new_info: WordInfo = (original_length, original_index)

        node = self.root

        # Update the root's best_info first, as every word passes through it
        node.best_info = self._update_best_info(node.best_info, new_info)

        # Insert the *reversed* word
        reversed_word = word[::-1]

        for char in reversed_word:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]

            # Update best_info for the current node
            node.best_info = self._update_best_info(node.best_info, new_info)

    def search_best_index(self, query_word: str) -> int:
        """
        Finds the index of the best match for the query word.

        The best match will be stored in the TrieNode that represents the
        longest common *prefix* of the reversed query and any reversed container word.
        """
        # Search using the reversed query word
        reversed_query = query_word[::-1]
        node = self.root

        # Initialize the result with the info from the root
        # This covers the case where the longest common suffix is the empty string
        # which means the best word overall must be chosen (which is stored at the root).
        best_match_info = self.root.best_info

        for char in reversed_query:
            if char in node.children:
                node = node.children[char]
                # Any node reached represents a longer common suffix, so its
                # best_info is the current best overall match found so far
                best_match_info = node.best_info
            else:
                # No more characters match, the longest common prefix/suffix is found
                break

        # best_match_info is guaranteed to hold the best candidate due to the
        # update logic during insertion.
        # We return the original index stored in the info.
        return best_match_info[1]
