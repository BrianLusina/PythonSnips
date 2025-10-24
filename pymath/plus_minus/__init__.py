from typing import List


def plus_minus(arr: List[int]) -> List[float]:
    size = len(arr)
    positives = 0
    negatives = 0
    zeroes = 0

    for number in arr:
        if number < 0:
            negatives += 1
        if number == 0:
            zeroes += 1
        if number > 0:
            positives += 1

    return [
        round(positives / size, 6),
        round(negatives / size, 6),
        round(zeroes / size, 6),
    ]
