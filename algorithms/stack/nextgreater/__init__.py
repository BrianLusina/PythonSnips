from typing import List
from collections import deque


def next_greater(nums: List[int]) -> List[int]:
    """Finds the next greater element of an array where next greater element is to the right of the element

    The idea is to traverse the array from right to left and use stack to keep track of next greater element in right.

    - Initialize an empty stack `stack` and result of size len(nums).
    - Run a loop from end to start i.e., n-1 to zero (Right to Left and i-based).
    - In each iteration of loop:
        - While the element at top of stack is less than or equal to the current array element, we pop elements from the
        stack. This operation will ensure that:
            - Either the stack will be empty(no element greater than the current element exists in right side of the
            current element).
            - The element at the top of the stack will be greater than the current element and closest to the
            current element in right.

        - If stack is empty then result[i] will be -1 Else it will be top of stack `stack`.
        - Push the current element in stack s.
    - Return result as answer.

    Complexity
    - Time Complexity: O(N), as we are iterating over array once and each element is pushed into and popped out of stack
    at max one time.

    - Auxiliary Space: O(N), as vector res is of size N and stack s can reach max size as N.

    Args:
        nums(list): list of numbers
    Returns:
        list: list with elements that are greater than the element before them
    """
    if len(nums) <= 1:
        return [-1]

    stack = deque()
    result = [0] * len(nums)

    # traverse the array from the last element in backward direction
    for i in range(len(nums) - 1, -1, -1):
        # while an element at top of stack is less than or equal to the current array element, we pop elements from the
        # stack
        while len(stack) and stack[-1] <= nums[i]:
            stack.pop()

        # if stack becomes empty, we store -1 in the result list else we store the top element of the stack.
        if not len(stack):
            result[i] = -1
        else:
            result[i] = stack[-1]

        # pushing the current array element into the stack.
        stack.append(nums[i])

    return result
