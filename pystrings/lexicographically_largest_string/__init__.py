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

# Function to find the lexicographically largest string
def lexicographically_largest_string_from_box_2(word: str, num: int) -> str:
    if num == 1:
        return word

    n = len(word)
    i, j = 0, 1

    while j < n:
        k = 0
        while j + k < n and word[i + k] == word[j + k]:
            k += 1

        if j + k < n and word[i + k] < word[j + k]:
            temp_index = i
            i = j
            j = max(j + 1, temp_index + k + 1)
        else:
            j = j + k + 1

    return word[i : min(n, i + n - num + 1)]
