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
        current_interval_start_time = interval[0]
        current_interval_end_time = interval[1]
        last_merged_interval_end_time = merged[-1][1] if merged else float("-inf")

        # if the merged array is empty or the last interval in the merged array does not overlap with the current interval
        if not merged or last_merged_interval_end_time < current_interval_start_time:
            # add it to the merged list
            merged.append(interval)
        else:
            # else we merge the intervals, by updating the max end time of the last interval in the merged list
            merged[-1][1] = max(
                last_merged_interval_end_time, current_interval_end_time
            )

    return merged
