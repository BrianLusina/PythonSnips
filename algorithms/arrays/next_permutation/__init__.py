from typing import List


def next_permutation(nums: List[int]) -> None:
    """
    Does not return anything, modifies nums in-place instead.

    >>> next_permutation([1,2,3])
    [1,3,2]
    """
    i = len(nums) - 2

    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1

        while nums[j] <= nums[i]:
            j -= 1

        swap(nums, i, j)
    reverse(nums, i + 1)


def reverse(nums: List[int], start: int) -> None:
    i = start
    j = len(nums) - 1

    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1


def swap(nums: List[int], i: int, j: int) -> None:
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
