from typing import List


def find_all_subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    if n == 0:
        return []

    subsets = []

    def backtrack(first, curr):
        # Add the current subset to the output
        subsets.append(curr[:])
        # Generate subsets starting from the current index
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(0, [])
    return subsets
