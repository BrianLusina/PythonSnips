from typing import List


def sorted_squared_array(array: List[int]) -> List[int]:
    """
    Takes in a sorted array and returns a new array with the values squared and sorted in ascending order.
    Args:
        array (List[int]): A sorted array of integers.
    Returns:
        List[int]: A new array with the values squared and sorted in ascending order.
    """
    n = len(array)
    if n == 0:
        return []
    # the result array must be the same length as the input array
    result = [0] * n

    # two pointers that point to the start and end of the input array to enable insertion of the squared values in
    # ascending order
    left, right = 0, n - 1

    # file result array from right to left (largest to smallest squares
    for i in range(n - 1, -1, -1):
        left_abs = abs(array[left])
        right_abs = abs(array[right])

        if left_abs > right_abs:
            square = left_abs * left_abs
            result[i] = square
            left += 1
        else:
            square = right_abs * right_abs
            result[i] = square
            right -= 1

    # Write your code here.
    return result


def sorted_squared_array_2(array: List[int]) -> List[int]:
    """
    Takes in a sorted array and returns a new array with the values squared and sorted in ascending order.
    Args:
        array (List[int]): A sorted array of integers.
    Returns:
        List[int]: A new array with the values squared and sorted in ascending order.
    """
    n = len(array)
    if n == 0:
        return []
    # the result array must be the same length as the input array
    result = [0] * n

    # two pointers that point to the start and end of the input array to enable insertion of the squared values in
    # ascending order
    left, right = 0, n - 1

    # file result array from right to left (largest to smallest squares
    for i in range(n - 1, -1, -1):
        left_square = array[left] ** 2
        right_square = array[right] ** 2

        if left_square > right_square:
            result[i] = left_square
            left += 1
        else:
            result[i] = right_square
            right -= 1

    # Write your code here.
    return result
