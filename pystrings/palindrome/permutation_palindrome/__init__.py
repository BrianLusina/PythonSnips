from typing import Dict


def has_palindrome_permutation(some_string: str) -> bool:
    # normalizes the string by removing white spaces and then lowercases the result
    input_string = some_string.replace(" ", "").lower()

    # keep track of oddly appearing char
    unpaired_chars = set()

    for char in input_string:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    # the string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_chars) <= 1


def is_palindrome_permutation(input_string: str) -> bool:
    """
    Checks if a given input string is a palindrome permutation and returns True if it is.
    Args:
        input_string (str): input string to evaluate
    Return:
        bool: True if the given input string is a palindrome permutation
    """
    # normalizes the string by removing white spaces and then lowercases the result
    normalized_string = input_string.replace(" ", "").lower()

    # keeps count of the characters in the string
    char_count: Dict[str, int] = dict()

    # loop through the string to check if a given character is in the dictionary, if it is, the count is incremented
    # otherwise, it is added and set to 1
    # note that this is an O(n) operation as the loop has to iterate through all the characters in the string
    for char in normalized_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for char, count in char_count.items():
        # check if the count is an odd number and odd_count equal 0. If for some char, count is odd and odd_count is 0
        # we increment odd_count by 1. In this way, we are recording for an instance if we have encountered the middle
        # element of an odd-length string. However. if count is an odd number, but odd_count equals something other
        # than 0, it implies that there is more than one character which has an odd number of occurrences in input_str.
        # Therefore, False is returned
        if count % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif count % 2 != 0 and odd_count != 0:
            return False

    return True
