from typing import List


def count_min_non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    Counts the minimum number of intervals that must be removed to make the intervals non-overlapping. Modifies the
    input list in place
    Args:
        intervals (List[List[int]]): The intervals to check
    Returns:
        int: number of intervals to remove
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        # Non-overlapping interval found
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count


def count_min_non_overlapping_intervals_2(intervals: List[List[int]]) -> int:
    """
    Counts the minimum number of intervals that must be removed to make the intervals non-overlapping. Does not modify
     the input list in place, this instead uses a sorted copy of the input intervals
    Args:
        intervals (List[List[int]]): The intervals to check
    Returns:
        int: number of intervals to remove
    """
    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    end = sorted_intervals[0][1]
    count = 1

    for current_interval in sorted_intervals[1:]:
        current_interval_start, current_interval_end = current_interval
        # Non-overlapping interval found
        if current_interval_start >= end:
            end = current_interval_end
            count += 1

    return len(sorted_intervals) - count
