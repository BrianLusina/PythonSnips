from typing import List, Optional
from collections import defaultdict, Counter
from datastructures.trees.trie import Trie


def top_k_frequent_words(words: List[str], k: int) -> List[str]:
    frequency_map = defaultdict(int)
    buckets: List[Optional[Trie]] = [None] * (len(words) + 1)
    top_k = []

    for word in words:
        frequency_map[word] += 1

    for word, frequency in frequency_map.items():
        if buckets[frequency] is None:
            buckets[frequency] = Trie()
        buckets[frequency].insert(word)

    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i] is not None:
            retrieve_words = buckets[i].get_all_words()
            if len(retrieve_words) < k:
                top_k.extend(retrieve_words)
                k -= len(retrieve_words)
            else:
                top_k.extend(retrieve_words[:k])
                break
    return top_k


def top_k_frequent_words_2(words: List[str], k: int) -> List[str]:
    word_freq = Counter(sorted(words))

    top_k = word_freq.most_common(k)

    return [w for w, c in top_k]
