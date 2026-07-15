from typing import List


def insert_interval(existing_intervals: List[List[int]], new_interval: List[int]):
    """
    Inserts the new interval into the list of existing intervals and return the updated list of intervals. This assumes
    that the existing_intervals array is already sorted by the start time.
    Args:
        existing_intervals (List[List[int]]): A list of intervals, where each interval is represented as a list of two integers [start, end].
        new_interval (List[int]): A new interval to be inserted into the list of existing intervals.
    Returns:
        List[List[int]]: The updated list of intervals after inserting the new interval.
    """
    # no intervals to insert
    if not existing_intervals:
        return [new_interval]
    result = []
    i = 0
    n = len(existing_intervals)
    new_start, new_end = new_interval

    # add all intervals that come completely before the new interval
    while i < n and existing_intervals[i][1] < new_start:
        result.append(existing_intervals[i])
        i += 1

    # merge all intervals that overlap with the new interval
    merged_start = new_start
    merged_end = new_end

    # add all intervals that come completely after the new interval
    while i < n and existing_intervals[i][0] <= merged_end:
        # Update merged-start and merged_end
        merged_start = min(merged_start, existing_intervals[i][0])
        merged_end = max(merged_end, existing_intervals[i][1])
        i += 1

    # add the merged interval
    result.append([merged_start, merged_end])

    # add all intervals that come completely after the new interval
    while i < n:
        result.append(existing_intervals[i])
        i += 1

    return result
