from typing import List, Optional
from datastructures.trees.trie.trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return f"Trie(root={self.root})"

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
        stripped_word = word.strip()

        for char in stripped_word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            if index is not None:
                if curr.index is None or index < curr.index:
                    curr.index = index
        curr.is_end = True

    def search_exact(self, word: str) -> bool:
        """
        Returns true if the exact word exists in the trie
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def get_completions(self, prefix: str) -> List[str]:
        if len(prefix) == 0:
            return []

        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        words = []

        self._dfs(curr, list(prefix), words)
        return words

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

    def get_all_words(self) -> List[str]:
        """
        Retrieves a list of all words in the trie
        """
        result: List[str] = []
        self._dfs(self.root, [], result)
        return result

    def _dfs(self, node: TrieNode, path: List[str], result: List[str]):
        """
        Helper method to traverse the trie
        Args:
            node (TrieNode): The node to traverse.
            path (List[str]): The list of characters building the current word
            result (List[str]): The resulting word
        """
        if node.is_end:
            result.append("".join(path))

        # sort keys if you want alphabetical order
        sorted_keys = sorted(node.children.keys())
        for char in sorted_keys:
            path.append(char)  # choose
            self._dfs(node.children[char], path, result)  # explore
            path.pop()  # backtrack

    def delete(self, word: str) -> bool:
        """Deletes a word from the trie. Returns True if successful."""

        def _delete_helper(node: TrieNode, w: str, depth: int) -> bool:
            if depth == len(w):
                if not node.is_end:
                    return False  # Word doesn't exist
                node.is_end = False
                return len(node.children) == 0  # Delete node if it has no children

            char = w[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete_helper(node.children[char], w, depth + 1)

            if should_delete_child:
                del node.children[char]
                # Return True if this node is not the end of another word and has no other children
                return not node.is_end and len(node.children) == 0
            return False

        return _delete_helper(self.root, word, 0)
