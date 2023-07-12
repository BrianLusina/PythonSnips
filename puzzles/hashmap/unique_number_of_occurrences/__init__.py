from collections import defaultdict
from typing import List, DefaultDict


def unique_occurrences(arr: List[int]) -> bool:
    frequency_map: DefaultDict[int, int] = defaultdict(int)

    for num in arr:
        frequency_map[num] += 1

    frequency_set = set(frequency_map.values())

    return len(frequency_set) == len(frequency_map)
