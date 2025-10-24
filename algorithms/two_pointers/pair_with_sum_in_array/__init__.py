from typing import List, Tuple


def pair_with_sum_in_collection(collection: List[int], target: int) -> Tuple[int, int]:
    """
    This finds the pair in the given collection that sums up to the target. This assumes that the passed in collection
    is sorted. This returns the indices of the values that sum up to the target
    Args:
        collection (list): sorted collection of integers
        target (int): target sum
    Return:

    """
    left_pointer = 0
    right_pointer = len(collection) - 1

    while left_pointer < right_pointer:
        left = collection[left_pointer]
        right = collection[right_pointer]

        current_sum = left + right

        if current_sum > target:
            right_pointer -= 1
        elif current_sum < target:
            left_pointer += 1
        else:
            return left_pointer, right_pointer

    return left_pointer, right_pointer
