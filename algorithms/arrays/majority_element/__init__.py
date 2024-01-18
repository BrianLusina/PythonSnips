from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Finds the element that occurs more than n/2 times, where n is the size of the input list. This first sorts the
    list in place and finds the element at index n/2, since the majority element will always occupy the middle position
    when the array is sorted.

    Complexity:
    - Time Complexity O(n log(n)) since sorting an array of size n takes O(n log(n))) time
    - Space Complexity O(1) since no extra space is required
    Args:
        nums (list): list of integers
    Return:
        int: element that occurs the most in the list
    """
    nums.sort()
    n = len(nums)
    return nums[n // 2]
