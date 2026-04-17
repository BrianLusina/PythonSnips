from typing import List
from datastructures.trees.trie import Trie

def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    trie = Trie()

    for word in words:
        trie.insert(word)

    results = []

    # loop through each character in the text
    for idx, char in enumerate(text):
        # start from the root of the Trie for each character in the text
        node = trie.root

        # Check each possible substring starting from index idx
        for j in range(idx, len(text)):
            ch = text[j]
            # If the character is not in the current Trie Node's children, stop searching
            if ch not in node.children:
                break

            # Move to the next node in the Trie
            node = node.children[ch]

            # If we reach the end of a word, record the indices
            if node.is_end:
                results.append([idx, j])

    return results
