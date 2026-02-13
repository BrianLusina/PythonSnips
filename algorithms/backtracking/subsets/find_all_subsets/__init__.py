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


def find_all_subsets_with_duplicates(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    if n == 0:
        return []

    # Sort in place to ensure that duplicate elements are next to each other, which will be used to skip over the duplicate
    # elements in the iteration.
    # Time complexity here is O(n log(n)) and space complexity is O(n) due to Timsort requiring space to handle sorting
    # in place
    nums.sort()

    subsets: List[int] = []
    result: List[List[int]] = []

    def backtrack(idx: int) -> None:
        """
        Backtrack to create subsets from the given current index of the element being considered
        Args:
            idx(int): index of the element being considered.
        """
        # Base case, if we reach the end of the list, we include the current subset to the result
        if idx == n:
            result.append(subsets[:])
            return

        # Add the current subset to the output
        # Include the current element to the subset and move to the next element
        subsets.append(nums[idx])
        backtrack(idx + 1)
        # After recursion, remove it to backtrack and explore the excluded path
        subsets.pop()

        # Skip the current element(exclude path), but skip duplicates too. If there are duplicate elements, skip them all
        # when choosing exclude path. This ensures that we only take one unique subset for each duplicate group
        while idx + 1 < n and nums[idx] == nums[idx + 1]:
            idx += 1
        backtrack(idx + 1)

    backtrack(0)
    return result
