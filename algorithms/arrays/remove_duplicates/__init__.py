from typing import List


def remove_duplicates(nums: List[int]) -> int:
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)
