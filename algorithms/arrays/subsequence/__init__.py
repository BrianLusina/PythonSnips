from typing import List


def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    """
    Returns true if a sequence is a subsequence of the provided array

    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
    order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array
    [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid
    subsequences of the array.

    Time complexity: O(n) - where n is the length of the array. We iterate through the array once to find the first
    element in the sequence. Then, we iterate through the sequence once to check if the current element in the array is

    Space complexity: O(1) - we only use a constant amount of extra space to store variables and do not depend on the
    input size.

    Args:
        array (list): A non-empty array of integers.
        sequence (list): A non-empty array of integers.

    Returns:
        A boolean that indicates whether the second array is a subsequence of the first one.
    """
    # a sequence that is longer than the array is not a valid subsequence
    if len(sequence) > len(array) or len(array) == 0 or len(sequence) == 0:
        return False

    seek = 0

    for i in range(len(array)):
        if sequence[seek] == array[i]:
            seek += 1
        if seek == len(sequence):
            return True

    return False


def is_valid_subsequence_v2(array: List[int], sequence: List[int]) -> bool:
    """
    Returns true if a sequence is a subsequence of the provided array

    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
    order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array
    [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid
    subsequences of the array.

    Time complexity: O(n) - where n is the length of the array. We iterate through the array once to find the first
    element in the sequence. Then, we iterate through the sequence once to check if the current element in the array is

    Space complexity: O(1) - we only use a constant amount of extra space to store variables and do not depend on the
    input size.

    Args:
        array (list): A non-empty array of integers.
        sequence (list): A non-empty array of integers.

    Returns:
        A boolean that indicates whether the second array is a subsequence of the first one.
    """
    i, j = 0, 0

    while i < len(sequence) and j < len(array):
        if sequence[i] == array[j]:
            i += 1
        j += 1

    if i == len(sequence):
        return True
    return False
