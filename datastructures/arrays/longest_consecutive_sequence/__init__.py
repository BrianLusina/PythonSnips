from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Longest consecutive sequence finds the length of the longest consecutive sequence in a list of integers.
    Complexity:
    Time: O(n) where n is the length of the nums list
    Space: O(n) where n is the size of the set created to keep track of neighbours of each integer in the input list
    @param nums: list of integers
    @return: integer denoting the length of the longest consecutive sequence
    """
    num_set = set(nums)
    longest = 0

    for number in nums:
        if (number - 1) not in num_set:
            length = 0
            while (number + length) in num_set:
                length += 1
            longest = max(length, longest)

    return longest
