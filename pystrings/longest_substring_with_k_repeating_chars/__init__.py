def longest_substring_util(s: str, start: int, end: int, k: int) -> int:
    if end < k:
        return 0

    count_map = [0] * 26

    for i in range(start, end):
        count_map[ord(s[i]) - ord('a')] += 1

    for mid in range(start, end):
        if count_map[ord(s[mid]) - ord('a')] >= k:
            continue

        mid_next = mid + 1

        while mid_next < end and count_map[ord(s[mid_next]) - ord('a')] < k:
            mid_next += 1

        return max(longest_substring_util(s, start, mid, k), longest_substring_util(s, mid_next, end, k))

    return end - start


def longest_substring(s: str, k: int) -> int:
    return longest_substring_util(s, 0, len(s), k)
