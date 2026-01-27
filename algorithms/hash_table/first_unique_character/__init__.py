from collections import Counter


def first_unique_character(s: str) -> int:
    frequency = Counter(s)

    for idx, letter in enumerate(s):
        if frequency[letter] == 1:
            return idx
    return -1
