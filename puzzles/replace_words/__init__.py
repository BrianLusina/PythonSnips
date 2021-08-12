import collections
from functools import reduce
from typing import List


def replace_words_with_prefix_hash(dictionary: List[str], sentence: str) -> str:
    """
    Replace words in a sentence with those in the dictionary based on the prefix match.

    Intuition:

    For each word in the sentence, we'll look at successive prefixes and see if we saw them before

    Algorithm:

    Store all roots in a set. Then for each word, look at successive prefixes for that word. If we find a prefix that is
    root, replace the word with that prefix. Otherwise, the prefix will just be the word itself, and we should add that
    to the final sentence

    Complexity Analysis:

    - Time Complexity: O(∑w i2) where wi is the length of the i-th word. We might check every prefix,
    the i-th of which is O(w_i^2) work.

    - Space Complexity: O(N) where N is the length of our sentence; the space used by root_set.

    @param dictionary: List of roots
    @param sentence: words separated by space to perform replacement on
    @return: New sentence with replaced words
    """
    root_set = set(dictionary)

    def replace(word: str) -> str:
        for x in range(1, len(word)):
            if word[:x] in root_set:
                return word[:x]
        return word

    return " ".join(map(replace, sentence.split()))


def replace_words_with_trie(dictionary: List[str], sentence: str) -> str:
    """
    Replace words in a sentence with those in the dictionary based on the prefix match.

    Intuition:

    Put all the roots in a trie (prefix tree). Then for any query word, we can find the smallest root that was a prefix
     in linear time.

    Complexity Analysis:

    - Time Complexity: O(N)O(N) where NN is the length of the sentence. Every query of a word is in linear time.

    - Space Complexity: O(N)O(N), the size of our trie.

    @param dictionary: List of roots
    @param sentence: words separated by space to perform replacement on
    @return: New sentence with replaced words
    """
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    end = True

    for root in dictionary:
        reduce(dict.__getitem__, root, trie)[end] = root

    def replace(word: str) -> str:
        cur = trie
        for letter in word:
            if letter not in cur or end in cur:
                break
            cur = cur[letter]
        return cur.get(end, word)

    return " ".join(map(replace, sentence.split()))
