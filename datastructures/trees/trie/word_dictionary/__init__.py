from typing import List

# from datastructures.trees.trie.word_dictionary.word_dictionary_trie_node import WordDictionaryTrieNode
from datastructures.trees.trie.trie_node import TrieNode


class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()
        self.words: List[str] = []

    def add_word(self, word: str) -> None:
        if not word:
            return

        self.words.append(word)
        self.trie.insert(word)

    def search_word(self, word: str) -> bool:
        result = False

        def dfs(node: TrieNode, w: str):
            nonlocal result
            if len(w) == 0:
                if node.is_end:
                    result = True
                return

            if w[0] == ".":
                for child in node.children.values():
                    dfs(child, w[1:])
            else:
                node = node.children[w[0]]
                if not node:
                    return
                dfs(node, w[1:])

        dfs(self.trie, word)
        return result

    def get_words(self) -> List[str]:
        return self.words
