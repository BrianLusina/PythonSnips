from typing import List


def compress(chars: List[str]) -> int:
    if len(chars) <= 1:
        return len(chars)

    # idx represents the first index of the current group
    idx, res = 0, 0

    while idx < len(chars):
        # current group length
        group_length = 1

        # find the length of the current group of repeating characters
        while idx + group_length < len(chars) and chars[idx + group_length] == chars[idx]:
            group_length += 1

        chars[res] = chars[idx]
        res += 1

        # if the group length is greater than 1, add the string representation of it to the answer
        if group_length > 1:
            group_length_str = f"{group_length}"
            chars[res: res + len(group_length_str)] = group_length_str
            res += len(group_length_str)

        # proceed to the next group
        idx += group_length

    return res
