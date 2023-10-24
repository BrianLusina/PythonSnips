from typing import List


def rob(nums: List[int]) -> int:
    """Uses a top-down approach using Rolling Window technique where the idea is to only remember what is the maximum
    gain at the next three houses from the current position."""
    current, previous = 0, 0

    for house in nums:
        current, previous = max(previous + house, current), current

    return current
