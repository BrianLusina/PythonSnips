from typing import List


def rotate_left(d: int, arr: List[int]) -> List[int]:
    size = len(arr)

    if size == 0 or size == d or len(set(arr)) == 1:
        return arr

    nums = [0 for _ in range(size)]

    for old_index, num in enumerate(arr):
        new_index = size + (old_index - d)

        if new_index >= size:
            new_position = new_index - size
            nums[new_position] = num
        else:
            nums[new_index] = num
    return nums
