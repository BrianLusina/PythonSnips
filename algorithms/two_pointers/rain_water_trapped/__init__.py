from typing import List


def trapped_rain_water(heights: List[int]) -> int:
    if not heights:
        return 0
    # Initialize the pointers left and right at both ends of the array
    left, right = 0, len(heights) - 1
    # initialize left_max and right_max that will keep track of the highest bars each pointer has seen
    left_max, right_max = heights[left], heights[right]
    # Keeps track of the total trapped rain wayter
    result = 0

    while left < right:
        if left_max < right_max:
            left += 1
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                result += left_max - heights[left]
        else:
            right -= 1
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                result += right_max - heights[right]
    return result
