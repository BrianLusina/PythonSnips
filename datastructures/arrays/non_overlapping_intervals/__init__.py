from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Finds the minimum number of intervals that need to be removed to make the rest of the intervals non-overlapping

    :param intervals: 2D list with intervals
    :return: minimum number of intervals that need to be removed
    """
    # sorting the 2D intervals by the end interval. This operation's complexity will depend on the sorting algorithm
    # used. However, since a new copy of the sorted intervals is returned, this has a space complexity of O(N) where
    # N is the size of the intervals
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    # end is the current minimum end interval, use to keep track of the minimal end interval seen so far
    # count is the number of intervals that need to be removed
    end, count = float('-inf'), 0

    for interval_start, interval_end in sorted_intervals:
        if interval_start >= end:
            end = interval_end
        else:
            count += 1
    return count
