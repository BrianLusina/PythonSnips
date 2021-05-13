def clean_string(s):
    if len(s) == 0:
        return s

    q = []

    for idx in range(len(s)):

        if s[idx] != "#":
            q.append(s[idx])
        elif len(q) != 0:
            q.pop()

    return "".join(q)
