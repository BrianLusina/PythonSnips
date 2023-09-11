from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index
