from typing import List


def next_permutation(nums: List[int]) -> None:
    """
    Does not return anything, modifies nums in-place instead.
    """
    # Start from the second last index (since we'll compare with the next element)
    i = len(nums) - 2

    # Step 1: Find the first decreasing element from the end
    # This identifies the pivot point where the sequence stops increasing
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1

    # Step 2: If such an element is found, find the next greater element to swap with
    if i >= 0:
        j = len(nums) - 1
        # Move from the end to find the first element greater than nums[i]
        while nums[j] <= nums[i]:
            j -= 1

        # Swap the pivot with the next greater element
        swap(nums, i, j)
    # Step 3: Reverse the suffix starting at i + 1 to get the smallest lexicographical order
    reverse(nums, i + 1)


# Helper function to reverse a portion of the list
def reverse(nums: List[int], start: int) -> None:
    i = start
    j = len(nums) - 1

    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1


# Helper function to swap two elements in the list
def swap(nums: List[int], i: int, j: int) -> None:
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
