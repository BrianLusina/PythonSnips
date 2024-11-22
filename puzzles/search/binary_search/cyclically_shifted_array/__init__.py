from typing import List

def find_index_of_smallest_number(numbers: List[int]) -> int:
    """
    Finds the index of the smallest number in a cyclically shifted array

    Args:
        numbers (list): cyclically shifted array
    Returns:
        int: index of the smallest number in a cyclically shifted array
    """
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        middle = (left_pointer + right_pointer) >> 1

        # if the number in the middle is less than or equal to the number on the right, this means that the search space
        # should be moved to the left. Eliminating numbers on the right by moving the right pointer to the middle. This
        # is because the numbers are increasing, therefore the numbers we are looking for can not be on the right
        if numbers[middle] <= numbers[right_pointer]:
            right_pointer = middle
        elif numbers[middle] > numbers[right_pointer]:
            # move the left pointer to the middle + 1 to eliminate the search space on the left if the middle number
            # is greater than the number at the right pointer. This is because the numbers are decreasing from the middle
            # therefore we can possibly find the number we are searching for in the right search space
            left_pointer = middle + 1

    return left_pointer
