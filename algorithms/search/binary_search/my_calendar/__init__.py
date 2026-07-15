from typing import List, Tuple


class MyCalendar:
    def __init__(self):
        self.calendar: List[Tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        """Checks if it is possible to book an event into a calendar given a start and end time.

        A potential insertion index idx means that the booking at calendar[idx-1] must come before the new booking,
        and the booking at calendar[idx] must come after the new booking. To simplify the searching process, we can
        deduce that calendar[idx-1] has a start time earlier than start, and calendar[idx] has a later start time than
        start. Essentially, we are trying to find the leftmost entry such that the start time of this booking is greater
         than the start of the new booking. We have the feasible function calendar[idx][0] > start, if this condition is
        true, we will recurse the left half, otherwise, recurse the right half.

        To implement the booking behaviour, we will use binary search to find a potential insertion index, then check
        whether the new booking can be actually scheduled into our calendar by checking whether the new booking overlaps
         with calendar[idx-1] and calendar[idx].

        Complexity: n is the number of events booked
        - Time Complexity: O(nlog(n)). For each new event, we search that the event is legal in O(log(n)) time then insert
        in O(log(n)) time.

        - Space Complexity: O(n), the size of the structure used

        Note that using list.insert() to add new events to a built in list as this does will result in a time complexity
        as O(n) instead of O(log(n)) for each insertion operation(see the docs). However, due to the built-in instruction
        optimization in list.insert() and the constraint n<=1000 for this problem, this O(n^2) solution may somehow
        show a better performance in runtime.

        Args:
            start(int): Start time of new event
            end(int): end time of new event.
        Returns:
              bool: True if it is possible to book event and has been added to the calendar, False otherwise.
        """
        left, right, idx = 0, len(self.calendar) - 1, len(self.calendar)

        while left <= right:
            mid = (left + right) // 2
            if self.calendar[mid][0] > start:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        # check if there is an overlap of calendar[idx-1] or calendar[idx]
        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
            idx < len(self.calendar) and self.calendar[idx][0] < end
        ):
            return False
        self.calendar.insert(idx, (start, end))
        return True
