def check_inclusion_optimized_sliding_window(s1: str, s2: str) -> bool:
    s1_len, s2_len = len(s1), len(s2)
    if s1_len > s2_len:
        return False

    s1_arr = [0] * 26
    s2_arr = [0] * 26

    for i in range(s1_len):
        x = ord(s1[i]) - ord("a")
        y = ord(s2[i]) - ord("a")
        s1_arr[x] += 1
        s2_arr[y] += 1

    count = 0
    for i in range(26):
        if s1_arr[i] == s2_arr[i]:
            count += 1

    for i in range(s2_len - s1_len):
        r = ord(s2[i + s1_len]) - ord("a")
        l = ord(s2[i]) - ord("a")

        if count == 26:
            return True
        s2_arr[r] += 1
        if s2_arr[r] == s1_arr[r]:
            count += 1
        elif s2_arr[r] == s1_arr[r] + 1:
            count -= 1

        s2_arr[l] -= 1
        if s2_arr[l] == s1_arr[l]:
            count += 1
        elif s2_arr[l] == s1_arr[l] - 1:
            count -= 1
    return count == 26


def check_inclusion_sliding_window(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)

    # If s1 is longer than s2, a permutation of s1 cannot be a substring of s2
    if n1 > n2:
        return False

    # Initialize frequency arrays for s1 and the current sliding window in s2
    # Use 26-element arrays for lowercase English letters 'a' through 'z'
    s1_counts = [0] * 26
    window_counts = [0] * 26

    # Populate s1_counts with character frequencies from s1
    for c in s1:
        s1_counts[ord(c) - ord("a")] += 1

    # Populate window_counts for the initial sliding window (first n1 characters of s2)
    for i in range(n1):
        window_counts[ord(s2[i]) - ord("a")] += 1

    # Check if the initial window is a permutation
    # This can be done by comparing the two frequency arrays
    if s1_counts == window_counts:
        return True

    # Slide the window across the rest of s2
    for i in range(n1, n2):
        # Character entering the window (at index i)
        char_added = ord(s2[i]) - ord("a")
        window_counts[char_added] += 1

        # Character leaving the window (at index i - n1)
        char_removed = ord(s2[i - n1]) - ord("a")
        window_counts[char_removed] -= 1

        # After updating the window, check if the frequencies match
        if s1_counts == window_counts:
            return True

    # If no permutation is found after checking all windows
    return False
