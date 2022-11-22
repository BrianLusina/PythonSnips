def length_of_longest_substring(s: str) -> int:
    """
    Retrieves the length of the longest substring from a string that does not have repeating characters.
    This uses a Sliding window technique and a dictionary to keep track of the characters visited.
    We have a left & a right pointer which we use to determine a particular substring, The right pointer is moved
    constantly as we move through the string. If a character that has been seen before(in the dictionary) is encountered
    the left pointer is moved to the next position.
    If the character has not yet been encountered, it's stored in a dictionary(visited) where the key is the character
    & the value is the right pointer's location.
    The max length is then determined from the maximum of the current maximum length and the right position's index
    minus left position index + 1

    Complexity Analysis:
        Time: O(n) where n is the length of the string as we travers characters in the string
        Space: O(n) as we are storing the characters visited in a dictionary

    @param s: input string
    @return: length of the longest substring without repeating characters
    """
    visited = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        char = s[right]

        if char in visited:
            left = max(left, visited[char] + 1)
        visited[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
