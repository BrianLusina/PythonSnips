import collections
from functools import reduce
from typing import List
from datastructures import Trie, TrieNode


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


def replace_words_with_trie_2(sentence: str, dictionary: List[str]) -> str:
    trie = Trie()

    # iterate over the prefixes in the dictionary and insert them into the trie
    for prefix in dictionary:
        trie.insert(prefix)

    # Store each of the word in the sentence in a new list
    word_list = sentence.split()

    # iterate over all the words in the list
    for idx in range(len(word_list)):

        def replace(root: TrieNode, word: str) -> str:
            """
            This replaces each word in the sentence with the smallest word from the dictionary
            """
            curr = root
            # iterate over each dictionary word along with the index of that character
            for i, char in enumerate(word):
                # If the character does not belong to the current node's children, then return the word
                if char not in curr.children:
                    return word

                # Move to the child of the current node corresponding to the current character
                curr = curr.children[char]

                # When the flag is_end becomes true, this means we have reached the end of the word in the trie. If this is
                # the case, then return this word
                if curr.is_end:
                    return word[: i + 1]

            return word

        # replace each word in the word_list with the shortest prefix from the trie
        word_list[idx] = replace(trie.root, word_list[idx])

    # After replacing each word with the shortest matching prefix, convert the list of words back to a single sentence.
    return " ".join(word_list)
