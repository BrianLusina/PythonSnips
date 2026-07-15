import sys
from typing import List, Set


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    """
    Checks if there are any duplicate elements within k steps of each other
    in the given list of numbers.

    Args:
        nums (List[int]): The list of numbers to check.
        k (int): The maximum number of steps between duplicate elements.

    Returns:
        bool: True if there are any duplicate elements within k steps of each other, False otherwise.
    """
    # Dictionary to store the indices of the numbers we have seen so far
    d = dict()
    for i, n in enumerate(nums):
        # If we have seen this number before and it is within k steps of the current position
        if n in d and i - d[n] <= k:
            return True
        # Store the index of the current number
        d[n] = i
    # If we have not found any duplicate elements within k steps of each other
    return False


def contains_nearby_duplicates_2(nums: List[int], k: int) -> bool:
    """
    Checks if there are any duplicate elements within k steps of each other
    in the given list of numbers.

    Args:
        nums (List[int]): The list of numbers to check.
        k (int): The maximum number of steps between duplicate elements.

    Returns:
        bool: True if there are any duplicate elements within k steps of each other, False otherwise.
    """
    # Set to store the numbers we have seen so far
    seen: Set[int] = set()
    # Iterate over the list of numbers
    for idx in range(len(nums)):
        # If we have seen this number before
        if nums[idx] in seen:
            # Return True
            return True
        # Add the current number to the set of seen numbers
        seen.add(nums[idx])

        # If we have seen more than k numbers
        if len(seen) > k:
            # Remove the number that is k steps behind the current number
            seen.remove(nums[idx - k])

    # If we have not found any duplicate elements within k steps of each other
    return False


def contains_nearby_almost_duplicate(nums: List[int], k: int, t: int) -> bool:
    if k < 1 or t < 0:
        return False
    d = dict()

    for idx, num in enumerate(nums):
        remapped_num = num - sys.maxsize
        bucket = remapped_num // (t + 1)

        if (
            (bucket in d)
            or ((bucket - 1) in d and remapped_num - d[bucket - 1] <= t)
            or ((bucket + 1) in d and d[bucket + 1] - remapped_num <= t)
        ):
            return True

        if len(d) >= k:
            last_bucket = (nums[idx - k] - sys.maxsize) // (t + 1)
            del d[last_bucket]

        d[bucket] = remapped_num

    return False
