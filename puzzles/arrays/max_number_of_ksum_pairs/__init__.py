from typing import List
from collections import defaultdict


def max_operations(nums: List[int], k: int) -> int:
    """
    Finds the maximum number of operations that are required to find the 2 numbers that sum up to k.

    First the list is sorted in place(this is the assumption used, that it is allowed to sort the input list in place.).
    Once the list is sorted, the 2 pointers can be placed at both ends

    Uses 2 pointers to find 2 elements that sum up to K. First sorting is done. This allows us to move either left or
    right pointer along the list based off the sum of the 2 elements. The left pointer is at the beginning of the list
    while the right pointer is at the end of the list.

    If the sum of these 2 elements is equal to k, we move the left pointer to the right and the right pointer to the left
    If they meet, then we can exit the loop as we have found all the possible combinations of 2 elements that can sum
    up to k.

    If the current sum of the 2 elements are less than k, then we move the left pointer to the right, this is because
    increasing the left pointer gives us a higher chance to find another element that we can sum with the right pointer
    to find k. The reverse is true, if the sum is greater than k, then we move the right pointer as reducing this number
    allows us to find an element that we can add to the left pointer to find k.

    Complexity:
    Time: O(nlogn), this is because we have to first sort the input list
    Space: O(1), no extra space is used in this operation as the list is sorted in place. If sorting in place is not
    allowed, then this will become O(n) where n is the size of the elements in the list as the algorithm will have to
    allocate extra memory to another collection that can be sorted.
    @param nums:
    @param k:
    @return:
    """
    if len(nums) <= 1:
        return 0

    nums.sort()

    left, right = 0, len(nums) - 1
    operations = 0

    while left < right:
        current = nums[left] + nums[right]
        if current == k:
            operations += 1
            left += 1
            right -= 1
        elif current < k:
            left += 1
        else:
            right -= 1

    return operations


def max_operations_with_hashmap(nums: List[int], k: int) -> int:
    if len(nums) <= 1:
        return 0

    seen = defaultdict(int)

    operations = 0

    for num in nums:
        x = k - num
        if seen[x] > 0:
            operations += 1
            seen[x] -= 1
        else:
            seen[num] += 1

    return operations
