def lexicographically_largest_string_from_box(word: str, num: int) -> str:
    if num == 1:
        return word

    n = len(word)
    max_substring = ""

    # Iterate through every possible starting character of a substring
    for i in range(n):
        # We want to find the longest valid substring starting at i.
        # To do this, we assume this substring acts as the m-th part
        # of the split, where m is as large as possible (latest slot).

        # If we start at 0, we MUST be the 1st part.
        if i == 0:
            m = 1
        else:
            # If we start later, we can be at most the (i+1)-th part
            # (since parts 1..m-1 need at least 1 char each).
            # We are also capped by the total number of friends.
            if num == 1:
                # If only 1 num, the part MUST start at 0. i > 0 is invalid.
                continue
            m = min(num, i + 1)

        # Calculate how many parts must come AFTER this one
        parts_after = num - m

        # The substring must end early enough to leave 1 char
        # for each remaining part.
        j = n - parts_after

        # If the derived end index j is not greater than i,
        # this split isn't possible (substring would be empty).
        if j > i:
            candidate = word[i:j]
            if candidate > max_substring:
                max_substring = candidate

    return max_substring


def lexicographically_largest_string_from_box_2(word: str, num: int) -> str:
    # If there's only one friend, no split is needed; return the entire string
    if num == 1:
        return word

    n = len(word)
    # i: start index of current best substring, j: candidate start index
    i, j = 0, 1

    while j < n:
        k = 0
        # Compare characters at i+k and j+k as long as they're equal and in bounds
        while j + k < n and word[i + k] == word[j + k]:
            k += 1

        # If the candidate substring starting at j is better, update i
        if j + k < n and word[i + k] < word[j + k]:
            # save current i to compute safe next j
            temp_index = i
            # move i to a better candidate
            i = j
            # skip redundant comparisons
            j = max(j + 1, temp_index + k + 1)
        else:
            # Otherwise, continue searching by skipping the compared section
            j = j + k + 1

    # Return the best substring of required length: len(word) - numFriends + 1
    return word[i : min(n, i + n - num + 1)]
