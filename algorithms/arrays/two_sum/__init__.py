from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a given list of integers which sum up to the target. This assumes the numbers are sorted in
    ascending order.

    Complexity:
    Where n is the number of elements in the list.

    Time: O(n) as the algorithm has to iterate through each element in the list
    Space: O(n) as the algorithm stores each element in a dictionary that it uses to check if the element that has been
    seen already sums up to the target with the current element the algorithm is iterating over.

    Args:
        numbers List: list of numbers
        target int: Target number
    Returns:
        List of two numbers that sum up to the target
    """
    m = {}

    for idx, num in enumerate(numbers, start=1):
        complement = target - num

        if complement in m:
            return [m[complement], idx]
        m[num] = idx


def two_sum_with_pointers(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a given list of integers which sum up to the target. This assumes the numbers are sorted in
    ascending order.

    Complexity:
    Where n is the number of elements in the list.

    Time: O(n) as the algorithm has to iterate through each element in the list
    Space: O(1) as the algorithm does not store elements in a data structure and simply iterates through each element
     comparing the element on the left with the element on the right

    Args:
        numbers List: list of numbers
        target int: Target number
    Returns:
        List of indices of the two numbers that sum up to the target
    """
    first_pointer = 0
    last_pointer = len(numbers) - 1

    while first_pointer < last_pointer:
        result = numbers[first_pointer] + numbers[last_pointer]
        if result == target:
            return [first_pointer, last_pointer]
        elif result < target:
            first_pointer += 1
        else:
            last_pointer -= 1
