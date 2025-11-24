from typing import Deque, List
from collections import deque
from datastructures.trees.trie import TrieNode


class StreamChecker(object):
    def __init__(self, words: List[str]):
        """
        Initializes a StreamChecker instance.

        Constructor Time: O(Ltotal), where Ltotal is the sum of the lengths of all words. This is a one-time cost.

        Parameters:
            words (List[str]): List of words to be checked in the stream.

        Returns:
            instance of streamchecker
        """
        self.words = words
        self.trie = TrieNode()
        self.max_len = 0
        self.__build_trie()
        # deque(maxlen) is key for stream history optimization
        self.stream: Deque[str] = deque(maxlen=self.max_len)

    def __build_trie(self):
        # insert the words in reverse order into the trie
        for word in self.words[::-1]:
            # 1. track max length for deque optimization
            if len(word) > self.max_len:
                self.max_len = len(word)

            current = self.trie
            # 2. insert characters in reverse order
            for letter in word[::-1]:
                current = current.children[letter]

            # 3. Mark the end of the reversed word
            current.is_end = True

    def query(self, letter: str) -> bool:
        """
        Query Time: O(L), where L is the length of the stream. This is because we only traverse the trie up to the
        length of the stream.

        Query Time: O(Lmax), where Lmax is the length of the longest word (up to 200). Since this is a constant limit,
        we can treat this as O(1) amortized time per query.

        Parameters:
            letter (str): The next letter in the stream.

        Returns:
            bool: True if the letter is the end of a word, False otherwise.
        """
        self.stream.append(letter)
        current = self.trie

        # Iterate stream in reverse (newest character first)
        for character in reversed(self.stream):
            # Check for dead-end (critical for query logic)
            if character not in current.children:
                return False

            # Traverse to the next node
            current = current.children[character]

            # check for match(success condition)
            if current.is_end:
                return True

        # If loop finishes without a match
        return False
