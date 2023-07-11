from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    hash_table = dict()
    hash_set = set()

    for num in arr:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1
        hash_set.add(hash_table[num])

    return len(hash_set) == len(hash_table)
