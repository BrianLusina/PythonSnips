def length_of_longest_substring(s: str) -> int:
    """
    The most obvious way to do this would be to go through all possible substrings of the string which would result in
    an algorithm with an overall O(n^2) complexity.

    But we can solve this problem using a more subtle method that does it with one linear traversal( O(n)complexity ).

    First,we go through the string one by one until we reach a repeated character. For example if the string is
    “abcdcedf”, what happens when you reach the second appearance of "c"?

    When a repeated character is found(let’s say at index j), it means that the current substring (excluding the
    repeated character of course) is a potential maximum, so we update the maximum if necessary. It also means that the
    repeated character must have appeared before at an index i, where i<j

    Since all substrings that start before or at index i would be less than the current maximum, we can safely start
    to look for the next substring with head which starts exactly at index i+1.
    """
    # creating set to store last positions of occurrence
    seen = {}
    max_length = 0
    # staring the initial window at 0
    start = 0

    for end in range(len(s)):

        # have we seen this element already?
        if s[end] in seen:
            # move the start pointer to position after last occurrence
            start = max(start, seen[s[end]] + 1)

        # update last seen value of character
        seen[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length
