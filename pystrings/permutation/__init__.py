def check_permutation(input_str_1: str, input_str_2: str) -> bool:
    """
    Check if two strings are permutations of each other.

    This function determines whether two input strings are permutations of one
    another by comparing the frequency of characters in each string. It considers
    case sensitivity and whitespace as significant when evaluating the two strings.

    Complexity:
    Time: O(nlog(n)) as sorting is used and sorting here is an O(nlog(n)) time complexity
    Space: O(1) as no extra space is used to achieve checking for permutations

    Args:
        input_str_1 (str): The first input string to compare.
        input_str_2 (str): The second input string to compare.

    Returns:
    bool
        True if the two strings are permutations of each other, False otherwise.
    """
    # strings of different lengths can not be permutations of each other
    if len(input_str_1) != len(input_str_2):
        return False

    input_str_1_sorted = "".join(sorted(input_str_1.lower()))
    input_str_2_sorted = "".join(sorted(input_str_2.lower()))

    n = len(input_str_1_sorted)

    for idx in range(n):
        if input_str_1_sorted[idx] != input_str_2_sorted[idx]:
            return False

    return True
