from typing import Dict


def word_pattern(pattern: str, s: str) -> bool:
    """
    Check if a pattern matches a string following a bijective mapping.
    Each character in pattern should map to exactly one word in s, and vice versa.

    Args:
        pattern: A string containing the pattern (e.g., "abba")
        s: A space-separated string of words (e.g., "dog cat cat dog")

    Returns:
        True if the pattern matches the string, False otherwise
    """
    # Split the string into individual words
    words = s.split()

    # If lengths don't match, pattern cannot be followed
    if len(pattern) != len(words):
        return False

    # Dictionary to map pattern characters to words
    pattern_to_word: Dict[str, str] = {}
    # Dictionary to map words to pattern characters (ensures bijection)
    word_to_pattern: Dict[str, str] = {}

    # Iterate through pattern characters and corresponding words simultaneously
    for pattern_char, word in zip(pattern, words):
        # Check if pattern character already has a different word mappting
        if pattern_char in pattern_to_word and pattern_to_word[pattern_char] != word:
            return False

        # Check if word already has a different pattern character mapping
        if word in word_to_pattern and word_to_pattern[word] != pattern_char:
            return False

        # Establish the bidirectional mapping
        pattern_to_word[pattern_char] = word
        word_to_pattern[word] = pattern_char

    return True


def word_pattern_2(pattern: str, s: str) -> bool:
    """
    Check if a pattern matches a string following a bijective mapping.
    Each character in pattern should map to exactly one word in s, and vice versa.

    Args:
        pattern: A string containing the pattern (e.g., "abba")
        s: A space-separated string of words (e.g., "dog cat cat dog")

    Returns:
        True if the pattern matches the string, False otherwise
    """
    # Create a dictionary to store index mappings for both characters and words
    map_index: Dict[str, int] = {}

    # Split the input string into individual words
    words = s.split()

    # If the number of pattern characters and words don't match,
    # there can't be a one-to-one correspondence
    if len(pattern) != len(words):
        return False

    # Iterate through each character-word pair
    for idx in range(len(words)):
        pattern_char = pattern[idx]  # Current character in the pattern
        word = words[idx]  # Corresponding word in the string

        # Create separate keys for characters and words
        # This helps differentiate between them in the same dictionary
        char_key = f"char_{pattern_char}"
        char_word = f"word_{word}"

        # If this character hasn't been seen before, store its index
        if char_key not in map_index:
            map_index[char_key] = idx

        # If this word hasn't been seen before, store its index
        if char_word not in map_index:
            map_index[char_word] = idx

        # If the indices for the character and word don't match,
        # it means they were mapped inconsistently — return False
        if map_index[char_key] != map_index[char_word]:
            return False

    # If we finish the loop without mismatches, the pattern is valid
    return True
