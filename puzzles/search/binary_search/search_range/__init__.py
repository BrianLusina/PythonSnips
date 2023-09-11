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
