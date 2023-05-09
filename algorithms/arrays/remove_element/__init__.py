from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    Removes an element from a given list of integers modifying the input list in place. Effectively, this means that
    no extra space is allocated and the original list is modified. Care should be taken by the caller as the original
    list is modified by this function.

    We start off with a pointer(reference) to the first element in the list and keep track of the size of the input
    array(read list) as we use this to track the movement of the pointer.

    As long as the pointer is less than the size of the list, we perform a comparison on the value of the
    current position of the pointer and the input value(the value to be removed). If they are equal, we remove this
    value by assigning it the last value in the list and decrement the size of the list by 1. if they are not equal,
    this is not the value to remove, therefore we proceed along the list, increment the pointer by 1. We do this until
    the pointer and the new size of the list are not equal.

    Complexity:
        Time Complexity is O(n) where n is the size of the input list
        Space Complexity is O(1) as no extra space is allocated but instead the original input array is modified
    :param nums: Input list
    :param val: value to remove
    :return: new length of the input array
    """
    pointer = 0
    size = len(nums)

    while pointer < size:
        if nums[pointer] == val:
            nums[pointer] = nums[size - 1]
            size -= 1
        else:
            pointer += 1

    return size
