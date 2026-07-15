from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Checks if an employee can attend all meetings given a list of intervals representing the start and end times of each
    meeting.

    A person can attend all meetings if and only if none of the meetings overlap. By sorting the intervals by start time,
    we can easily check if any two consecutive intervals overlap.

    We iterate over each interval, beginning with the second interval in the sorted list. We compare the start time of
    the current interval with the end time of the previous interval. If the start time of the current interval is less
    than the end time of the previous interval, then the two intervals overlap and the person cannot attend both meetings,
    so we return false.

    Otherwise, the person can attend both meetings, and we continue to the next interval. If we reach the end of the
    list without finding any overlapping intervals, then the person can attend all meetings, and we return true.

    Complexity Analysis

    Time Complexity: O(n * logn) where n is the number of intervals. The time complexity is dominated by the sorting step.

    Space Complexity:

    Since we are sorting the intervals and creating a new sorted_intervals variable that has the sorted intervals by time
    the space incurred is O(n). However, if sorting in place, then the space cost becomes O(1) and in that case no extra
    extra space would be used beyond a few variables.

    Args:
        intervals(list): list of intervals where each entry is a list containing the start and end time of a meeting
    Returns:
        bool: True if an employee can attend all meetings, false otherwise
    """
    if len(intervals) == 0:
        return True

    # Sort the intervals by start time first to enable easier iteration through the intervals. Meetings with similar
    # start times will be close to each other, allowing quick and early exit if they overlap.
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Keep track of the last seen end time.
    # We initialize the first interval's end time to keep track of the last interval's end that we have seen so far
    last_end_time = sorted_intervals[0][1]

    # We then iterate through the list checking if there is any overlaps
    # Start from the second interval in the list to check if it overlaps with the previous interval.
    for current_interval in sorted_intervals[1:]:
        # Get the start and end of the current interval
        current_start, current_end = current_interval

        if current_start < last_end_time:
            # there is an overlap, we return here
            return False

        # Otherwise, we update the last end time we have seen with this interval's end time
        last_end_time = current_end

    # If no overlap is found, we return True
    return True
