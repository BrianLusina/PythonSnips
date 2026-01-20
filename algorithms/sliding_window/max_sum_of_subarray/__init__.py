from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    n = len(nums)

    # If the length of the numbers is less than k, we return 0, as we can't get a contiguous subarray of size k from nums
    if n < k:
        return 0

    start = 0
    state = 0
    max_sum = float("-inf")

    for end in range(n):
        state += nums[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, state)
            state -= nums[start]
            start += 1

    return max_sum


def max_sum_subarray_2(nums: List[int], k: int) -> int:
    n = len(nums)

    # If the length of the numbers is less than k, we return 0, as we can't get a contiguous subarray of size k from nums
    if n < k:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum
    start = 0

    for end in range(k, n):
        window_sum += nums[end] - nums[start]
        start += 1
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_sum_subarray_3(nums: List[int], k: int) -> int:
    n = len(nums)

    # If the length of the numbers is less than k, we return 0, as we can't get a contiguous subarray of size k from nums
    if n < k:
        return 0

    # Use two points which will act as the boundary of the window. In this window, the sum of the elements will be
    # checked to get the max sum of the sub array
    lower_bound = 0
    upper_bound = k
    max_sum = 0

    while upper_bound <= n:
        current_sum = sum(nums[lower_bound:upper_bound])
        max_sum = max(current_sum, max_sum)
        lower_bound += 1
        upper_bound += 1

    return max_sum
