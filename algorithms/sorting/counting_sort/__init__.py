from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    result = [0] * len(arr)

    for num in arr:
        result[num] += 1

    return result
