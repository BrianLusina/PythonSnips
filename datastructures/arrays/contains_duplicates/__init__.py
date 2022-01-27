from typing import List

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    d = dict()
    for i, n in enumerate(nums):
        if n in d and i - d[n] <= k:
            return True
        d[n] = i
    return False
