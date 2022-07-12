from typing import List, Union


def find_uniq(arr: List[Union[int, float]]) -> Union[int, float]:
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
