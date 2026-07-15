from typing import List
import sys
from math import inf


def remove_min_intervals(intervals: List[List[int]]) -> int:
    # Sort the intervals based on their ending points
    intervals.sort(key=lambda x: x[1])

    # Initialize a variable to keep track of the current end point
    end = -sys.maxsize - 1

    # Initialize a variable to count the intervals that need to be removed
    remove = 0

    # Loop through each interval in the sorted list
    for interval in intervals:
        # Check if the start point of the current interval is greater than or equal to the current end point
        if interval[0] >= end:
            # If it is, update the current end point to the end point of the current interval
            end = interval[1]
        else:
            # If not, increment the count of intervals to be removed
            remove += 1

    # Return the count of intervals to be removed
    return remove


def remove_min_intervals_2(intervals: List[List[int]]) -> int:
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    current_minimum_end, count = float(-inf), 0

    for interval_start, interval_end in sorted_intervals:
        if interval_start >= current_minimum_end:
            current_minimum_end = interval_end
        else:
            count += 1

    return count
