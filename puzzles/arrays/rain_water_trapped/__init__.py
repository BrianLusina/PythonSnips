from typing import List


def trapped_rain_water(heights: List[int]) -> int:
    if not heights or len(heights) == 1:
        return 0
    left, right = 0, len(heights) - 1
    result = 0
    mx, mi = 0, 0

    while left <= right:
        mi = min(heights[left], heights[right])
        mx = max(mx, mi)

        result += mx - mi

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return result
