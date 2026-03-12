from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    piles = []

    for num in nums:
        left, right = 0, len(piles)

        while left < right:
            middle = left + (right - left) // 2
            if num > piles[middle]:
                left = middle + 1
            else:
                right = middle

        if left < len(piles):
            piles[left] = num
        else:
            piles.append(num)

    return len(piles)


def find_number_of_lis(nums: List[int]) -> int:
    n = len(nums)
    # length[i]: length of the LIS ending at i
    # count[i]: number of LIS of that length ending at i
    length = [1] * n
    count = [1] * n

    # Try to build LIS ending at each index i
    for i in range(n):
        # Check all previous positions j < i
        for j in range(i):
            # Can nums[i] extend an increasing subsequence from j?
            if nums[j] < nums[i]:
                # Found a strictly longer subsequence ending at i
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    # inherit all ways ending at j
                    count[i] = 0
                # Found another way to reach the same LIS length at i
                if length[j] + 1 == length[i]:
                    # accumulate all valid paths
                    count[i] += count[j]

    # Update global maximum LIS length
    max_length = max(length)
    result = 0

    # Sum counts of all positions that achieve the LIS length
    for i in range(n):
        if length[i] == max_length:
            result += count[i]
    # total number of longest increasing subsequences
    return result
