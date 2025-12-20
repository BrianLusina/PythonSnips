from typing import List


def remove_covered_intervals(intervals: List[List[int]]) -> int:
    """
    Finds the number of intervals that are not covered by any other interval in the list.

    This uses a greedy approach to find the number of intervals that are not covered by any other interval in the list.
    Note An interval [a, b) is considered covered by another interval [c,d) if and only if c ⇐ a and b ⇐ d.

    So, the timeline will look something like this:
    c---a---b---d

    If b <= d, then [a, b) is covered by [c, d)

    Args:
        intervals (List[List[int]]): A list of intervals, where each interval is represented as [start, end]
    Returns:
        int: The number of intervals that are not covered by any other interval in the list
    """
    # early return if there are no intervals to begin with
    if not intervals:
        return 0

    # Sort intervals by start time in ascending order and then by end time in descending order. We sort by the end time
    # to remove a tie-breaker where two intervals have the same start time.
    # This will incur a time complexity of O(nlogn). We sort in place, so, we do not
    # incur any additional space complexity by copying over to a new list. The assumption made here is that it is okay
    # to mutate the input list.
    intervals.sort(key=lambda x: (x[0], -x[1]))

    # keep track of the last max end seen so far, we use a large negative infinity to cover all possible numbers
    max_end_seen = float('-inf')
    count = 0

    # We then iterate through the given intervals
    for _, current_end in intervals:
        if current_end > max_end_seen:
            count += 1
            max_end_seen = current_end

    # return the count of non-overlapping intervals
    return count
