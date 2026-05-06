import bisect
from typing import List


def max_envelopes(envelopes: List[List[int]]) -> int:
    # Sort the envelopes by width in ascending order, if the widths are equal sort by height in descending order.
    # This ensures that the envelopes with the same width won't be selected in our subsequence.
    # Note here that we are using sorted instead of sorting in place to avoid side effects to the input 'envelopes' that
    # may continue to be used on the call site. This ultimately incurs a space complexity cost of O(n) and time of O(n log(n))
    sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    # Create a list that will maintain the smallest ending heights for subsequences of different lengths. Initially,
    # it will just contain the heigh of the first envelop
    smallest_ending_heights = [sorted_envelopes[0][1]]

    # We iterate through the remaining envelopes, only caring about the heights(width is already handled by sorting)
    for _, height in sorted_envelopes[1:]:
        # The current height is larger than all heights in smallest ending heights
        if height > smallest_ending_heights[-1]:
            smallest_ending_heights.append(height)
        # Otherwise, find the leftmost position in smallest_ending_heights where we can place height to maintain sorted order
        idx = bisect.bisect_left(smallest_ending_heights, height)
        # this replacement ensures that smallest_ending_heights[idx] stores the smallest possible height for subsequences
        # of length idx+1
        smallest_ending_heights[idx] = height

    # Return the result which represents the maximum number of envelops that can be nested
    return len(smallest_ending_heights)


def max_envelopes_find_position(envelopes: List[List[int]]) -> int:
    # Sort the envelopes by width in ascending order, if the widths are equal sort by height in descending order.
    # This ensures that the envelopes with the same width won't be selected in our subsequence.
    # Note here that we are using sorted instead of sorting in place to avoid side effects to the input 'envelopes' that
    # may continue to be used on the call site. This ultimately incurs a space complexity cost of O(n) and time of O(n log(n))
    sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    # Create a list that will maintain the smallest ending heights for subsequences of different lengths. Initially,
    # it will just contain the heigh of the first envelop
    smallest_ending_heights = []

    def find_position(h):
        left, right = 0, len(smallest_ending_heights) - 1

        while left <= right:
            mid = (left + right) // 2
            if smallest_ending_heights[mid] < h:
                left = mid + 1
            else:
                right = mid - 1

        return left

    # We iterate through the remaining envelopes, only caring about the heights(width is already handled by sorting)
    for width, height in sorted_envelopes:
        position = find_position(height)
        # The current height is larger than all heights in smallest ending heights
        if position == len(smallest_ending_heights):
            smallest_ending_heights.append(height)
        else:
            smallest_ending_heights[position] = height

    # Return the result which represents the maximum number of envelops that can be nested
    return len(smallest_ending_heights)
