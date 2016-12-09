def common_ground(s1, s2):
    lst = []
    for w in s2.split():
        if w in s1.split() and w not in lst:
            lst.append(w)
    return ' '.join(lst) if lst else "death"
