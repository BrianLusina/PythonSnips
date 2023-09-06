from typing import List


def find_min(nums: List[int]) -> int:
    """
    Finds the minimum from a rotated sorted array.
    @param nums: list of rotated sorted integers
    @return: minimum from list
    """
    left, right = 0, len(nums) - 1
    current_min = float("inf")

    while left < right:
        middle = (left + right) // 2
        current_min = min(current_min, nums[middle])

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle - 1

    return min(current_min, nums[left])
