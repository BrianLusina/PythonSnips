from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Sort the points by distance, then take the closest K points.
    """
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:k]
