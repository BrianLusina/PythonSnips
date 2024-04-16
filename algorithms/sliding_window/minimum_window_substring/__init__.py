from collections import Counter


def min_window(s: str, t: str) -> str:
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
    filtered_s = []
    for idx, char in enumerate(s):
        if char in counter_t:
            filtered_s.append((idx, char))

    left, right = 0, 0
    formed = 0
    window_counts = {}
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
