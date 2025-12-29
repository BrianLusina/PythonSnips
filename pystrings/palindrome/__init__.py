def is_palindrome(phrase: str) -> bool:
    """
    Checks if a given passed in phrase or sequence of characters in any type is a palindrome, i.e. reads the same forwards
    as it does backwards.

    This does this in linear time using constant extra space

    Time: O(n) where n is the length of the passed in phrase
    Space: O(1) as no extra space is used as the iteration happens on the provided input

    This is achieved by using two pointers, one at the left or the beginning of the string and the other at the end or
    the end of the string. A while loop is used to iterate through both ends of the string as long as the left pointer
    is less than the right pointer.

    There are two while loops in the parent while loop:
    The first checks that the character at the position of the left pointer is not alphanumeric and that it is less
    than the right pointer and if this condition is met, the left pointer is advanced forward(1 is added to it).

    Similar case to the second while loop, which checks for this condition in the reverse. If the character at the
    right pointer is not an alphanumeric character and the right pointer is greater than the left pointer, then it is
    decremented by 1, moving it backwards.

    The palindrome property is checked by comparing the current lower case version of the character at the position of
    the left pointer and the current lower case version of the character at the position of the right pointer and if
    they do not match, False is returned immediately. If they are equal, the left pointer and the right pointer are
    incremented and decremented respectively to proceed to the next set of characters.

    If the condition of this match stays false for all possible iterations of the while loop, True is returned at the
    end indicating that the phrase is indeed a palindrome.

    Args:
        phrase (str): the phrase to check for whether it meets the criteria of being a palindrome
    Returns:
        bool: returns True if it's a palindrome, False otherwise
    """

    left_pointer = 0
    right_pointer = len(phrase) - 1

    while left_pointer < right_pointer:
        while not phrase[left_pointer].isalnum() and left_pointer < right_pointer:
            left_pointer += 1
        while not phrase[right_pointer].isalnum() and left_pointer < right_pointer:
            right_pointer -= 1

        if phrase[left_pointer].lower() != phrase[right_pointer].lower():
            return False

        left_pointer += 1
        right_pointer -= 1

    return True


def get_longest_palindrome(s: str, start_index: int, end_index: int) -> str:
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
    return s[start_index + 1 : end_index]


def smallest_palindrome(max_factor, min_factor=0):
    """
    Gets the smallest palindrome from the generator and returns the value from the operation
    :param max_factor:Largest factor to evaluate
    :param min_factor: Smallest factor to evaluate
    :return: Smallest palindrome pair product,
    :rtype:int
    """
    return min(generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0])


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
    return max(generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0])


def is_palindrome_number(x: int) -> bool:
    """
    Checks if a number is a palindrome
    Args:
        x(int): number
    Returns:
        bool: True if it is a palindrome, False otherwise
    """
    # Negative numbers are never palindromes.
    # Also, any number ending in 0 (except 0 itself) cannot be a palindrome.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0  # This will store the reversed last half of the digits.

    # Reverse only half of the number.
    # Stop when the reversed half becomes >= the remaining half.
    while x > reversed_half:
        last_digit = x % 10  # Extract last digit
        reversed_half = reversed_half * 10 + last_digit  # Build reversed number
        x //= 10  # Remove last digit from x

    # If the number has even digits, check x == reversedHalf.
    # If odd digits, the middle digit doesn't matter, so remove it using //10.
    # If either of the above are True, return True. Otherwise, False
    if x == reversed_half or x == reversed_half // 10:
        return True
    else:
        return False


def is_palindrome_number_2(x: int) -> bool:
    """
    Checks if a number is a palindrome
    Args:
        x(int): number
    Returns:
        bool: True if it is a palindrome, False otherwise
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    num_str = str(x)
    left = 0
    right = len(num_str) - 1

    while left < right:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    return True
