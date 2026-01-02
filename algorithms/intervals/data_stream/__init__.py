from typing import List, Dict
from bisect import bisect_right, insort


class SummaryRanges:
    def __init__(self):
        # Map to store intervals: key = start of interval, value = end of interval.
        # Intervals are kept sorted automatically by map ordering.
        self.intervals: Dict[int, int] = {}
        # stores the starts of the intervals
        self.starts: List[int] = []

    def add_num(self, value: int) -> None:
        """
        Adds the integer value to the stream.

        Args:
            value (int): The integer value to add to the stream.
        """
        new_start = value
        new_end = value

        # Find the first interval with a start greater than 'value'
        idx = bisect_right(self.starts, value)

        # Check the interval immediately before 'value' (if it exists)
        if idx > 0:
            previous_start = self.starts[idx - 1]
            previous_end = self.intervals[previous_start]

            # Case 1: 'value' already inside an existing interval -> do nothing
            if previous_end >= value:
                return

            # Case 2: 'value' extends the previous interval by exactly 1
            if previous_end == value - 1:
                # merge with previous
                new_start = previous_start

        # Case 3: 'value' connects directly to the start of the next interval
        next_start = self.starts[idx] if idx < len(self.starts) else None
        if next_start is not None and next_start == value + 1:
            # merge with next
            new_end = self.intervals[next_start]
            # remove the old interval [next_start, ...]
            del self.intervals[next_start]
            self.starts.pop(idx)

        # Insert the merged or new interval into the map
        if new_start in self.intervals:
            # update existing interval(merged with previous)
            self.intervals[new_start] = new_end
        else:
            # insert new
            self.intervals[new_start] = new_end
            insort(self.starts, new_start)

    def get_intervals(self) -> List[List[int]]:
        """
        Returns the current summary of numbers as a list of disjoint intervals [start_i, end_i], sorted by start_i.
        Returns:
            List[List[int]]: List of disjoint intervals
        """
        result: List[List[int]] = []
        # Collect all intervals from the map
        for s in self.starts:
            result.append([s, self.intervals[s]])
        return result


class SummaryRangesV2:
    def __init__(self):
        # stores the intervals
        self.intervals: List[List[int]] = []
        # stores the starts of the intervals
        self.starts: List[int] = []

    def add_num(self, value: int) -> None:
        # If we have an existing interval, we should join the new value if: start - 1 <= value <= end + 1
        # So, for an interval [start, end], the condition to see if value is already included is: start <= value <= end

        # 1. Get the index of the interval where the value should be inserted
        idx = bisect_right(self.starts, value)

        # ... (Case 1: Duplicate)
        # if idx is greater than 0, our left neighbor is at idx - 1
        # 2. Check for Duplicate (already in left neighbor)
        if (
            idx > 0
            and self.intervals[idx - 1][0] <= value <= self.intervals[idx - 1][1]
        ):
            return

        # identify possible neighbors for merging
        left_merge = idx > 0 and self.intervals[idx - 1][1] + 1 == value
        right_merge = idx < len(self.intervals) and self.intervals[idx][0] - 1 == value

        # ... (Case 2: Double Merge)
        # 3. Check for Double Merge
        if left_merge and right_merge:
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.starts.pop(idx)
            self.intervals.pop(idx)
        # ... (Case 3: Left Merge)
        elif left_merge:
            # Extend the end of the left interval
            self.intervals[idx - 1][1] = value
        # ... (Case 4: Right Merge)
        elif right_merge:
            # Extend the start of the right interval
            self.intervals[idx][0] = value
            # keep the starts list updated
            self.starts[idx] = value
        # ... (Case 5: New Island)
        else:
            insort(self.starts, value)
            insort(self.intervals, [value, value])

    def get_intervals(self) -> List[List[int]]:
        """
        Returns the current summary of numbers as a list of disjoint intervals [start_i, end_i], sorted by start_i.
        This is run in O(1) time as it simply returns the list of intervals.
        Returns:
            List[List[int]]: List of disjoint intervals
        """
        return self.intervals
