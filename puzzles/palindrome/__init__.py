from typing import List


def is_palindrome(a) -> bool:
    return str(a) == str(a)[::-1]


def get_longest_palindrome(s: str, start_index:int, end_index:int) -> str:
    """Gets the longest palindrome substring from a given string from a start index to an end index

    Args:
        s (str): string to search for palindrome substrings
        start_index (int): start index to start search from
        end_index (int): end index to end search for

    Returns:
        str: longest palindrome substring
    """
    while 0 <= start_index and end_index < len(s) and s[start_index] == s[end_index]:
        start_index -= 1
        end_index += 1
    return s[start_index + 1: end_index]


def smallest_palindrome(max_factor, min_factor=0):
    """
    Gets the smallest palindrome from the generator and returns the value from the operation
    :param max_factor:Largest factor to evaluate
    :param min_factor: Smallest factor to evaluate
    :return: Smallest palindrome pair product,
    :rtype:int
    """
    return min(
        generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0]
    )


def generate_palindromes(max_factor, min_factor):
    """
    Creates 2 ranges one for the minimum factor and another for the maximum factor
    The results for the first one are used to generate a range for the second one
    Then checks if the product from the result of the 2 operations is a palindrome
    Returns only if the product results to a palindrome
    :return: Tuple with the first element as the product(value) and the 2nd element as the palindrome pair that
    make the product(factors)
    :rtype: tuple
    """
    return (
        (a * b, (a, b))
        for a in range(min_factor, max_factor + 1)
        for b in range(min_factor, a + 1)
        if is_palindrome(a * b)
    )


def largest_palindrome(max_factor, min_factor=0):
    """
    Gets the maximum palindrome product from the generator function
    using the key to only fetch the value from the operation
    :param max_factor: The maximum factor or number to use
    :param min_factor: the minimum number to use, which defaults to 0 if there is no input
    :return: Maximum palindrome product from the generator
    :rtype:int
    """
    return max(
        generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0]
    )
