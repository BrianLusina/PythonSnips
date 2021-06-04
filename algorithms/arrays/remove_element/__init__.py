from typing import List


def remove_element(nums: List[int], val: int) -> int:
    pointer = 0
    size = len(nums)

    while pointer < size:
        if nums[pointer] == val:
            nums[pointer] = nums[size - 1]
            size -= 1
        else:
            pointer += 1

    return size
