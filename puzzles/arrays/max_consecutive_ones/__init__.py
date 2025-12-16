from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    left = right = 0

    for right in range(len(nums)):
        # if we encounter a 0 then we decrement k
        if nums[right] == 0:
            k -= 1

        # if k < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if k < 0:
            # if the left one was zero then we adjust K
            if nums[left] == 0:
                k += 1
            # regardless of whether we had a 1 or a 0 we can move left side by 1
            # if we keep seeing 1's the window still keeps moving as-is
            left += 1

    return right - left + 1


def find_max_consecutive_ones(nums: List[int]) -> int:
    """
    Finds the maximum consecutive ones in a binary array and returns it.

    The most straightforward way to solve this is to use a single pass through the array, keeping track of two values
    as we go. First, we need a counter for the current streak of consecutive 1s we're seeing. Second, we need to
    remember the maximum streak we've encountered so far.

    As we examine each element, if we see a 1, we increment our current streak counter. If we see a 0, that breaks our
    streak, so we reset the counter to 0. Importantly, every time we update our current streak, we check whether it's
    larger than our maximum and update the maximum if needed.

    Time complexity is O(n) where n is the length of the input array
    Space complexity is O(1) as no extra space is required

    Args:
        nums(list): a list of 1s and 0s.
    Returns:
        int: maximum number of consecutive 1s in the nums binary array
    """
    if len(nums) == 0:
        return 0
    max_ones = 0
    current_consecutive = 0

    for num in nums:
        if num == 1:
            current_consecutive += 1
            max_ones = max(max_ones, current_consecutive)
        else:
            current_consecutive = 0
    return max_ones
