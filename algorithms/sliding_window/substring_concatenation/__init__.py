from typing import List
from collections import Counter


def find_substring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []

    # Check each possible word alignment offset (0, 1, ..., word_len - 1)
    for i in range(word_len):
        left = i
        curr_freq = Counter()
        count = 0

        # Slide the window across the string in steps of word_len
        for j in range(i, len(s) - word_len + 1, word_len):
            word = s[j : j + word_len]

            if word in word_freq:
                curr_freq[word] += 1
                count += 1

                # If we have too many of this word, shrink from the left
                while curr_freq[word] > word_freq[word]:
                    left_word = s[left : left + word_len]
                    curr_freq[left_word] -= 1
                    count -= 1
                    left += word_len

                # Success! The window contains all words exactly once
                if count == word_count:
                    result.append(left)
            else:
                # Invalid word: reset the current window and move 'left' past 'j'
                curr_freq.clear()
                count = 0
                left = j + word_len

    return result


def find_substring_2(s: str, words: List[str]) -> List[int]:
    # Each word has the same length
    word_len = len(words[0])
    # Total number of words
    num_words = len(words)
    # Total length of a valid substring (all words concatenated)
    total_len = word_len * num_words
    # Frequency count of all words in the list
    word_count = Counter(words)
    # List to store all valid starting indices
    result = []

    # Check all possible starting offsets within word length range
    for i in range(word_len):
        left = i  # Left pointer for sliding window
        right = i  # Right pointer for sliding window
        seen = Counter()  # Tracks words seen in the current window

        # Slide the window across the string
        while right + word_len <= len(s):
            # Extract a word-sized substring
            word = s[right : right + word_len]
            right += word_len

            # If the word exists in the target list
            if word in word_count:
                seen[word] += 1  # Count it in the current window

                # If we’ve seen a word too many times, shrink the window from the left
                while seen[word] > word_count[word]:
                    left_word = s[left : left + word_len]
                    seen[left_word] -= 1
                    left += word_len

                # If the total window matches the length of all words, record index
                if right - left == total_len:
                    result.append(left)
            else:
                # Invalid word — reset the window
                seen.clear()
                left = right

    # Return all valid starting indices
    return result
