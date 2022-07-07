from typing import List


def each_cons(lst: List[int], n: int) -> List[List[int]]:
    result = []

    for x in range(0, len(lst) - n + 1):
        result.append(lst[x:x + n])
    return result
