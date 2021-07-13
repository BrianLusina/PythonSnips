MAX_CHARS = 256


def is_isomorphic(s: str, t: str) -> bool:
    if not s or not t:
        return False

    if len(s) != len(t):
        return False

    marked = [False] * MAX_CHARS
    mapping = [None] * MAX_CHARS

    for x in range(len(t)):
        if not mapping[ord(s[x])]:

            if marked[ord(t[x])]:
                return False

            marked[ord(t[x])] = True

            mapping[ord(s[x])] = t[x]

        elif mapping[ord(s[x])] != t[x]:
            return False

    return True


def is_isomorphic_v2(s: str, t: str) -> bool:
    if not s or not t:
        return False

    if len(s) != len(t):
        return False

    mapping = {}

    for x in range(len(s)):
        if s[x] in mapping:
            if mapping[s[x]] != t[x]:
                return False
        else:
            if t[x] in mapping.values():
                return False
            else:
                mapping[s[x]] = t[x]

    return True
