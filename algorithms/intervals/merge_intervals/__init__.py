from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges overlapping intervals in a list of intervals.
    Args:
        intervals (List[List[int]]): A list of intervals, where each interval is represented as a list of two integers [start, end].
    Returns:
        List[List[int]]: A list of merged intervals.
    """
    # no intervals to merge
    if not intervals:
        return []

    # copy the `intervals` array to avoid mutating the input array
    closed_intervals = intervals[:]
    # sort the closed intervals array in place using the start time as the key. This sorts in ascending order
    closed_intervals.sort(key=lambda x: x[0])

    # the final result array
    merged = []

    for interval in closed_intervals:
        # if the merged array is empty or the last interval in the merged array does not overlap with the current interval
        if not merged or merged[-1][1] < interval[0]:
            # add it to the merged list
            merged.append(interval)
        else:
            # else we merge the intervals, by updating the max end time of the last interval in the merged list
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
