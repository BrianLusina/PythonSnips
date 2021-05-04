from math import sqrt
from typing import List


def construct_rectangle(area: int) -> List[int]:
    w = int(sqrt(area))

    while area % w != 0:
        w -= 1

    return [area // w, w]
