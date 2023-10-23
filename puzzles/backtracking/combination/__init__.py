from typing import List


def combination_sum_3(k: int, n: int) -> List[List[int]]:
    result = []

    def backtrack(num: int, stack: List[int], target: int):
        if len(stack) == k:
            if target == 0:
                result.append(stack)
            return

        for x in range(num + 1, 10):
            if x <= target:
                backtrack(x, stack + [x], target - x)
            else:
                return

    backtrack(0, [], n)
    return result


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    result = []



    return result
