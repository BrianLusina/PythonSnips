from typing import List


def longest_subarray(nums: List[int]) -> int:
    longest_window = 0
    left = 0
    last_zero = -1

    for right in range(len(nums)):
        if nums[right] == 0:
            left = last_zero + 1
            last_zero = right

        longest_window = max(longest_window, right - left)

    return longest_window
