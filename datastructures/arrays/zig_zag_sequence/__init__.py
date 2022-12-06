from typing import List


def zig_zag_sequence(a: List[int]) -> List[int]:
    """
    Creates a zig-zag sequence from a given list of integers.

    Complexity Analysis:
    Time Complexity: First, we sort the Array in order to have the largest element at the end of the list. All sorting
    algorithms can't do better than O(nlogn)
    Space Complexity: O(1), no extra space is used as the elements are swapped in place in the input list.
    @param a: list to create zig-zag sequence from
    @return: zig-zag sequence
    """
    # Time Complexity O(nlogn), This sorts in place, so no new array is used. Space Complexity O(1)
    a.sort()

    length = len(a)
    mid_index = length // 2
    last_index = length - 1

    # swap largest element to move to the middle of the sorted list
    a[last_index], a[mid_index] = a[mid_index], a[last_index]

    # reverse remaining elements, the last half of the list, this will cost O(n/2) as we have to traverse the right side
    # of the list. That is, elements after the middle as they are not in the right order swapping them as needed
    # we have 2 pointers, the left pointer(index) will be at the element after the middle and right will be element
    # before the last element as the last element is already the smallest of that sub sequence
    left_index = mid_index + 1
    right_index = last_index - 1

    while left_index < right_index:
        a[right_index], a[left_index] = a[left_index], a[right_index]

        left_index += 1
        right_index -= 1

    return a
