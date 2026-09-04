"""
Finds the maximum sub-array in an array
"""

from typing import List
from math import inf

try:
    from collections import Iterable
except ImportError:
    from collections.abc import Iterable
try:
    from sys import maxsize as maxint
except ImportError:
    from sys import maxint


def find_max_sub_array(array: List[int]) -> int:
    """
    Finds the maximum sub-array in an array of integers
    Examples:
    >>> find_max_sub_array([1, 2, 3])
    6

    :param array: Array of numbers
    :type array list
    :return: Sum of sub-array that is the maximum of all sub-arrays
    :rtype: int
    """

    if array is None or not isinstance(array, Iterable):
        raise ValueError(f"Expected an iterable instead found {array}")

    if len(array) == 0:
        return 0

    max_so_far = -maxint - 1
    max_ending = 0

    for num in array:
        max_ending += num

        if max_so_far < max_ending:
            max_so_far = max_ending

        if max_ending < 0:
            max_ending = 0

    return max_so_far


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(current_sum, 0) + num

        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum_circular(nums: List[int]) -> int:
    # Initialize variables for tracking prefix sums
    # Minimum Prefix seen so far and maximum prefix seen so far
    min_prefix = 0
    max_prefix = -inf

    # Variables for tracking the minimum and maximum subarray sums
    # The maximum_subarray_sum using Kadane's algorithm
    # The current_sum is the running prefix sum
    # The minimum subarray sum
    max_subarray_sum = -inf
    current_sum = 0
    min_subarray_sum = inf

    # Iterate through each element in the array
    for num in nums:
        # Update the running prefix sum
        current_sum += num

        # Update the maximum subarray sum using Kadane's algorithm
        max_subarray_sum = max(max_subarray_sum, current_sum - min_prefix)

        # Update minimum subarray sum
        min_subarray_sum = min(min_subarray_sum, current_sum - max_prefix)

        # Update min and max prefix sums for next iteration
        min_prefix = min(min_prefix, current_sum)
        max_prefix = max(max_prefix, current_sum)

    # Return the maximum of:
    # 1. Maximum subarray sum(handles non-circular case)
    # 2. Total sum - minimum subarray sum(handles circular case)
    # The circular case works because removing the minimum subarray from the total gives us the maximum circular subarray
    return max(max_subarray_sum, current_sum - min_subarray_sum)


def max_subarray_sum_circular_2(nums: List[int]) -> int:
    # Initialize running totals for Kadane's max subarray
    cur_max = nums[0]
    best_max = nums[0]

    # Initialize running totals for Kadane's min subarray
    cur_min = nums[0]
    best_min = nums[0]

    # Track total sum of the array
    total_sum = nums[0]

    # Process remaining elements
    for i in range(1, len(nums)):
        num = nums[i]  # current value
        total_sum += num  # update total sum

        # Standard Kadane update for maximum subarray sum
        cur_max = max(num, cur_max + num)
        best_max = max(best_max, cur_max)

        # Kadane variant update for minimum subarray sum
        cur_min = min(num, cur_min + num)
        best_min = min(best_min, cur_min)

    # If all numbers are negative, wrapping would incorrectly give 0, so return bestMax
    if best_max < 0:
        return best_max

    # Best circular sum is either non-wrapping bestMax or wrapping totalSum - bestMin
    return max(best_max, total_sum - best_min)
