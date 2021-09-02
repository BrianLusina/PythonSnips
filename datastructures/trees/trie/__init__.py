from collections import defaultdict
from typing import List


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]

            else:
                new_node = TrieNode(char)
                curr.children[char] = new_node
                curr = new_node

        curr.is_end = True

    def search(self, word: str) -> List[str]:
        curr = self.root

        if len(word) == 0:
            return []

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return []

        output = []

        def dfs(node: TrieNode, prefix: str) -> None:
            if node.is_end:
                output.append((prefix + node.char))

            for child in node.children.values():
                dfs(child, prefix + node.char)

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
