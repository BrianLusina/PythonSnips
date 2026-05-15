from typing import List


def max_frequency(nums: List[int], k: int) -> int:
    """
    Returns the maximum possible frequency of a element after performing at most k operations
    Args:
        nums (List[int]): The list of numbers
        k (int): The number of frequencies to return.
    Returns:
        int: The largest frequency.
    """
    # Sort the nums first, this incurs a time complexity of O(n log(n)) and space complexity of O(n) due to the Timsort
    # algorithm used
    sorted_nums = sorted(nums)

    # left pointer of the window
    left = 0
    # Stores the maximum frequency found
    max_freq = 0
    # Sum of the elements within the current window
    window_sum = 0

    # expand the window by moving the right pointer
    for right in range(len(sorted_nums)):
        # Target element to make frequent
        target = sorted_nums[right]

        # Update the sum of elements in the window
        window_sum += target

        # Check if the total required increments exceed k
        while (right - left + 1) * target > window_sum + k:
            # Remove the leftmost element
            window_sum -= sorted_nums[left]

            # Shrink the window from the left
            left += 1

        # Update the maximum frequency found
        max_freq = max(max_freq, right - left + 1)

    return max_freq
