from typing import List, Optional
from datastructures.trees.trie.trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: Optional[int] = None) -> None:
        """
        Inserts a word into the Trie. This has an optional index argument that allows
        us to track the index of the word in the original list. So, if inserting words from a list such as "The author
        is smart", the index of "smart" would be 3. If this is not provided, i.e. None, then each node in the tree will
        have an index of None. Note that for each character in the word, we update the index of the node to the index of
        the word. For example:

        sentence = "please playground player"

        Insert "please" (index 0):
            p(0) → l(0) → e(0) → a(0) → s(0) → e(0)

        Insert "playground" (index 1):
        p(0) → l(0) → a(1) → y(1) → g(1) → ...
                 ↘
                  e(0) → a(0) → s(0) → e(0)

        Insert "player" (index 2):
        p(0) → l(0) → a(1) → y(1) → ...
                              ↘
                               e(2) → r(2)

        The Index then tracks the earliest index of the word in the original list. So, for the example above, the index
        of "player" would be 2, not 0.

        Parameters:
            word (str): The word to insert
            index (Optional[int]): The index of the word (default is None)

        Returns:
            None
        """
        curr = self.root

        for char in word:
            curr = curr.children[char]
            if index is not None:
                curr.index = min(curr.index or float("inf"), index)

        curr.is_end = True

    def search(self, word: str) -> List[str]:
        if len(word) == 0:
            return []

        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return []

        output = []

        def dfs(node: TrieNode, prefix: str) -> None:
            if node.is_end:
                output.append((prefix + "".join(node.children.keys())))

            for child in node.children.values():
                dfs(child, prefix + "".join(node.children.keys()))

        dfs(curr, word[:-1])
        return output

    def starts_with(self, prefix: str) -> bool:
        """
        Returns true if the given prefix is a prefix of any word in the trie.
        """
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    def remove_characters(self, string_to_delete: str):
        """
        Removes a string from the trie
        """
        node = self.root
        child_list = []

        for c in string_to_delete:
            child_list.append([node, c])
            node = node.children[c]

        for pair in reversed(child_list):
            parent = pair[0]
            child_char = pair[1]
            target = parent.children[child_char]

            if target.children:
                return
            del parent.children[child_char]

    def __repr__(self):
        return f"Trie(root={self.root})"
