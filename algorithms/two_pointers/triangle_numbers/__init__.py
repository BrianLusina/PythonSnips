from typing import List


def triangle_number(heights: List[int]) -> int:
    """
    Finds the count of valid triangles that can be formed from the given input of numbers. A valid triangle is a triangle
    which has any two sides whose sum is greater than the third side. This assumes that it is okay to manipulate the
    input list. Therefore callers of this function should be aware that the input list is manipulated in place.

    Args:
        heights (list): list of integers that represent sides of a triangle
    Returns:
        int: number of valid triangles that can be formed
    """
    # If there are no heights, or we have an empty list, return 0 early as no valid triangles can be formed here.
    if not heights:
        return 0

    # Sorts the heights in place. This incurs a time complexity cost of O(n log(n)) and space cost of O(n) as this sorting
    # requires temporary storage using Python's timsort
    heights.sort()

    # Keeps track of number of valid triangles that can be formed
    count = 0

    # Iterate through the list starting from the back, idx will be at the last position, this will be the third pointer
    for idx in range(len(heights) - 1, 1, -1):
        # Initialize the two pointers to keep track of the other two indices that will point to the two other numbers that
        # can form a valid triangle.
        left = 0
        right = idx - 1

        # This is a micro-optimization to get the largest side and use it in the loop below
        largest_side = heights[idx]

        while left < right:
            # A valid triplet is found by satisfying the condition a + b > c. If this condition holds, then the other
            # two conditions hold as well, a + c > b and b + c > a.
            is_valid_triplet = heights[left] + heights[right] > largest_side
            if is_valid_triplet:
                # The numbers between the right and left pointers form valid triplets with the number at the idx position
                # we find all the possible triplets(triangles) that can be formed by finding the difference.
                count += right - left
                # we decrement right to check if there are valid triplets that can be formed by decreasing the middle valid
                right -= 1
            else:
                # Increase the left to find the next maximum minimum number that can form a valid triplet
                left += 1

    # return the count of the triangles that can be formed
    return count
