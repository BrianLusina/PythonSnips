from typing import Set, Counter
from collections import Counter


def num_jewels_in_stones_with_set(jewels: str, stones: str) -> int:
    # Store all jewel types for fast membership checking
    jewel_set: Set[str] = set(jewels)

    # Count how many stones are jewels
    count = 0

    # Check each stone and increment count if it's a jewel
    for ch in stones:
        if ch in jewel_set:
            count += 1

    # Return the total number of jewels found in stones
    return count


def num_jewels_in_stones_with_dict(jewels: str, stones: str) -> int:
    # Store all jewel types for fast membership checking
    stone_counts: Counter[str] = Counter(stones)

    # Count how many stones are jewels
    count = 0

    # Check each stone and increment count if it's a jewel
    for jewel in jewels:
        if jewel in stone_counts:
            count += stone_counts[jewel]

    # Return the total number of jewels found in stones
    return count
