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
    low, mid, high = 0, 0, len(colors) - 1

    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            mid += 1
        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1

    return colors


def sort_colors_v2(colors: List[int]) -> List[int]:
    """
    Sorts a list of 0s, 1s, and 2s in place using two pointers

    This algorithm uses two pointers: low and high. The low pointer is used to track the position where the next 0
     should be placed, and the high pointer is used to track the position where the next 2 should be placed.

    The algorithm works by iterating through the list with the low pointer. If it encounters a 0, it simply increments
    low. If it encounters a 2, it decrements high. If it encounters a 1, it swaps it with the element at the high index
    and decrements high. This swapping process ensures that all the 1s are placed between the 0s and the 2s.

    This algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for sorting lists
    of 0s, 1s, and 2s using only two pointers.

    Args:
        colors (list): list of 0s, 1s, and 2s
    Returns:
        list: sorted list of 0s, 1s, and 2s
    """
    red, blue = 0, len(colors) - 1
    i = 0
    while i <= blue:
        if colors[i] == 0:
            colors[red], colors[i] = colors[i], colors[red]
            red += 1
            i += 1
        elif colors[i] == 2:
            colors[blue], colors[i] = colors[i], colors[blue]
            blue -= 1
        else:
            i += 1
    return colors
