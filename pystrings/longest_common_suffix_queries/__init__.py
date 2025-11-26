from typing import List
from datastructures.trees.trie import SuffixTree


def longest_common_suffix_queries(
    words_container: List[str], words_query: List[str]
) -> List[int]:
    trie = SuffixTree()

    # 1. Build the Trie from words_container
    for i, word in enumerate(words_container):
        trie.insert(word, i)

    # 2. Process all queries
    results = []
    for query_word in words_query:
        # Search the Trie and get the original index of the best match
        best_index = trie.search_best_index(query_word)
        results.append(best_index)

    return results
