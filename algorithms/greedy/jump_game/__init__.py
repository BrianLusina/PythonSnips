from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    This function checks if it is possible to reach the last index of the array from the first index.
    Args:
        nums(list): list of integers
    Returns:
        bool: True if can jump to the last index, False otherwise
    """

    current_position = nums[0]

    for idx in range(1, len(nums)):
        if current_position == 0:
            return False

        current_position -= 1

        current_position = max(current_position, nums[idx])

    return True


def can_jump_2(nums: List[int]) -> bool:
    """
    This function checks if it is possible to reach the last index of the array from the first index.

    This variation starts checking from the last element in the input list and tracking back to check if it is possible
    to reach the end.

    Args:
        nums(list): list of integers
    Returns:
        bool: True if can jump to the last index, False otherwise
    """
    target_num_index = len(nums) - 1

    for idx in range(len(nums) - 2, -1, -1):
        if target_num_index <= idx + nums[idx]:
            target_num_index = idx

    if target_num_index == 0:
        return True
    return False


def jump(nums: List[int]) -> int:
    """
    This function returns the minimum number of jumps needed to reach the last index of the array from the first index.
    Args:
        nums(list): list of integers
    Returns:
        int: minimum number of jumps needed to reach the last index
    """
    size = len(nums)
    # if start index == destination index == 0
    if size == 1:
        return 0

    # destination is last index
    destination = size - 1

    # record of current coverage, record of last jump index
    current_coverage, last_jump_index = 0, 0

    # min number of jumps
    min_jumps = 0

    # Greedy strategy: extend coverage as long as possible with lazy jump
    for idx in range(size):
        # extend coverage as far as possible
        current_coverage = max(current_coverage, idx + nums[idx])

        # forced to jump (by lazy jump) to extend coverage
        if idx == last_jump_index:
            # update last jump index
            last_jump_index = current_coverage

            # update counter of jump by +1
            min_jumps += 1

            # check if destination has been reached
            if current_coverage >= destination:
                return min_jumps

    return min_jumps


def jump_2(nums: List[int]) -> int:
    """
    This function returns the minimum number of jumps needed to reach the last index of the array from the first index.
    Args:
        nums(list): list of integers
    Returns:
        int: minimum number of jumps needed to reach the last index
    """
    # Store the length of the input array
    size = len(nums)

    # if start index == destination index == 0
    if size == 1:
        return 0

    # Initialize the variables to track the number of jumps,
    # the current jump's limit, and the farthest reachable index
    min_jumps = 0
    current_jump_boundary = 0
    furthest_jump_index = 0

    # Iterate through the array, stopping before the last element
    for idx in range(size - 1):
        # Update the farthest_jump_index to be the maximum of its current value
        # and the index we can reach from the current position
        furthest_jump_index = max(furthest_jump_index, idx + nums[idx])

        # If we have reached the limit of the current jump
        if idx == current_jump_boundary:
            # update counter of jump by +1
            min_jumps += 1

            # Update the current_jump_boundary to the farthest we can reach
            current_jump_boundary = furthest_jump_index

    # Return the total number of jumps needed to reach the end of the array
    return min_jumps
