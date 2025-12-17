from typing import List, Optional


class AlphabetTrieNode:
    def __init__(self):
        self.children: List[Optional[AlphabetTrieNode]] = [None] * 26
        self.is_end_of_word: bool = False
