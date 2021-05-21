def longest_substring_util(s: str, start: int, end: int, k: int) -> int:
    if end < k:
        return 0

    # will hold the occurrences of each character in the string
    # counter = Counter(s)
    count_map = [0] * 26

    # build the count map which will contain the occurrences of each character in the string
    for i in range(start, end):
        count_map[ord(s[i]) - ord('a')] += 1

    # iterate through the string
    for mid in range(start, end):

        # if we find a character that is 'invalid' i.e. the frequency of the character is less than k
        # if counter.get(s[mid]) >= k:
        if count_map[ord(s[mid]) - ord('a')] >= k:
            continue

        # we now have a mid point
        mid_next = mid + 1

        # while mid_next < end and counter.get(s[mid_next]) < k:
        while mid_next < end and count_map[ord(s[mid_next]) - ord('a')] < k:
            mid_next += 1

        left_sub = longest_substring_util(s, start, mid, k)
        right_sub = longest_substring_util(s, mid_next, end, k)

        return max(left_sub, right_sub)

    return end - start


def longest_substring(s: str, k: int) -> int:
    """
    Divide and Conquer is one of the popular strategies that work in 2 phases.

    Divide the problem into subproblems. (Divide Phase).
    Repeatedly solve each subproblem independently and combine the result to solve the original problem. (Conquer Phase)
    We could apply this strategy by recursively splitting the string into substrings and combine the result to find the
    longest substring that satisfies the given condition. The longest substring for a string starting at index start and
     ending at index end can be given by,

    longestSustring(start, end) = max(longestSubstring(start, mid), longestSubstring(mid+1, end))
    Finding the split position (mid)

    The string would be split only when we find an invalid character. An invalid character is the one with a frequency
    of less than k. As we know, the invalid character cannot be part of the result, we split the string at the index
    where we find the invalid character, recursively check for each split, and combine the result.

    Algorithm

    Build the countMap with the frequency of each character in the string s.
    Find the position for mid index by iterating over the string. The mid index would be the first invalid character in
    the string.
    Split the string into 2 substrings at the mid index and recursively find the result.
    To make it more efficient, we ignore all the invalid characters after the mid index as well, thereby reducing the
    number of recursive calls.

    Complexity Analysis

    Time Complexity: O(N^2), where N is the length of string ss. Though the algorithm performs better in most cases,
    the worst case time complexity is still (N ^ 2).

    In cases where we perform split at every index, the maximum depth of recursive call could be O(N). For each
    recursive call it takes O(N) time to build the countMap resulting in O(n ^ 2) time complexity.

    Space Complexity: O(N) This is the space used to store the recursive call stack. The maximum depth of recursive
    call stack would be O(N).

    @param s: String to evaluate for
    @param k: length of the longest substring
    @return: length of longest substring with at most repeating characters of length k
    @rtype int
    """
    return longest_substring_util(s, 0, len(s), k)
