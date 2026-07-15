from typing import List, Optional


def find_closest_number(items: List[int], target: int) -> Optional[int]:
    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(items) - 1
    closest_number = None

    # edge cases for empty list or list with 1 item
    if len(items) == 0:
        return None
    if len(items) == 1:
        return items[0]

    while low <= high:
        mid = (low + high) // 2

        # ensure we do not read beyond the bounds of the list
        if mid + 1 < len(items):
            min_diff_right = abs(items[mid + 1] - target)

        if mid > 0:
            min_diff_left = abs(items[mid - 1] - target)

        # check if the absolute value between left and right elements are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = items[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = items[mid + 1]

        # move the mid-point appropriately as is done via binary search
        if items[mid] < target:
            low = mid + 1
        elif items[mid] > target:
            high = mid - 1
            if high < 0:
                return items[mid]
        # if the element itself is the target, the closest number to it is itself, return the number
        else:
            return items[mid]

    return closest_number
