from typing import List, Optional


def find_first_in_duplicates_linear(numbers: List[int], target: int) -> Optional[int]:
    """
    Finds the first duplicate number that matches the target from the sorted numbers list. if not found, None is returned.

    This uses a linear approach to solve the problem. Which iterates through the entire list until the first occurrence
    of target is found and once found, exists immediately returning the index. If not, None is returned.

    Complexity:
    Time: O(n) as the worst case if the target is not in the number list, then the loop will go over every element in the
    list
    Space: O(1) as no extra space is allocated to handle the computation

    Args:
        numbers (list): sorted list of integers
        target (int): target number/integer being sought
    Returns:
        int or None: returns the index of the target number if found, else returns None
    """

    for idx in range(len(numbers)):
        if numbers[idx] == target:
            return idx
    return None


def find_first_in_duplicates(numbers: List[int], target: int) -> Optional[int]:
    """
    Finds the first duplicate number that matches the target from the sorted numbers list. if not found, None is returned.

    This uses a binary search approach to solve the problem.

    Complexity:
    Time: O(log(n)) as the algorithm halves the input list on every iteration reducing computation time
    Space: O(1) as no extra space is allocated to handle the computation

    Args:
        numbers (list): sorted list of integers
        target (int): target number/integer being sought
    Returns:
        int or None: returns the index of the target number if found, else returns None
    """
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) >> 1

        # If the middle number is less than the target, we move the low/left pointer to the middle + 1, eliminating the
        # left portion of the list
        if numbers[mid] < target:
            low = mid + 1
        elif numbers[mid] > target:
            # if the middle number is greater than the target, we move the right/high pointer to the middle-1, removing
            # the right portion of the list
            high = mid - 1
        else:
            # This else block addresses finding the first occurrence of the target element. This block is entered when
            # the target is equal to numbers[mid]. Since the list is sorted in ascending order, the target is either the
            # middle element or an element on its left. This makes sure that we return the first occurrence of target.

            # This addresses an edge case were we could possibly deal with the first occurrence on the first index.
            if mid - 1 < 0:
                return mid
            # next is to check if the element to the left of numbers[mid], i.e. numbers[mid-1] is the target or not. It
            # is not, this evaluates to true and implies that numbers[mid] is the first occurrence, so mid is returned
            if numbers[mid - 1] != target:
                return mid
            # However, if the element on the left is also the same as the target element, we update high to mid - 1. This
            # way, we condense our search space to find the first occurrence of the target which will be on the left of
            # the midpoint.
            high = mid - 1
