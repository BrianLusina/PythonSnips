from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    """
    Finds the maximum average in a sub array of length k from the provided list/array.

    Uses a sliding window to find the maximum average.
    This traverses over nums just once, and on the go keep determining the sums possible for the subarrays of length k.
    To understand the idea, assume that we already know the sum of elements from index i to index i+k, say it is
    current_sum.

    Now, to determine the sum of elements from the index i+1 to the index i+k+1, all we need to do is to subtract the
    element nums[i] from x and to add the element nums[i+k+1] to current_sum. We can carry out our process based on this
    idea and determine the maximum possible average.

    Complexity Analysis:
    - Time Complexity: O(n). Iterate over the given nums array of length n only once
    - Space Complexity: O(1). Constant extra space is used

    @param nums: List of integers
    @param k: Length of subarray
    @return: maximum average of subarray
    """
    if len(nums) <= 1:
        return sum(nums) / k

    current_sum = 0
    x = 0
    while x < k:
        current_sum += nums[x]
        x += 1

    current_max_sum = current_sum
    right = k

    while right < len(nums):
        current_sum += nums[right] - nums[right - k]
        current_max_sum = max(current_sum, current_max_sum)
        right += 1

    return current_max_sum / k
