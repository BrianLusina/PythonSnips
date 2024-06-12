from typing import List


def arbitrary_precision_increment(a: List[int]) -> List[int]:
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i - 1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a


def arbitrary_precision_increment_two(a: List[int]) -> List[int]:
    s = "".join(map(str, a))
    result = str(int(s) + 1)
    output = [int(n) for n in result]

    return output
