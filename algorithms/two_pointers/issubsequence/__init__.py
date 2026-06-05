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


def is_subsequence_two_pointers(s: str, t: str) -> bool:
    pointer_s, pointer_t = 0, 0
    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        pointer_t += 1

    return pointer_s == len(s)
