from itertools import permutations
from typing import List


def find_permutation(word: str) -> List[str]:
    """
    Find all permutations of a word.
    >>> find_permutation('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    @param word: input word
    @return: lexicographically sorted list of permutations for given word
    """
    perms = set(permutations(word))
    return sorted(["".join(p) for p in perms])
