from typing import List


def find_duplicate_floyd_algo(numbers: List[int]) -> int:
    """
    Finds the duplicate number in a list of integers.
    @param numbers: List of integers
    @return: duplicated integer
    """
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
    for i in range(len(numbers)):
        idx = abs(numbers[i])
        if numbers[idx] < 0:
            return abs(numbers[i])
        else:
            numbers[idx] = -numbers[idx]
    return -1
