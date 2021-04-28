import sys
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """
    Uses 2 pointers to find the minimum length of the sub array whose sum is equal to or greater than the target.
    We could keep 2 pointer,one for the start and another for the end of the current subarray, and make optimal moves
    so as to keep the sum greater than ss as well as maintain the lowest size possible.

    Algorithm

    - Initialize left pointer to 0 and sum to 0
    - Iterate over the nums:
        - Add nums[i] to sum
        - While sum is greater than or equal to target:
            - Update ans = min(ans,i+1-left), where i+1-left is the size of current subarray
            - It means that the first index can safely be incremented, since, the minimum subarray starting with this
              index with sum≥target has been achieved
            - Subtract nums[left] from sum and increment left

    Complexity analysis

    Time complexity: O(n). Single iteration of O(n).
        Each element can be visited at most twice, once by the right pointer(i) and (at most) once by the left pointer.

    Space complexity: O(1) extra space. Only constant space required for left, sum, ans and i.

    :param target: The target value
    :param nums: List of integers
    :return: length of the sub array
    """
    ans = sys.maxsize
    size = len(nums)
    left = 0
    sum_ = 0

    if size == 0:
        return 0

    for x in range(size):
        sum_ += nums[x]

        while sum_ >= target:
            ans = min(ans, x + 1 - left)

            sum_ -= nums[left]
            left += 1

    return ans if ans != sys.maxsize else 0
