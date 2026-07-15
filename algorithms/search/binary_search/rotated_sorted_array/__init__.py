from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        # we search the left sorted portion
        if nums[left] <= nums[mid]:
            # if our target is greater than our middle value or less than the left most value, then we need to move our
            # left pointer to the middle plus 1, this means our target is in the right sorted portion
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                # if not, we move our right pointer to the middle. Meaning our target is in the left sorted portion
                right = mid - 1
        # right sorted portion
        else:
            # else our target is in the right sorted portion. We check if the target is less than our middle or our
            # target is greater than our right most value. Then we move to the left portion by moving our right pointer
            # to the middle value
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                # Move our left to the middle position if our target is greater than middle value or less than right
                # most value
                left = mid + 1

    return -1


def search_with_duplicates(nums: List[int], target: int) -> bool:
    """Performs a search of target in the nums list that is already sorted in non-decreasing order(that is increasing)
    & does not contain distinct values. Nums has been rotated at an unknown pivot index

    Args:
        nums(list): list of integers sorted in non-decreasing order with non-distinct values rotated at an unknown pivot
        target: number being sought for in nums.

    Return:
        bool: True if the target can be found in the nums list, False otherwise
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return True

        # We have failed to estimate which side is sorted, we move the right pointer back by 1 step
        if nums[mid] == nums[right]:
            right -= 1

        # we search the left sorted portion
        elif nums[left] <= nums[mid]:
            # if our target is greater than our middle value or less than the left most value, then we need to move our
            # left pointer to the middle plus 1, this means our target is in the right sorted portion
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                # if not, we move our right pointer to the middle. Meaning our target is in the left sorted portion
                right = mid - 1
        # right sorted portion
        else:
            # else our target is in the right sorted portion. We check if the target is less than our middle or our
            # target is greater than our right most value. Then we move to the left portion by moving our right pointer
            # to the middle value
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                # Move our left to the middle position if our target is greater than middle value or less than right
                # most value
                left = mid + 1

    return False
