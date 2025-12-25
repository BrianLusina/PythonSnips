from typing import List


def count_days(days: int, meetings: List[List[int]]) -> int:
    """
    Counts the number of days the employee is available for work but has no scheduled meetings.

    Complexity:

    Standard time complexity for sorting is O(n log(n)). The loop is O(n). The part that dominates the overall time
    complexity is the sorting and the loop. It amounts to O(n log(n)) as the overall. The overall space complexity for
    this approach is O(1) without accounting for the in place sorting that is taking place which is O(n) using timsort
    in Python.

    Summary of Performance
    ---
    Metric	Complexity	Reason
    ---
    Time	O(nlogn)	Dominated by the initial sort of n meetings.
    Space	O(n)	Required by Timsort for internal temporary storage.

    Args:
        days (int): The total number of days the employee is available for work
        meetings (List[List[int]]): A list of meetings, where each meeting is represented as a list of two integers [start, end]
    Returns:
        int: The number of days the employee is available for work but has no scheduled meetings
    """
    # sort meetings by start in place, incurs O(n log(n)) time complexity
    meetings.sort(key=lambda x: x[0])

    # keep track of free days
    free_days = 0

    # a pointer that keeps track of the current day
    last_busy_day = 0

    # iterate through the meetings, for each meeting we might have a gap
    for meeting in meetings:
        # get the start and end of the meeting
        start, end = meeting

        # calculate gaps, if the meeting starts at start and our last_busy_day is less than start - 1, the days in
        # between are free
        if start > last_busy_day + 1:
            free_days += (start - 1) - last_busy_day

        # update the last busy day to the maximum of the last busy day and the end of the meeting

        # This ensures that if a meeting is completely contained within a previous busy block, the boundary doesn't move
        # backward, which handles overlaps perfectly.
        last_busy_day = max(last_busy_day, end)

    # add the remaining days to the free days
    return free_days + (days - last_busy_day)


def count_days_2(days: int, meetings: List[List[int]]) -> int:
    """
    Counts the number of days the employee is available for work but has no scheduled meetings.
    
    This implementation merges overlapping meetings and counts total occupied days.
    
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1) excluding sort overhead
    
    Args:
        days (int): The total number of days the employee is available for work
        meetings (List[List[int]]): A list of meetings, where each meeting is represented as a list of two integers [start, end]
            Note: This function modifies the input list by sorting it in place.
    Returns:
        int: The number of days the employee is available for work but has no scheduled meetings
    """
    # Sort the meetings based on their start time to process them in order
    meetings.sort()

    # Initialize a variable with 0 to count the number of days when the employee has meetings scheduled
    occupied = 0

    # Initialize two variables with the first meeting’s start and end times
    start, end = meetings[0]

    # Iterate through the remaining meetings
    for i in range(1, len(meetings)):
        # If a meeting overlaps with the current merged meeting
        if meetings[i][0] <= end:
            # Extend the end time to merge it
            end = max(end, meetings[i][1])
        else:
            # Add the days of the merged meeting
            occupied += end - start + 1

            # Update start and end for the next interval
            start, end = meetings[i]

    # Add the days of the last merged meeting
    occupied += end - start + 1

    # Return the free days
    return days - occupied
