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
    size = len(nums)
    # destination is last index
    destination = size - 1

    # record of current coverage, record of last jump index
    current_coverage, last_jump_index = 0, 0

    # min number of jumps
    min_jumps = 0

    # if start index == destination index == 0
    if size == 1:
        return 0

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
