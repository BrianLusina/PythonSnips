from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    result = [1] * len(nums)
    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
