from typing import List


def intervals_intersection(
    interval_list_a: List[List[int]], interval_list_b: List[List[int]]
) -> List[List[int]]:
    """
    This function finds the intersections between interval_list_a and interval_list_b and returns the list of
    intersections.

    Time Complexity is O(n+m): where n is the length of list a and m is the length of list b
    Space Complexity is O(1) for auxiliary space as no extra space is required other than the pointers used to move along
    both lists. However, the resultant list returned can have a worst case of O(n+m) in the case we have either list
    having multiple intervals that are all intersections in the other list.

    Args:
        interval_list_a(list): list 'a' of intervals.
        interval_list_b(list): list 'b' of intervals.
    Returns:
        list: list of intersected intervals
    """
    if not interval_list_a and not interval_list_b:
        return []
    # pointers that will move along the interval lists, i moves along the intervals on interval_list_a, while j moves
    # along the intervals on interval_list_b
    i, j = 0, 0

    # the final result list
    intersected_intervals = []

    interval_list_a_len = len(interval_list_a)
    interval_list_b_len = len(interval_list_b)

    # while loop will break whenever either of the lists ends
    while i < interval_list_a_len and j < interval_list_b_len:
        # Let's check if interval_list_a[i] intersects interval_list_b[j]
        interval_a = interval_list_a[i]
        interval_b = interval_list_b[j]

        # extract the start and end times of each interval
        start_a, end_a = interval_a
        start_b, end_b = interval_b

        # Get the potential startpoint and endpoint of the closed interval intersection
        closed_interval_start = max(start_a, start_b)
        closed_interval_end = min(end_a, end_b)

        # if this is an actual intersection
        if closed_interval_start <= closed_interval_end:
            # add it to the list
            closed_interval = [closed_interval_start, closed_interval_end]
            intersected_intervals.append(closed_interval)

        # Move forward in the list whose interval ends earlier
        if end_a <= end_b:
            i += 1
        else:
            j += 1

    return intersected_intervals
