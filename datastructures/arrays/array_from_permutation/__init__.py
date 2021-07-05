from typing import List


def build_array(nums: List[int]) -> List[int]:
    return [nums[nums[x]] for x in range(len(nums))]
