from typing import List, Tuple, Dict
from collections import Counter


def min_window(s: str, t: str) -> str:
    # If `t` is empty, return an empty string as no window is possible
    if not t:
        return ""

    # Dictionaries to store the required character counts and the current window's character counts
    req_count = {}
    window = {}

    # Populate `req_count` with the character frequencies of `t`
    for char in t:
        req_count[char] = req_count.get(char, 0) + 1

    # Variables to track the number of characters that match the required frequencies
    current = (
        0  # Count of characters in the current window that meet the required frequency
    )
    required = len(req_count)  # Total number of unique characters in `t`

    # Result variables to track the best window
    res = [-1, -1]  # Stores the start and end indices of the minimum window
    res_len = float("inf")  # Length of the minimum window

    # Sliding window pointers
    left = 0  # Left pointer of the window
    for right in range(len(s)):
        char = s[right]

        # If `char` is in `t`, update the window count
        if char in req_count:
            window[char] = window.get(char, 0) + 1
            # If the frequency of `char` in the window matches the required frequency, update `current`
            if window[char] == req_count[char]:
                current += 1

        # Try to contract the window while all required characters are present
        while current == required:
            # Update the result if the current window is smaller than the previous best
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Shrink the window from the left
            left_char = s[left]
            if left_char in req_count:
                # Decrement the count of `left_char` in the window
                window[left_char] -= 1
                # If the frequency of `left_char` in the window is less than required, update `current`
                if window[left_char] < req_count[left_char]:
                    current -= 1
            left += 1  # Move the left pointer to shrink the window

    # Return the minimum window if found, otherwise return an empty string
    return s[res[0] : res[1] + 1] if res_len != float("inf") else ""


def min_window_2(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    if t == s:
        return s

    if not t or not s:
        return ""

    counter_t = Counter(t)

    required = len(counter_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s: List[Tuple[int, str]] = []
    for idx, char in enumerate(s):
        if char in counter_t:
            filtered_s.append((idx, char))

    left, right = 0, 0
    formed = 0
    window_counts: Dict[str, int] = {}
    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while right < len(filtered_s):
        char = filtered_s[right][1]
        window_counts[char] = window_counts.get(char, 0) + 1

        if window_counts[char] == counter_t[char]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while left <= right and formed == required:
            char = filtered_s[left][1]

            end = filtered_s[right][0]
            start = filtered_s[left][0]

            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[char] -= 1
            if window_counts[char] < counter_t[char]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("Inf") else s[ans[1] : ans[2] + 1]
