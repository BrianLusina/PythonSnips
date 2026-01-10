from typing import List
from . import is_palindrome


def palindrome_pairs(words: List[str]) -> List[List[int]]:
    """
    Loops through the word_list and checks if the current word is a palindrome of any of the preceding words
    or if the preceding words are a palindrome of the current
    :param words: list of words to evaluate for palindrome pairs
    :return: list of lists with each list containing the word indices which form a palindrome
    """

    return [
        [i, j]
        for i, word_i in enumerate(words)
        for j, word_j in enumerate(words)
        if i != j and is_palindrome(word_i + word_j)
    ]


def palindrome_pairs_2(words: List[str]) -> List[List[int]]:
    """

    @param words:
    @return: 2D array with indices of the palindrome pairs
    """
    result = []

    # create a dictionary to store the reverse of words and their indices
    reversed_words_map = {word[::-1]: i for i, word in enumerate(words)}

    for index, word in enumerate(words):
        # check if empty string is in the dictionary and the current word is palindrome
        if (
            "" in reversed_words_map
            and reversed_words_map[""] != index
            and is_palindrome(word)
        ):
            # append the indices to the result list
            result.append([index, reversed_words_map[""]])

        # iterate through the word characters
        for j in range(1, len(word) + 1):
            left_substring = word[:j]  # get the left substring
            right_substring = word[j:]  # get the right substring

            # check if left substring is in the dictionary and the right substring is palindrome
            if (
                left_substring in reversed_words_map
                and reversed_words_map[left_substring] != index
                and is_palindrome(right_substring)
            ):
                # append the indices to the result list
                result.append([index, reversed_words_map[left_substring]])

            # check if right substring is in the dictionary and the left substring is palindrome
            if (
                right_substring in reversed_words_map
                and reversed_words_map[right_substring] != index
                and is_palindrome(left_substring)
            ):
                # append the indices to the ans list
                result.append([reversed_words_map[right_substring], index])

    return result
