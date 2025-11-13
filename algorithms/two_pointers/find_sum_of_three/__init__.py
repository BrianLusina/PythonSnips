from typing import List
from copy import copy


def find_sum_of_three(nums: List[int], target: int) -> bool:
    """
    Checks if there are any three integers in nums whose sum is equal to the target
    Args:
        nums (list): list of integers
        target (int): target to equate to
    Returns:
        bool: True if there are three integers that sum up to target, False otherwise
    """
    # note that using a copy of the original array leads to unnecessary memory consumption
    numbers = copy(nums)
    # Sorts in place which incurs a Time complexity of O(nlog(n))
    numbers.sort()

    for idx, num in enumerate(numbers):
        if idx > 0 and num == numbers[idx - 1]:
            continue

        left, right = idx + 1, len(numbers) - 1

        while left < right:
            current_sum = num + numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return True

    return False
