from datastructures.trees.trie.alphabet_trie.alphabet_trie_node import AlphabetTrieNode


class AlphabetTrie:
    def __init__(self):
        self.root = AlphabetTrieNode()

    def insert(self, word: str) -> None:
        if not word or not all("a" <= char.lower() <= "z" for char in word):
            raise ValueError("Word must contain only English letters (a-z)")
        node = self.root
        for char in word:
            index = ord(char.lower()) - ord("a")
            if not node.children[index]:
                node.children[index] = AlphabetTrieNode()
            node = node.children[index]
        node.is_end_of_word = True
