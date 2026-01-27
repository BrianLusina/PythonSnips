"""
Finds the maximum sub-array in an array
"""

from typing import List

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
