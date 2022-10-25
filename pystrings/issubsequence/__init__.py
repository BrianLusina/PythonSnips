def is_subsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    seek = 0

    for i in range(len(t)):
        if s[seek] == t[i]:
            seek += 1
        if seek == len(s):
            return True

    return False


def is_subsequence_v2(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    if i == len(s):
        return True
    return False
