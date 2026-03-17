from typing import List
from itertools import combinations


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


def combine(n: int, k: int) -> List[List[int]]:
    result = []
    stack = []

    def backtrack(start: int):
        if len(stack) == k:
            result.append(stack[:])
            return

        for num in range(start, n + 1):
            stack.append(num)
            backtrack(num + 1)
            stack.pop()

    backtrack(1)
    return result


def combine_2(n: int, k: int) -> List[List[int]]:
    ans = []

    def backtrack(path: List[int], start: int):
        # If the combination is complete, save it
        if len(path) == k:
            ans.append(path[:])
            return

        # How many more numbers we still need
        need = k - len(path)

        # Compute the maximum valid starting number
        # Ensures enough numbers remain to finish the combination
        max_start = n - need + 1

        # Try each possible next number
        for num in range(start, max_start + 1):
            path.append(num)  # choose
            backtrack(path, num + 1)  # explore
            path.pop()  # un-choose (backtrack)

    # Start recursion with an empty combination
    backtrack([], 1)
    return ans


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    return result
