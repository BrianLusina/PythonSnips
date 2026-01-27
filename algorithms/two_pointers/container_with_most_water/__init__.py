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

def max_area_2(heights: List[int]) -> int:
    """
    Finds the container that can contain the most water.
    Args:
        heights(list): list of integers which denote the vertical line heights of the edges of a container
    Returns:
        int: Maximum area that can be obtained from the heights
    """
    left, right = 0, len(heights) - 1
    current_max = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        current_max = max(current_area, current_max)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return current_max
