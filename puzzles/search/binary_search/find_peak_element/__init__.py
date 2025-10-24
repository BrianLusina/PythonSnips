from typing import List, Optional


def find_peak_element(nums: List[int]) -> Optional[int]:
    """Finds a peak element's index in the provided list of integers

    Algorithm:
    - Initializes left as the start index of the list and right as the end index of the list (len(nums)- 1).
    - Perform binary search until left becomes equal to right.
    - Calculate the middle index mid using the formula mid = left + (right - left) // 2. or mid = (left + right) >> 1
    - Compare nums[mid] with nums[mid + 1] to determine if the peak is on the left side or the right side of mid.
        - If nums[mid] is greater than nums[mid + 1], move the right index to mid, indicating that the peak is on the
        left side.
        - Otherwise, move the left index to mid + 1, indicating that the peak is on the right side.
    - Repeat steps 3-4 until left becomes equal to right.
    - Return the value of peak_index, which represents the index of the peak element.

    Complexity:

    - Time complexity O(log n): Where n is the number of elements in the nums vector.
    - Space Complexity O(1): Since it uses a constant amount of extra space.

    Args:
        nums (List): list of integers
    Returns:
        int: index of a peak element(i.e. element that is greater than its adjacent neighbours)
    """
    # we require at least 3 numbers to form a bitonic peak
    if len(nums) < 3:
        return None

    left = 0
    right = len(nums) - 1
    peak_index = -1

    while left <= right:
        mid = (left + right) >> 1

        # check that the potential peak element is within bounds or is greater than both its neighbours. The
        # `mid==len(nums)-1` check is to ensure we are not at the end of the list. The potential_peak > nums[mid + 1]
        # checks if the peak is greater than the next number. If either condition evaluates to true, the peak index is
        # set to the middle and the right boundary is moved to the middle minus 1, this removes the right half
        potential_peak = nums[mid]
        if mid == len(nums) - 1 or potential_peak > nums[mid + 1]:
            peak_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return peak_index


def find_bitonic_peak(nums: List[int]) -> Optional[int]:
    """
    Finds the bitonic peak or the peak element in a list of numbers. A bitonic peak is an integer whose value is greater
    thant its neighbours on both the immediate left and the immediate right.

    Complexity:

    - Time complexity O(log n): Where n is the number of elements in the nums vector.
    - Space Complexity O(1): Since it uses a constant amount of extra space.

    Args:
        nums (List): list of integers
    Returns:
        int: index of a peak element(i.e. element that is greater than its adjacent neighbours)
    """
    # we require at least 3 numbers to form a bitonic peak
    if len(nums) < 3:
        return None

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) >> 1

        # we assign the mid_left and mid_right based on the middle index. If the middle index - 1(i.e. left of the middle
        # is greater than or equal to 0, we assign that value to mid_left, else we assign it a negative infinity value.
        # the negative infinity indicates that the value is out of bounds of the list.
        # On the other hand, if the middle index + 1 (i.e. the right of the middle index) is less than the length of the
        # list, then we assign it that value to the mid_right. If not, we give the mid_right a value of positive infinity
        # indicating that this is out of bounds of the list
        mid_left = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
        mid_right = nums[mid + 1] if mid + 1 < len(nums) else float("inf")

        # if the mid_left is less than the middle value and the mid_right is greater than the middle value, we move the
        # left pointer to 1 value greater than the middle index
        if mid_left < nums[mid] < mid_right:
            left = mid + 1
        elif mid_left > nums[mid] > mid_right:
            # we move the right pointer to middle index minus 1
            right = mid - 1
        elif mid_left < nums[mid] and mid_right < nums[mid]:
            # else we return the middle value
            return mid

    return None
