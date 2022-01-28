import sys
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    d = dict()
    for i, n in enumerate(nums):
        if n in d and i - d[n] <= k:
            return True
        d[n] = i
    return False


def contains_nearby_almost_duplicate(nums: List[int], k: int, t: int) -> bool:
    if k < 1 or t < 0:
        return False
    d = dict()

    for idx, num in enumerate(nums):
        remapped_num = num - sys.maxsize
        bucket = remapped_num // (t + 1)

        if (bucket in d) \
                or ((bucket - 1) in d and remapped_num - d[bucket - 1] <= t) \
                or ((bucket + 1) in d and d[bucket + 1] - remapped_num <= t):
            return True

        if len(d) >= k:
            last_bucket = (nums[idx - k] - sys.maxsize) // (t + 1)
            del d[last_bucket]

        d[bucket] = remapped_num

    return False
