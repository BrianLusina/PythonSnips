def longest_self_contained_substring(s: str) -> int:
    """
    Finds the longest self-contained substring in a given string.

    A self-contained substring is one where each character only appears within the substring itself.
    The function returns the length of the longest self-contained substring, and -1 if no such substring exists.

    Parameters:
        s (str): The input string.

    Returns:
        int: The length of the longest self-contained substring, or -1 if no such substring exists.

    Examples:
        >>> longest_self_contained_substring("xyyx")
        2
        >>> longest_self_contained_substring("xyxy")
        -1
        >>> longest_self_contained_substring("abacd")
        4

    Note:
        This implementation uses a brute-force approach with O(n³) time complexity.
        For better performance, consider using max_substring_length() which runs in O(n).
    """
    n = len(s)

    # First, find the first and last occurrence of each character
    # This helps us quickly check if a character appears outside a range
    first_occurrence = {}
    last_occurrence = {}

    for i, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = i
        last_occurrence[char] = i

    max_length = -1

    # Try all possible substrings (excluding the entire string)
    for start in range(n):
        for end in range(start, n):
            # Skip the entire string
            if start == 0 and end == n - 1:
                continue

            # Check if this substring is self-contained
            substring = s[start:end + 1]
            is_self_contained = True

            # For each character in the substring, verify it doesn't appear outside
            for char in set(substring):
                # If the character's first occurrence is before our start
                # or last occurrence is after our end, it appears outside
                if first_occurrence[char] < start or last_occurrence[char] > end:
                    is_self_contained = False
                    break

            # If self-contained, update our maximum
            if is_self_contained:
                max_length = max(max_length, end - start + 1)

    return max_length


def max_substring_length(s: str) -> int:
    """
    Finds the length of the longest substring of s that is self-contained.

    A self-contained substring is one in which all characters only appear within the substring.

    The function uses an optimized window expansion approach. For each unique character as a starting point,
    it defines an initial window from the character's first to last occurrence. The window is expanded to include
    all occurrences of characters within it, and is invalidated if any character's first occurrence lies before
    the window start.

    Parameters:
        s (str): The string to find the longest self-contained substring of

    Returns:
        int: The length of the longest self-contained substring of s

    Examples:
        >>> max_substring_length("xyyx")
        2
        >>> max_substring_length("xyxy")
        -1
        >>> max_substring_length("abacd")
        4

    Note:
        Time complexity: O(n), Space complexity: O(1) for fixed character set size.
    """
    first = {}
    last = {}
    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    max_len = -1

    for c1 in first:
        start = first[c1]
        end = last[c1]
        j = start

        while j < len(s):
            c2 = s[j]
            if first[c2] < start:
                break
            end = max(end, last[c2])
            if end == j and end - start + 1 != len(s):
                max_len = max(max_len, end - start + 1)
            j += 1

    return max_len
