from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    left = find_left_value(nums, target)
    right = find_right_value(nums, target)
    return [left, right]


def find_left_value(nums: List[int], target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target and mid - 1 >= 0:
                return mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def find_right_value(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target and mid + 1 < len(nums):
                return mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search_range_v2(nums: List[int], target: int) -> List[int]:
    def search(x: int):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    lower_bound = search(target)
    upper_bound = search(target + 1) - 1

    if lower_bound <= upper_bound:
        return [lower_bound, upper_bound]

    return [-1, -1]


def search_range_v3(nums: List[int], target: int) -> List[int]:
    """Searches for the left and right positions of a target in nums

    For the first_pos, we want to find the leftmost target. So we will do binary search on nums, and whenever we find
    a target, we search for its left side to see whether there is another target on the left while keeping track of the
    leftmost seen first_pos.

    Similarly, we want to find the rightmost target in nums to be last_pos. So when we see a target, we search for its
    right side and record the last_pos = current index. If the current element is not target, then ordinary binary
    search will lead us to the correct searching side.

    Args:
        nums(list): numbers to search
        target(int): target number

    Returns:
        list: array of length 2 with 1st index as the left position and last index as the right position
    """

    left, right = 0, len(nums) - 1
    first_pos, last_pos = -1, -1

    # find first position
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_pos = mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # find left position
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last_pos = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return [first_pos, last_pos]
