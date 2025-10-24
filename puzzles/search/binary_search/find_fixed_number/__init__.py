from typing import Optional, List


def find_fixed_point(numbers: List[int]) -> Optional[int]:
    """
    The assumption made here is that the list is already sorted and there are distinct elements. This uses a binary
    search algorithm to find a fixed point.
    Using the binary search algorithm will entail splitting the sorted input list in 2 halves at the midpoint. It's at
    this midpoint that we check if the middle value is equal to its index. If it is, we immediately return as we have
    found the fixed point. if the middle value is greater than its index, this means that the right portion of the list
    as each element on the right will be greater than their indices. Same case applies for the middle value being less
    than its index. In that scenario, we discard the left portion of the list as those elements will have indices that
    are less than their values. The middle point is then moved according to this rule, either to the left or to the right
    This is repeated until the fixed point is found, if not, None is returned.
    Args:
        numbers (list) of (int): sorted list of distinct integers
    Returns:
        optional (int): Either None if a fixed point is not found of the element.
    """
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        # if the middle value is less than its index
        if numbers[mid] < mid:
            # we move the left(or low) index to the middle + 1. This eliminates the left portion of the list
            low = mid + 1
        # if the middle value is greater than the index
        elif numbers[mid] > mid:
            # we move the high(or right) index to the middle - 1. This eliminates the right portion of the list
            high = mid - 1
        else:
            # else we have found the fixed point
            return numbers[mid]
    return None


def find_fixed_point_linear(numbers: List[int]) -> Optional[int]:
    """
    Uses a linear algorithm to find a fixed point in a list of numbers. The assumption made here is that the list is
    already sorted and there are distinct elements
    Space: O(1) as no extra space is allocated
    Time: O(n) as the worst case is looping over all elements in the list
    Args:
        numbers (list) of (int): sorted list of distinct integers
    Returns:
        optional (int): Either None if a fixed point is not found of the element.
    """
    for x in range(len(numbers)):
        if numbers[x] == x:
            return numbers[x]
    return None
