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
    # Initialize the fast and slow pointers and make them point the first
    # element of the array
    slow = fast = numbers[0]

    # PART #1
    # Traverse in array until the intersection point is found
    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = numbers[slow]
        # Move the fast pointer two times fast as the slow pointer using the
        # nums[nums[fast]] flow
        fast = numbers[numbers[fast]]
        # Break the loop when slow pointer becomes equal to the fast pointer, i.e.,
        # if the intersection is found
        if slow == fast:
            break

    # PART #2
    # Make the slow pointer point the starting position of an array again, i.e.,
    # start the slow pointer from starting position
    slow = numbers[0]
    # Traverse in the array until the slow pointer becomes equal to the
    # fast pointer
    while fast != slow:
        # Move the slow pointer using the nums[slow] flow
        slow = numbers[slow]
        # Move the fast pointer slower than before, i.e., move the fast pointer
        # using the nums[fast] flow
        fast = numbers[fast]

    # Return the fast pointer as it points the duplicate number of the array
    return fast


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
