import math
from typing import List


def find_min(nums: List[int]) -> int:
    """
    Finds the minimum from a rotated sorted array.
    @param nums: list of rotated sorted integers
    @return: minimum from list
    """
    left, right = 0, len(nums) - 1
    current_min = math.inf

    while left < right:
        middle = (left + right) // 2
        current_min = min(current_min, nums[middle])

        # if the middle element is greater than the last element, then the target is in the upper half
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle - 1

    return min(current_min, nums[left])


def find_min_with_duplicates(nums: List[int]) -> int:
    """
    Finds the minimum from a rotated sorted array which may contain duplicates
    """
    left, right = 0, len(nums) - 1
    while left < right:
        middle = left + (right - left) // 2
        if nums[middle] == nums[left] and nums[middle] == nums[right]:
            left += 1
            right -= 1
        elif nums[middle] <= nums[right]:
            right = middle
        else:
            left = middle + 1
    return nums[left]


def find_min_with_duplicates_2(nums: List[int]) -> int:
    # Set two pointers at the beginning and end of the array
    low, high = 0, len(nums) - 1

    # Iterate through the array as long as low is less than high
    while low < high:
        # Compute the middle index of the current range
        pivot = (low + high) // 2

        # If the element at pivot is less than the element at high,
        # shrink the search space by setting high = pivot
        if nums[pivot] < nums[high]:
            high = pivot

        # If the element at pivot is greater than the element at high,
        # update the low pointer to pivot + 1
        elif nums[pivot] > nums[high]:
            low = pivot + 1

        # If both values are equal, safely reduce the search space by shrinking high by one
        else:
            high -= 1

    # When the loop terminates, low points to the minimum element
    return nums[low]
