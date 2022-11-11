from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Complexity Analysis:
    Time Complexity: O(nlogn) + O(n^2) = O(n^2) the O(nlogn) is due to sorting
    Space Complexity: O(1) as no extra space is taken up
    @param nums: input list of integers
    @return: lists of lists of integers
    """
    result = []
    # Time Complexity: O(nlogn)
    nums.sort()

    for idx, num in enumerate(nums):
        if idx > 0 and num == nums[idx - 1]:
            continue

        left, right = idx + 1, len(nums) - 1

        while left < right:
            sum_ = num + nums[left] + nums[right]
            if sum_ > 0:
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
