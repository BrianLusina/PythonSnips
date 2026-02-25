from typing import List


def peak_of_mountain(arr: List[int]) -> int:
    """
    The array strictly increases until the peak element and then strictly decreases. The monotonicity is a strong sign
    that we can use binary search to find the peak element.

    To use binary search though, we need the entire search range to be strictly increasing or decreasing. We need to
    find the feasible function that returns false for elements up until the peak and true from the peak to the end.

    We already know the array strictly decreases from the peak element to the last element. So we can try to use a
    feasible function of arr[i]> arr[i+1] to return true for elements from the peak to the last element. Once we do
    that, we realize that also returns false from the first element to the peak element. We got our feasible function.

    A minor edge case is for the last element as it has no next element. We can pad the array with an imaginary node
    of negative infinity. In the implementation, we don't actually need to pad the array as that would incur O(n)
    extra cost. We can just check if i+1 is out of bounds and return true if it is since this implies arr[i] is the
    last element.
    """
    left = 0
    right = len(arr) - 1
    k = -1

    while left <= right:
        mid = (left + right) // 2

        if mid == len(arr) - 1 or arr[mid] > arr[mid + 1]:
            k = mid
            right = mid - 1
        else:
            left = mid + 1

    return k
