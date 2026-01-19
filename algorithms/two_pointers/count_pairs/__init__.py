from typing import List


def count_pairs(nums: List[int], target: int) -> int:
    """
    Counts the number of pairs of numbers in a list that sum to a value less than a target.
    Uses a two-pointer approach to find the pairs, with a time complexity of O(n log n).
    Modifies the list in place to sort the numbers.
    Args:
        nums (List[int]): A list of integers
        target (int): The target value to search for
    Returns:
        int: The number of pairs of numbers in the list that sum to a value less than the target
    """
    # Get the length of the numbers
    n = len(nums)

    # Validation check, if there are less than 2 numbers, return 0. We can't form a pair here
    if n < 2:
        return 0

    # Sort the nums in place, this incurs a time complexity of O(n log n)
    nums.sort()

    # Initialize the left and right pointers
    left, right = 0, n - 1

    # Initialize the count of pairs
    count = 0

    # Use a while loop to find the pairs
    while left < right:
        # Get the current sum of the numbers at the left and right pointers
        current_sum = nums[left] + nums[right]
        # If the sum is less than the target, then the numbers in between the left and right pointers
        # form valid pairs with the left pointer
        if current_sum < target:
            # Count the pairs
            count += right - left
            # Move the pointer up to find other distinct pairs
            left += 1
        else:
            # move the pointer down to find other pairs, reducing the sum of the boundary
            right -= 1

    # Return the count of pairs
    return count
