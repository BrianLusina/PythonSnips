from typing import List


def count_subarrays(nums: List[int], min_k: int, max_k: int) -> int:
    """
    Counts the number of subarrays in the provided array which satisfies the following conditions:
    1. The smallest value in the subarray equals min_k.
    2. The largest value in the subarray equals max_k.

    Args:
        nums (List[int]): The array of integers.
        min_k (int): The minimum value in the subarray.
        max_k (int): The maximum value in the subarray.

    Returns:
        int: The number of subarrays that satisfies the conditions.
    """
    last_min, last_max, last_invalid = -1, -1, -1
    count = 0

    for i, num in enumerate(nums):
        if num == min_k:
            last_min = i
        if num == max_k:
            last_max = i
        if num < min_k or num > max_k:
            last_invalid = i

        count += max(0, min(last_min, last_max) - last_invalid)

    return count