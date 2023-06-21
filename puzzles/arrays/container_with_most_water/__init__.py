from typing import List


def max_area(height: List[int]) -> int:
    """
    Finds the container that can contain the most water.
    :param height: list of integers which denote the vertical line heights of the edges of a container
    :return: Maximum area that can be obtained from the heights
    """
    left, right, width, result = 0, len(height) - 1, len(height) - 1, 0

    for w in range(width, 0, -1):
        if height[left] < height[right]:
            result, left = max(result, height[left] * w), left + 1
        else:
            result, right = max(result, height[right] * w), right - 1

    return result
