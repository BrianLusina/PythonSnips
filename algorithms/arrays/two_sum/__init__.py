from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    m = {}

    for idx, num in enumerate(numbers, start=1):
        complement = target - num

        if complement in m:
            return [m[complement], idx]
        m[num] = idx
