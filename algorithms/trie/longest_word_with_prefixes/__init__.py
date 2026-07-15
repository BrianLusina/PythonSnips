from typing import List
from datastructures.trees.trie import TrieNode


def longest_word(words: List[str]) -> str:
    """
    Find the longest string in words such that every prefix of this string is also present in words.

    Time complexity
    Building the trie and validating all words takes O(∑∣wordi∣).

    Space complexity
    The trie stores, at most, one node per character, so the space is O(∑∣wordi∣)

    Args:
        words (List[str]): list of words
    Returns:
        str: longest word
    """
    if not words:
        return ""

    trie = TrieNode()

    for idx, word in enumerate(words):
        trie.insert(word, idx)

    result = ""
    for word in words:
        word_length = len(word)
        result_length = len(result)

        is_longer = word_length > result_length
        is_same_length_but_smaller = word_length == result_length and word < result

        if (is_longer or is_same_length_but_smaller) and trie.search(word):
            result = word

    return result
