from typing import List


def sub_array_sum(arr: List[int], expected_sum: int) -> List[int]:
    """
    Returns the indexes of the sub array in the arr whose elements sum up to expected_sum
    @param arr: input array of integers
    @param expected_sum: expected sum
    @return: start and end indices of the elements in the array which form a range which sum up to expected_sum
    """
    current_sum = 0
    index = 0

    for x in range(len(arr)):
        current_sum += arr[x]
        if current_sum >= expected_sum:
            while index < x and current_sum > expected_sum:
                current_sum -= arr[index]
                index += 1

            if current_sum == expected_sum:
                return [index, x]
    return []
