from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Complexity Analysis:
    Ww assume that n is the length of the input array

    Time Complexity: O(nlog(n)) + O(n^2) = O(n^2) the O(nlog(n)) is due to sorting, overall, the time complexity is O(n²).
    This is due to the nested loops in the algorithm. We perform n iterations of the outer loop, and each iteration
    takes O(n) time to use the two-pointer technique.

    Space Complexity: O(n²) as no extra space is taken up. We need to store all distinct triplets that sum to 0, which
    can be at most O(n²) triplets.

    Args:
        nums (list): input list of integers
    Return:
        list: list of lists of integers
    """
    result = []
    # Time Complexity: O(nlog(n)) sorting in place. This may incur space complexity of O(n) due to Python's timesort
    # using temporary storage to handle the in place sorting
    nums.sort()

    for idx, num in enumerate(nums):
        # Increment to avoid duplicates
        if idx > 0 and num == nums[idx - 1]:
            continue

        left, right = idx + 1, len(nums) - 1

        while left < right:
            total = num + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                # add the triplet
                result.append([num, nums[left], nums[right]])

                # move the left pointer to avoid duplicates while it is still less than the right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
