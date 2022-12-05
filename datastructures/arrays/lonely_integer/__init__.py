from typing import List
from collections import Counter


def lonely_integer(a: List[int]):
    counts = Counter(a)
    return counts.most_common()[-1][0]
