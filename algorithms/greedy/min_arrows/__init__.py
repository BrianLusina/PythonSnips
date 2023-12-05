from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
    """The answer is at least 1. First we sort the balloons by the end coordinate. Set the first end coordinate as
    current. Iterate over all balloons to check if the balloon starts after current. If so, increase answer by 1 and set
    current = right.
    """
    sorted_points = sorted(points, key=lambda x: x[1])
    result = 1
    current = sorted_points[0][1]

    for point in sorted_points:
        left = point[0]
        right = point[1]
        if current < left:
            result += 1
            current = right

    return result
