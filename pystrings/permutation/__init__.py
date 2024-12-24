from typing import Dict


def check_permutation_with_sorting(input_str_1: str, input_str_2: str) -> bool:
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

def check_permutation_with_map(input_str_1: str, input_str_2: str) -> bool:
    """
    Check if two strings are permutations of each other.

    This function determines whether two input strings are permutations of one
    another by comparing the frequency of characters in each string. It considers
    case sensitivity and whitespace as significant when evaluating the two strings.

    Complexity:
    Time: O(n) as iteration is handled on each string where n is the number of characters in each string
    Space: O(n) as a dictionary is used to store characters for lookups

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

    input_str_1_lower = input_str_1.lower()
    input_str_2_lower = input_str_2.lower()

    char_count: Dict[str, int] = dict()

    # Now, if input_str_1 and input_str_2 are permutations of each other, the two for loops will counterbalance each
    # other and the values of all the keys in char_count should be 0.
    # We find this out at the end where we evaluate count == 0 for all the keys in char_count. Using the all function,
    # we combine the evaluation results from all the iterations and return it from the function. The all() function
    # returns True if all items in an iterable are True. Otherwise, it returns False.

    for char in input_str_1_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in input_str_2_lower:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    return all(count == 0 for count in char_count.values())
