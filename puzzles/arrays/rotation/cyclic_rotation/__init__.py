from typing import List


def cyclic_rotation(a: List, k: int) -> List:
    """Rotates an integers in array a by k number of times. Moving each element k positions to its right with the
    original list unmodified

    Complexity:
        Time: O(n) where n is the number of elements in the list
        Space: O(n) a new list is created from rotating the original list. This results in extra space being used of size
        n which is the original list's size

    Args:
        a (List): list of values to rotate
        k (int): how many rotations to perform
    Returns:
        List: rotated list
    """

    length = len(a)

    if length == 0 or length == k or len(set(a)) == 1:
        return a

    output = [0 for _ in a]

    for index, value in enumerate(a):
        new_index = index + k

        if new_index >= length:
            new_position = new_index - length
            output[new_position] = value
        else:
            output[new_index] = value

    return output


def cyclic_rotation_2(nums: list, k: int) -> list:
    """
    This modifies the array nums in place though
    """
    length = len(nums)

    if length == 0:
        return nums

    k = k % length
    nums[:] = nums[length - k :] + nums[: length - k]
    return nums
