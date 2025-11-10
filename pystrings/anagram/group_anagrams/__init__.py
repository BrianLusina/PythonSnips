from typing import List, Dict, Tuple
from collections import defaultdict


def group_anagrams_naive(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings by their anagrams.

    Parameters:
        strs (List[str]): A list of strings

    Returns:
        List[List[str]]: A list of lists, where each inner list contains strings that are anagrams of each other
    """
    word_map: Dict[str, List[str]] = defaultdict(list)
    # traversing the list of strings takes O(n) time where n is the number of strings in this list
    for word in strs:
        # Note that the sorting here takes O(nlog(n)) time were n is the number of characters in this string
        key = "".join(sorted(word.lower()))
        word_map[key].append(word)

    return list(word_map.values())

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings by their anagrams.

    This uses A better approach than sorting can be used to solve this problem. This solution involves computing the
    frequency of each letter in every string. This will help reduce the time complexity of the given problem. We’ll just
    compute the frequency of every string and store the strings in their respective list in a hash map.

    We see that all members of each set are characterized by the same frequency of each letter. This means that the
    frequency of each letter in the words belonging to the same group is equal. In the set [["speed", "spede"]], the
    frequency of the characters s, p, e, and d are the same in each word.

    Let’s see how we can implement the above algorithm:

    - For each string, compute a 6-element list. Each element in this list represents the frequency of an English letter
     in the corresponding string. This frequency count will be represented as a tuple. For example, "abbccc" will be
     represented as (1, 2, 3, 0, 0, ..., 0). This mapping will generate identical lists for strings that are anagrams.

    - Use this list as a key to insert the strings into a hash map. All anagrams will be mapped to the same key in this
    hash map.

    - While traversing each string, we generate its 26-element list and check if this list is present as a key in the
    hash map. If it does, we'll append the string to the array corresponding to that key. Otherwise, we'll add the new
    key-value pair to the hash map.

    - Return the values of the hash map in a two-dimensional array, since each value will be an individual set of
    anagrams.

    Parameters:
        strs (List[str]): A list of strings

    Returns:
        List[List[str]]: A list of lists, where each inner list contains strings that are anagrams of each other
    """
    word_map: Dict[Tuple[int,...], List[str]] = defaultdict(list)
    # traversing the list of strings takes O(n) time where n is the number of strings in this list
    for word in strs:
        count = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1

        key = tuple(count)
        word_map[key].append(word)

    return list(word_map.values())
