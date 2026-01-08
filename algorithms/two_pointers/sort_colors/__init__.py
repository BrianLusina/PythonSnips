from typing import List


def sort_colors(colors: List[int]) -> List[int]:
    """
    Sorts a list of 0s, 1s, and 2s in place

    This algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position where the next
    0 should be placed, the mid-pointer is used to scan the list, and the high pointer is used to track the position
    where the next 2 should be placed.

    The algorithm works by iterating through the list with the mid-pointer. If it encounters a 0, it swaps it with the
    element at the low index and increments both low and mid. If it encounters a 1, it simply increments mid. If it
    encounters a 2, it swaps it with the element at the high index and decrements high (without incrementing mid,
    because the swapped element could be a 0 or a 1).

    This algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for sorting lists
    of 0s, 1s, and 2s.

    Args:
        colors (list): list of 0s, 1s, and 2s
    Returns:
        list: sorted list of 0s, 1s, and 2s
    """
    # Initialize the three pointers, low to track 0s, mid to track 1s and high to track 2s
    low, mid, high = 0, 0, len(colors) - 1

    # Perform our loop.
    # We compare mid and high pointers because the elements at low will be swapped with elements at mid if necessary.
    # And mid will be moving up until the end of the list, while high will be moving down until it is equal to high.
    while mid <= high:
        if colors[mid] == 0:
            # Swap the mid and the low elements and move the low pointer up and the mid pointer up to find the next
            # elements that are potentially 0 and 1
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            # Move the 'mid' pointer up, because the element is already at the correct position, no need to swap it
            mid += 1
        else:
            # Move the high pointer down. We don't move the mid pointer, because it could be a 0 or a 1
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1

    return colors
