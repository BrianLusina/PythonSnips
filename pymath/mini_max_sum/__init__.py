from typing import List


def mini_max_sum(arr: List[int]) -> List[int]:
    min_ = sum(arr) - max(arr)
    max_ = sum(arr) - min(arr)

    return [min_, max_]
