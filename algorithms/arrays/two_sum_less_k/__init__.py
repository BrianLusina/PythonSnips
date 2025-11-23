from typing import List


def two_sum_less_than_k(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of two elements in a given list of numbers that is less than k.
    Uses binary search to achieve a time complexity of O(n log n) and find the maximum sum of two elements
    that is less than k. It takes the nums array and the target value k as input.
    Args:
        nums (List[int]): A sorted list of integers
        k int: The target value to search for
    Returns:
        The maximum sum of two elements that is less than k
    """
    max_sum = -1

    # sort the numbers in ascending order to facilitate binary search
    nums.sort()

    for x in range(len(nums)):
        # find the maximum sum of two elements that is less than k, with the first element being nums[x]
        y = search(nums, k - nums[x], x + 1)
        if y > x:
            # update max_sum with the maximum sum found so far
            max_sum = max(max_sum, nums[x] + nums[y])

    return max_sum


def search(nums: List[int], target: int, start: int) -> int:
    """
    Searches for a number that is less than the target in a sorted list of numbers.
    Uses binary search to achieve a time complexity of O(log n) and find the index j such that the sum
    nums[i]+nums[j] < k. It takes the nums array, target value, and the start range of the search as input.
    Args:
        nums (List[int]): A sorted list of integers
        target int: The target value to search for
        start int: The starting index of the search range
    Returns:
        The index of the number that is less than the target, or -1 if no such number is found
    """
    left, right = start, len(nums) - 1
    result = -1

    while left <= right:
        # calculate the midpoint of the search range
        mid = (left + right) // 2
        if nums[mid] < target:
            # update result to mid and move left to mid + 1 to look for larger values.
            result = mid
            left = mid + 1
        else:
            # move right to mid - 1 to check smaller values.
            right = mid - 1

    return result
