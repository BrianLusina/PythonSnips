from typing import List


def subset_xor_sum(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result |= num
    return result << (len(nums) - 1)
