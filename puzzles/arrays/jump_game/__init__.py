from typing import List


def can_jump(nums: List[int]) -> bool:
    current_position = nums[0]

    for idx in range(1, len(nums)):
        if current_position == 0:
            return False

        current_position -= 1

        current_position = max(current_position, nums[idx])

    return True
