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
