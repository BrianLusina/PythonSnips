from typing import List


def find_duplicate_floyd_algo(numbers: List[int]) -> int:
    """
    Finds the duplicate number in a list of integers.

    This code implements Floyd's Tortoise and Hare algorithm to find the duplicate number in a list of integers. It
    uses two pointers, slow and fast, that move at different speeds through the list, eventually meeting at the
    duplicate number. The algorithm assumes that the list contains a duplicate number and that the numbers in the list
    are indices that point to other numbers in the list.

    Args:
        numbers (list): list of integers
    Returns:
        int: duplicated integer
    """
    if not numbers:
        raise ValueError("List is empty")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("List contains non-integer values")

    if len(numbers) == len(set(numbers)):
        return -1

    if len(numbers) <= 1:
        return -1

    slow = numbers[0]
    fast = numbers[numbers[0]]

    while slow != fast:
        slow = numbers[slow]
        fast = numbers[numbers[fast]]

    fast = 0
    while fast != slow:
        slow = numbers[slow]
        fast = numbers[fast]

    return slow


def find_duplicate(numbers: List[int]) -> int:
    """
    Finds the duplicate number in a list of integers.
    @param numbers: List of integers
    @return: duplicated integer
    """
    if not numbers:
        raise ValueError("List is empty")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("List contains non-integer values")

    if len(numbers) == len(set(numbers)):
        return -1

    if len(numbers) <= 1:
        return -1

    for i in range(len(numbers)):
        idx = abs(numbers[i])
        if numbers[idx] < 0:
            return abs(numbers[i])
        else:
            numbers[idx] = -numbers[idx]

    return -1
